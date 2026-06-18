
# 一、Jupyter notebook 打开方式
## 方式一：Terminal 打开
~~~bash
conda activate base  # 打开bash环境
~~~
~~~bash
jupyter notebook   # 打开jupyter notebook
~~~
### 💡 小技巧：指定 Jupyter 的工作目录

- **方法一（推荐）**：先在终端里 `cd` 到你想作为根文件夹的目录，再执行 `jupyter notebook`。
    ~~~bash
    
    cd /Users/你的用户名/我的数据科学项目
    jupyter notebook
    ~~~
	 Jupyter 就会以这个文件夹作为根目录。
## （略）方式二：Anaconda navigate 打开

# 二、base环境
当你安装好 Anaconda（或 Miniconda）后，系统自动创建的那个默认环境就叫 **base**
- 它是 conda 的“主环境”，也是你打开终端后默认激活的环境（你会看到命令行前面有个 `(base)` 标志）。
- ***base 里面已经预装了 Python 以及 Anaconda 自带的几百个常用库（numpy, pandas, matplotlib, jupyter 等）。***
- 如果你不创建任何新环境，你安装的所有包都会塞进 base 里。
    
**缺点**：如果你在做项目 A 时需要包版本 1.0，项目 B 需要包版本 2.0，两个版本冲突，base 环境无法同时满足 —— 这也是为什么需要创建独立环境的原因。
## base环境关闭自动激活
1. 避免干扰
2. 终端启动更快
3. 环境管理更清晰
4. 与macOS原生工具兼容
在terminal执行：
~~~bash
conda config --set auto_activate_base false
~~~
## 手动激活/退出
- **激活 base 环境**：`conda activate base`
- **退出当前 conda 环境**：`conda deactivate`
# 三、conda 环境（通常指“虚拟环境”）是什么？

**注意**：我们常说“conda 环境”，其实包括 base 环境 —— 因为它也是由 conda 管理的。但日常对话中，“conda 环境”往往特指你自己创建的 **非 base 的独立环境**。

## 四、base 环境 vs. 自己创建的 conda 环境：区别总结

| 维度       | base 环境                      | 自己创建的 conda 环境 (例如 myenv)             |
| -------- | ---------------------------- | ------------------------------------- |
| **创建方式** | 安装 Anaconda 后自动生成            | 手动 `conda create -n myenv python=3.x` |
| **是否必须** | 是，一定存在                       | 否，按需创建                                |
| **隔离性**  | ❌ 不隔离（所有项目共享包，容易冲突）          | ✅ 完全隔离（每个项目有自己的包）                     |
| **包数量**  | 很多（Anaconda 预装几百个）           | 极少（只有你主动安装的几个）                        |
| **磁盘占用** | 大（数 GB）                      | 小（几十到几百 MB，不含冗余）                      |
| **切换命令** | 默认激活，或 `conda activate base` | `conda activate myenv`                |
| **适用场景** | 日常随便试试、学习、不介意混乱              | 正式项目、需要特定版本、协作开发                      |


## 五、实际操作中的建议

1. **尽量别在 base 里乱装包**  
    把 base 当成“干净启动盘”，用来创建新环境和基本的 conda 管理。如果你已经在 base 里装了很多包，也没事，但建议从现在开始养成好习惯。
    
2. **每个项目建一个独立 conda 环境**  
    比如：
	~~~bash
	conda create -n data_science python=3.9  # 创建data_science 环境，-n、--name 表示给你创建的虚拟环境起个名字
	conda activate data_science
	conda install numpy pandas matplotlib jupyter
	~~~


