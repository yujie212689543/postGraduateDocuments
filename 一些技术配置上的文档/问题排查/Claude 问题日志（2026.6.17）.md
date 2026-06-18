# Claude Code CLI 故障排查记录（2026-06-17）

## 一、问题现象

2026-06-17 上午，发现 Claude Code 无法正常使用。

### 终端表现

执行：

```bash
Claude
```

报错：

```bash
zsh: permission denied: Claude
```

执行：

```bash
claude
```

报错：

```bash
zsh: permission denied: claude
```

执行：

```bash
which claude
```

结果：

```bash
claude not found
```

---

### Obsidian 表现

Claudian 插件无法启动 Claude Code。

错误信息：

```text
Failed to spawn Claude Code process:
spawn /Users/gu/.npm-global/bin/claude EACCES
```

---

### VSCode 表现

VSCode 中的 Claude 插件可以正常使用。

因此初步判断：

- Claude 服务本身正常
    
- Anthropic 账号正常
    
- 问题发生在本地 CLI 环境
    

---

## 二、排查过程

### 1. 检查 Claude 可执行文件

执行：

```bash
ls -l /Users/gu/.npm-global/bin/claude
```

结果：

```bash
lrwxr-xr-x
claude -> ../lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
```

发现：

- claude 是软链接
    
- 指向 claude.exe
    

当时怀疑：

- 安装了 Windows 版本
    
- npm 安装异常
    

后续证明该判断不准确。

---

### 2. 检查 npm 安装状态

尝试重新安装：

```bash
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
```

出现错误：

```bash
ENOTEMPTY: directory not empty, rename
```

具体路径：

```text
~/.npm-global/lib/node_modules/@anthropic-ai/claude-code
```

说明 npm 无法完成卸载。

---

### 3. 检查残留目录

执行：

```bash
ls -lah ~/.npm-global/lib/node_modules/@anthropic-ai/
```

发现：

```text
.claude-code-DPwwALqB
claude-code
```

说明：

- 上一次安装或升级过程中断
    
- npm 创建了临时目录
    
- 临时目录未成功删除
    

导致：

```text
npm 卸载失败
→ npm 安装失败
→ Claude Code 状态损坏
```

---

### 4. 清理残留

执行：

```bash
rm -rf ~/.npm-global/lib/node_modules/@anthropic-ai/claude-code

rm -rf ~/.npm-global/lib/node_modules/@anthropic-ai/.claude-code-DPwwALqB
```

彻底删除损坏安装。

---

### 5. 重新安装

执行：

```bash
npm install -g @anthropic-ai/claude-code
```

安装成功：

```bash
added 2 packages in 46s
```

重新生成：

```bash
~/.npm-global/bin/claude
```

软链接。

---

### 6. 验证安装

执行：

```bash
Claude --version
```

输出：

```bash
2.1.179 (Claude Code)
```

安装恢复正常。

---

### 7. 验证 claude.exe

执行：

```bash
file ~/.npm-global/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
```

输出：

```text
Mach-O 64-bit executable arm64
```

结论：

虽然文件名是：

```text
claude.exe
```

但实际上是：

```text
macOS ARM 原生可执行文件
```

并非 Windows 程序。

因此：

```text
.exe 文件名 ≠ Windows 可执行文件
```

不能仅根据扩展名判断问题。

---

## 三、根因分析

真实问题链路如下：

```text
Claude Code 更新或安装过程中断
↓
npm 留下临时目录

.claude-code-DPwwALqB

↓
npm 后续卸载失败

ENOTEMPTY

↓
Claude Code 安装状态损坏

↓
Obsidian Claudian 调用失败

spawn ... EACCES

↓
CLI 无法正常使用
```

---

## 四、为什么 VSCode 能用

当时现象：

```text
Obsidian 失败
VSCode 正常
```

原因可能是：

### Obsidian

依赖系统 Claude CLI：

```text
~/.npm-global/bin/claude
```

因此受到损坏安装影响。

---

### VSCode

可能使用：

- 内置 Runtime
    
- 内置 Claude SDK
    
- 独立调用方式
    

因此未受影响。

结论：

```text
VSCode 正常
≠
系统 Claude CLI 正常
```

---

## 五、最终修复命令

### 清理损坏安装

```bash
rm -rf ~/.npm-global/lib/node_modules/@anthropic-ai/claude-code

rm -rf ~/.npm-global/lib/node_modules/@anthropic-ai/.claude-code-*
```

### 重新安装

```bash
npm install -g @anthropic-ai/claude-code
```

### 验证

```bash
Claude --version
```

---

## 六、经验总结

### 1. 遇到 ENOTEMPTY

优先检查：

```bash
ls -lah ~/.npm-global/lib/node_modules/
```

是否存在：

```text
.xxx-random-string
```

残留目录。

---

### 2. 不要被 .exe 迷惑

检查真实文件类型：

```bash
file 文件路径
```

例如：

```bash
file claude.exe
```

结果比文件扩展名更可靠。

---

### 3. 先验证 CLI

出现插件问题时优先测试：

```bash
claude --version
```

如果这里失败：

```text
先修 CLI
再修插件
```

---

### 4. 记录的最终结论

本次故障不是：

- Anthropic 服务异常
    
- Obsidian Bug
    
- macOS 权限问题
    
- Claude Code 程序损坏
    

而是：

```text
npm 全局安装残留目录
导致 Claude Code 处于半安装状态
最终引发 CLI 和 Obsidian 调用失败
```