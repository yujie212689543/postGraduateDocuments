# 双版本只同步文件不同步设置
先别急，这个问题看起来像是 `.gitignore` 没起作用，但其实原因很简单：

> **`.gitignore` 只能忽略那些“从来没有被 Git 跟踪过”的新文件。**  
> 而你的 `workspace.json` 已经被 Git 纳入版本控制了，所以就算把它写进 `.gitignore`，Git 依然会盯着它的所有改动。

所以才会有“明明写了忽略，它还一直弹出来”的错觉 —— 不是没用，是你还差最后一步：**让 Git 彻底忘掉它**。

---

### 🛠️ 3 步一次性根治（在 GitHub Desktop 里就能做完）

#### 1. 打开终端

在 GitHub Desktop 顶部菜单，点击 **Repository → Open in Terminal**。  
这会直接打开一个终端窗口，并且路径已经自动在你的仓库。

#### 2. 让 Git 停止跟踪这两个文件

把下面两条命令**逐条复制进去，回车执行**：

~~~bash
git rm --cached .obsidian/workspace.json
~~~
执行完不会有太多提示，别怕，这只是在 Git 的记录里“删除”，你电脑上的原文件**完全不会丢**。

#### 3. 提交并推送

回到 GitHub Desktop，你会看到 Changes 里多出了两项删除记录。
- 填写提交信息（比如“停止跟踪 workspace 和测试文件”）
- 点击 **Commit to main**
- 再点击 **Push origin**

---

### 🍏 在另一台电脑上同步一下

之后你换到 Mac 或 Win 的另一台设备，打开 GitHub Desktop，点一下 **Fetch origin** 或 **Pull origin**。  
这样 Git 就会知道这两个文件不再被跟踪了，以后你在哪边打开 Obsidian，它们都不会再跳到 Changes 列表里来烦你。

---

### 💡 如果你想把整个 `.obsidian` 文件夹都忽略

也可以一步到位（连插件、设置文件都不跟踪）：

~~~bash
git rm --cached -r .obsidian
~~~
然后同样提交推送。你的 `.gitignore` 里保持一行：

~~~text
.obsidian/
~~~
就好了。
做完上面这几步，你的世界会立刻清净。试试看，两分钟就能搞定。

----
