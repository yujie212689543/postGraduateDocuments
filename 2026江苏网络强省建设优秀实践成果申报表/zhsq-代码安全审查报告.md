# zhsq-backstage 代码安全审查报告

> 审查日期：2026-05-22
> 项目：zhsq-backstage-2.0 (Spring Cloud Gateway + OAuth2 微服务网关)
> 审查范围：网关层、通用工具类、安全配置

---

## 摘要

本次审查共发现 **10 个原始安全问题**，经 AI 过滤后保留 **7 个有效漏洞**：

| 严重性 | 数量 |
|--------|------|
| HIGH | 6 |
| MEDIUM | 1 |
| LOW | 0 |

---

## 有效漏洞详情

---

### Vuln 1: CORS 配置错误（通配符 + 凭据冲突）

- **严重性：** HIGH
- **置信度：** 9/10
- **文件：** `CorsConfig.java:27-29`
- **描述：** `config.setAllowCredentials(true)` 与 `config.addAllowedOrigin("*")` 同时使用。根据 CORS 规范，当 `Access-Control-Allow-Credentials` 为 `true` 时，`Access-Control-Allow-Origin` 不能为 `*`。Spring 的 `CorsWebFilter` 在某些版本中不会阻止这种配置，导致浏览器行为不可预测。
- **攻击场景：** 攻击者搭建恶意站点 → 诱导已登录用户访问 → 浏览器发送带凭据的跨域请求 → 如果某些浏览器不严格执行规范，攻击者可读取响应数据。
- **修复建议：** 将 `addAllowedOrigin("*")` 改为明确的允许域名列表，或使用 `addAllowedOriginPattern("*")`（Spring 5.3+ 支持的模式匹配）。

---

### Vuln 2: 客户端凭据通过 URL 查询参数明文传输

- **严重性：** HIGH
- **置信度：** 9/10
- **文件：** `BasicHttpAuthFilter.java:29-33`
- **描述：** 在 `/oauth/token` 路径上，`appid` 和 `secret` 从 URL 查询参数中获取，拼接后构造 Basic Auth 头。URL 查询参数会被记录在 Nginx/Apache 访问日志、Spring 请求日志、浏览器历史中。
- **攻击场景：** 运维人员或攻击者获取到服务器访问日志 → 从 URL 中提取 `appid` 和 `secret` → 使用窃取的凭据调用 OAuth2 token 端点获取 access token → 以该客户端身份访问所有 API。
- **修复建议：** 客户端凭据应通过 `Authorization: Basic` 头传递，而不是 URL 查询参数。前端应在客户端对凭据进行 Base64 编码后放入请求头。

---

### Vuln 3: AES 硬编码密钥 + ECB 模式

- **严重性：** HIGH
- **置信度：** 10/10
- **文件：** `AESUtil.java:21, 105`
- **描述：** AES 密钥 `"20231025HelloDog"` 硬编码在源码中，使用 `AES/ECB/PKCS5Padding` 模式。ECB 模式不提供语义安全性——相同的明文块产生相同的密文块，且无法抵御重放攻击。密钥硬编码意味着所有部署实例共享同一个密钥。
- **攻击场景：** 攻击者通过源码泄露、反编译 jar 或内部访问获取密钥 → 解密所有使用该 AES 加密的数据（包括用户个人信息）。
- **修复建议：** 1) 将密钥移至环境变量或配置中心（如 Nacos/Spring Cloud Config）；2) 将 ECB 模式改为 GCM 或 CBC + 随机 IV；3) 定期轮换密钥。

---

### Vuln 4: SSL 证书验证完全禁用

- **严重性：** HIGH
- **置信度：** 10/10
- **文件：** `application.yml:7-8`
- **描述：** `spring.cloud.gateway.httpclient.ssl.use-insecure-trust-manager: true` 禁用了所有 SSL/TLS 证书链验证。网关对外部 HTTPS 请求（如 `https://218.90.184.178:8443` 的 `openApi` 路由）不验证服务器证书的有效性。
- **攻击场景：** 攻击者在网络路径上部署中间人代理 → 网关与后端之间的 HTTPS 连接被拦截 → 攻击者可以读取和篡改所有 API 请求/响应数据。
- **修复建议：** 移除该配置，使用正确的信任证书。如果需要自签名证书，应将 CA 证书导入 Java 信任库（cacerts）而不是全局禁用验证。

---

### Vuln 5: Token 通过 URL 查询参数传递

- **严重性：** MEDIUM
- **置信度：** 8/10
- **文件：** `TokenUtil.java:20`
- **描述：** `request.getParameter(OAuth2AccessToken.ACCESS_TOKEN)` 从 URL 查询参数获取 access_token。Token 出现在 URL 中会：1) 记录在服务器访问日志；2) 通过 Referer 头泄露给第三方站点；3) 出现在浏览器历史中。
- **攻击场景：** 用户点击站外链接 → 浏览器发送 Referer 头（包含当前页面的完整 URL，其中带有 token）→ 第三方站点从 Referer 中提取 token。
- **修复建议：** 仅从 `Authorization: Bearer` 头获取 token，移除 `getParameter(ACCESS_TOKEN)` 回退逻辑。

---

### Vuln 6: 硬编码 RSA 私钥（RSATools.java）

- **严重性：** HIGH
- **置信度：** 10/10
- **文件：** `RSATools.java:273-274, 293-294`
- **描述：** `RSATools.java` 的 `testSign2()` 和 `testSign()` 方法中硬编码了完整的 1024 位 RSA 私钥（Base64 编码）。这些测试方法中的私钥如果被用于生产签名验证，任何获取到源码的人都可以伪造签名。
- **攻击场景：** 攻击者获取源码（GitHub 泄露、内部人员、反编译）→ 提取私钥 → 伪造 API 请求的签名 → 绕过签名验证机制。
- **修复建议：** 1) 删除 main 方法中的硬编码私钥；2) 生产私钥应存储在密钥管理服务（如 AWS KMS、HashiCorp Vault）或环境变量中；3) 使用独立的测试密钥（与生产隔离）。

---

### Vuln 7: 硬编码 RSA 私钥（SignUtil.java）

- **严重性：** HIGH
- **置信度：** 10/10
- **文件：** `SignUtil.java:80`
- **描述：** `SignUtil.main()` 方法中硬编码了完整的 2048 位 RSA 私钥。该工具类用于签名生成和验证，硬编码的私钥如果被用于生产环境，后果同上。
- **攻击场景：** 同上。
- **修复建议：** 同上。

---

## 已排除的发现（3 项）

| # | 标题 | 排除原因 |
|---|------|---------|
| 1 | RSA 1024 位弱密钥（RSATools.java:61） | 置信度 6/10 — 虽然是弱密钥，但实际破解需要大量计算资源，属于 defense-in-depth 问题 |
| 2 | System.out.println 调试信息泄露（TraceFilter.java:40, ReadRequestBody.java:19） | 置信度 5/10 — stdout 在生产环境通常不持久化，泄露风险有限 |
| 3 | CSRF 完全禁用（ResourceServerConfiguration.java:73） | 置信度 5/10 — 网关主要服务于 REST API（使用 Bearer token），CSRF 攻击面有限 |

---

## 修复优先级建议

| 优先级 | 漏洞编号 | 修复难度 | 影响范围 |
|--------|---------|---------|---------|
| P0 | Vuln 2, 4, 6, 7 | 低 | 凭据泄露 / MITM / 签名伪造 |
| P1 | Vuln 3 | 中 | 加密数据可解密 |
| P2 | Vuln 1, 5 | 低 | 跨域 / Token 泄露 |

---

*报告由 Hermes Agent 安全审查技能自动生成*