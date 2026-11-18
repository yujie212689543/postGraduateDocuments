# Telegram Turbo Downloader 使用指南

> 适用版本：`0.1.3`  
> 安装位置：`/Users/gu/Documents/telegram-turbo-downloader`  
> 适用系统：macOS  
> 使用要求：Telegram 账号、可用的 VPN/代理、Python 运行环境

## 1. 这是什么

`telegram-turbo-downloader` 是一个终端版 Telegram 高速下载工具，主要用于：

- 浏览 Telegram 频道、群组和机器人中的文件
- 从“收藏夹 / Saved Messages”下载自己保存的文件
- 对单个文件进行多连接分块下载
- 批量排队下载多个文件
- 中断后继续下载

程序采用“终端用户界面（TUI）”，不需要鼠标操作。

> 注意：该程序仍是 Alpha 阶段，GitHub 上的 Stars 很少。建议只从项目官方仓库和可信来源使用，不要随意下载修改版。

## 2. 当前安装状态

程序已经安装在这里：

```text
/Users/gu/Documents/telegram-turbo-downloader
```

专用 Python 虚拟环境位于：

```text
/Users/gu/Documents/telegram-turbo-downloader/.venv
```

配置文件位于：

```text
/Users/gu/Documents/telegram-turbo-downloader/.env
```

登录会话位于：

```text
/Users/gu/Documents/telegram-turbo-downloader/data/yhxm/session.session
```

当前账户标签已经配置为：

```text
DOWNLOAD_ACCOUNT=yhxm
```

`.env` 中包含 Telegram API 凭据和账户配置，不应上传、分享或提交到 Git 仓库。

## 3. 启动前准备

### 3.1 开启 VPN 或代理

Telegram 在部分地区无法直连。启动程序前先开启可用的 VPN 或代理，并确认系统网络能够访问 Telegram。

如果没有开启代理，可能出现：

```text
PermissionError: [Errno 1] Operation not permitted
Connection to Telegram failed
```

### 3.2 打开终端

在 macOS 中打开“终端”，进入程序目录：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
```

## 4. 启动程序

登录状态有效时，直接运行：

```bash
.venv/bin/ttd
```

也可以使用完整命令：

```bash
.venv/bin/telegram-turbo-downloader
```

启动并连接成功后，顶部会显示类似：

```text
connected · yhxm · DC5 · jobs 5
```

各部分的含义：

- `connected`：已经连接到 Telegram
- `yhxm`：当前登录的账户标签
- `DC5`：当前使用的 Telegram 数据中心
- `jobs 5`：连接池大小为 5

## 5. 重新登录

如果程序提示 session 缺失、失效或需要重新登录：

```bash
.venv/bin/ttd-login
```

完整命令：

```bash
.venv/bin/telegram-turbo-downloader-login
```

登录时：

1. 账户标签直接按回车，默认会使用 `.env` 中配置的 `yhxm`
2. 输入包含国家码的 Telegram 手机号，例如 `+86138...`
3. 输入 Telegram 发来的验证码
4. 如果开启了二步验证，再输入二步验证密码
5. 看到 `LOGIN SUCCESSFUL` 即表示成功

登录成功后，验证码和密码不需要再次输入，程序会自动复用 session。

如果登录时使用了其他账户标签，需要同步修改 `.env`：

```dotenv
DOWNLOAD_ACCOUNT=新的账户标签
```

## 6. 下载频道中的文件

启动程序后：

1. 按 `o` 打开频道或机器人
2. 输入频道用户名、机器人用户名或频道 ID
3. 按回车

支持的输入形式：

```text
@channelname
@SearchBot
-1001234567890
```

程序会读取该聊天最近的、包含文件的消息。当前版本大约会加载最近 200 条消息中的文件。

## 7. 下载收藏夹中的文件

“收藏夹”在 Telegram 内部称为 **Saved Messages**。

操作步骤：

1. 在程序主界面按 `o`
2. 输入：

```text
me
```

3. 按回车
4. 等待文件列表加载
5. 按 `/` 或 `f` 搜索文件名
6. 使用上下方向键选择文件
7. 按空格给文件打勾
8. 按 `d` 开始下载

例如可以搜索：

```text
命运石之门
```

或：

```text
5pb 001
```

如果较旧的收藏文件没有显示，可以回到 Telegram，把目标文件重新转发到收藏夹，然后在程序中按 `r` 刷新。

## 8. 搜索和选择文件

| 操作 | 按键 |
|---|---|
| 进入频道/机器人输入框 | `o` |
| 进入文件名搜索框 | `/` 或 `f` |
| 返回文件列表 | `Esc` |
| 上下移动光标 | `↑` / `↓` |
| 选中或取消当前文件 | `Space` |
| 选中当前列表中全部文件 | `A` 或 `a` |
| 清除当前选择 | `N` 或 `n` |
| 开始下载已选文件 | `D` 或 `d` |
| 刷新当前聊天文件列表 | `R` 或 `r` |
| 退出程序 | `Q` 或 `q` |

建议先输入搜索词缩小列表，再按 `A` 全选，避免误选无关文件。

## 9. 下载界面

开始下载后，界面会显示：

```text
downloading 1 · 1 queued
```

这表示：

- 当前只有一个文件处于下载状态
- 其他文件正在排队

程序不会同时下载多个大文件。它会先集中下载当前文件，再继续队列中的下一个文件。

状态行可能类似：

```text
8.6%  265.0 MB/3.00 GB  4.20 MB/s  ETA 00:11  · 5w
```

其中：

- `8.6%`：当前文件进度
- `265.0 MB/3.00 GB`：已下载大小和总大小
- `4.20 MB/s`：当前速度
- `ETA`：预计剩余时间
- `5w`：当前文件正在使用 5 个下载 worker

`0.00 MB/s` 可能只是瞬时采样没有捕捉到刚完成的分块，并不一定表示下载停止。应观察至少 20～30 秒。

### 下载控制

| 操作 | 按键 |
|---|---|
| 上下选择下载项 | `j` / `k` 或 `↑` / `↓` |
| 暂停或继续 | `p` |
| 停止当前文件 | `s` |
| 停止全部文件 | `x` |
| 失败后重试 | `Enter` |
| 清除已完成记录 | `c` |
| 增加连接数 | `+` |
| 减少连接数 | `-` |
| 返回文件列表 | `b` |
| 退出程序 | `q` |

## 10. 多连接和速度

### `5w` 是什么

`5w` 表示当前文件正在使用 5 个并发 worker 下载不同分块，不是单线程下载。

连接数可以从下载界面直接调整：

- 按 `+`：增加 1 个连接
- 按 `-`：减少 1 个连接

也可以启动前通过环境变量设置：

```bash
TTD_JOBS=6 .venv/bin/ttd
```

建议值：

- 普通免费账户：`5`～`6`
- 网络不稳定：`3`～`5`
- 不建议超过 `8`

Telegram 的速度限制通常是按账号计算，而不是单纯按连接数计算。增加连接不一定会线性提速，过高还可能触发限流、连接中断或失败。

### 实际速度受什么影响

- Telegram 免费账户限速
- VPN 或代理节点的带宽与延迟
- 文件所在数据中心与当前账户数据中心之间的跨 DC 传输
- 国际线路质量
- 频道资源服务器和账号当前的限流状态
- 本地 Wi-Fi 或宽带速度

## 11. 查看下载日志

如果速度长期为 0，可以另开一个终端窗口运行：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
tail -f logs/app.log | rg '\[WORKER-|FLOOD|ERROR'
```

正常的并行下载日志会出现多个 worker，例如：

```text
[WORKER-0] starting download
[WORKER-1] starting download
[WORKER-2] starting download
[WORKER-3] starting download
[WORKER-4] starting download
```

以及：

```text
[WORKER-2][PART-457] [OK] Success
```

如果看到多个 `WORKER` 编号交替出现，说明多连接下载工作正常。

## 12. 下载文件保存位置

默认保存目录：

```text
~/Downloads
```

程序会尝试自动分类，例如：

| 文件名 | 保存位置 |
|---|---|
| `Show.S01E01...` | `~/Downloads/Show/S01/` |
| `Movie.2024...` | `~/Downloads/Movie/` |
| 无法识别的名称 | `~/Downloads/` |

## 13. 分卷压缩包

常见文件名：

```text
资源.7z.001
资源.7z.002
资源.7z.003
资源.7z.004
资源.7z.005
```

必须下载全部分卷，并把它们放在同一个文件夹中。

解压时只需要打开：

```text
资源.7z.001
```

不要单独解压 `.002`、`.003` 等文件。

macOS 自带“归档实用工具”可能无法处理这种分卷格式，可以安装 Keka 或 7-Zip。

## 14. 断点续传

如果下载中断：

1. 重新启动程序
2. 按 `o` 重新打开原频道或输入 `me`
3. 找到同一个文件
4. 重新选中并按 `d`

程序会扫描 `.part` 文件，并只下载尚未完成的分块。

不要手动删除 `.part` 文件，否则已下载的部分会丢失。

## 15. 常见问题

### 15.1 提示登录缺失或 session 失效

运行：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
.venv/bin/ttd-login
```

### 15.2 无法连接 Telegram

先检查 VPN 或代理是否开启，并确认其他 Telegram 客户端可以正常联网。

### 15.3 输入 `me` 后没有目标文件

程序只列出最近的、带文件的消息。可以把旧文件重新转发到收藏夹，再按 `r` 刷新。

### 15.4 只能看到机器人消息，没有文件

程序不会替你向搜索机器人发送查询。需要先在 Telegram 客户端中向机器人发送搜索内容，等机器人回复文件后，再回到本程序打开同一个机器人。

### 15.5 速度显示为 0

先等待 20～30 秒，并观察进度和日志。若多个 `WORKER` 仍在成功下载，通常只是瞬时速度显示问题。

若日志长时间没有任何 `[OK] Success`：

1. 按 `p` 暂停，再按 `p` 继续
2. 将连接数降到 `3`～`5`
3. 更换 VPN 节点
4. 重启程序并重新开始同一文件

### 15.6 下载速度没有明显提升

这是常见现象。Telegram 会按账号限速，`5` 个连接通常已经接近免费账户的合理上限。先从 VPN 线路和实际网络带宽排查，不要盲目把连接数调到很高。

## 16. 安全注意事项

- `.env`、`session.session` 都相当于账号敏感信息，不要分享
- 不要把整个 `data` 目录上传到网盘或 Git 仓库
- 只从可信频道下载文件
- 不运行来源不明的 `.exe`、脚本或 macOS 应用
- 下载完成后可用系统安全软件扫描大型压缩包
- 遵守 Telegram 服务条款，不要批量滥用或高频抓取

## 17. 快速命令

启动：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
.venv/bin/ttd
```

重新登录：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
.venv/bin/ttd-login
```

使用 6 个下载 worker 启动：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
TTD_JOBS=6 .venv/bin/ttd
```

查看下载日志：

```bash
cd "/Users/gu/Documents/telegram-turbo-downloader"
tail -f logs/app.log | rg '\[WORKER-|FLOOD|ERROR'
```
