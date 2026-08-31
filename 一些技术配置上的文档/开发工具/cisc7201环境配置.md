# cisc7201 项目环境说明

> 独立 Python 环境安装与使用指南（2026-08-31）

---

## 一、环境概况

本机使用 **conda 创建独立环境 `cisc7201`**，与系统 base 环境完全隔离，用于运行 `cisc7201` 项目。

| 项目 | 内容 |
|---|---|
| 环境名称 | `cisc7201` |
| 环境路径 | `/opt/anaconda3/envs/cisc7201` |
| Python 版本 | **3.11.16**（满足 requires-python ≥ 3.10） |
| 包管理器 | pip（环境内统一管理，与 conda 账本无关，不污染 base） |

### 已安装依赖（全部满足 pyproject.toml 要求）

| 包 | 已装版本 | 要求 |
|---|---|---|
| ipykernel | 7.3.0 | ≥7.3.0 ✅ |
| jupyterlab | 4.6.3 | ≥4.6.3 ✅ |
| matplotlib | 3.11.1 | ≥3.10.9 ✅ |
| numpy | 2.4.6 | ≥2.2.6 ✅ |
| pandas | 3.0.5 | ≥2.3.3 ✅ |
| plotly | 7.0.0 | ≥7.0.0 ✅ |
| polars | 1.44.1 | ≥1.44.1 ✅ |
| requests | 2.34.2 | ≥2.34.2 ✅ |
| scikit-learn | 1.9.0 | ≥1.7.2 ✅ |
| scipy | 1.17.1 | ≥1.15.3 ✅ |
| seaborn | 0.13.2 | ≥0.13.2 ✅ |
| statsmodels | 0.15.0 | ≥0.15.0 ✅ |
| notebook | 7.6.2 | 补充安装（经典 Notebook 界面） |

> 以上均已通过「版本校验 + 导入测试 + kernel 实测」三重验证。

---

## 二、日常使用

### 1. 激活环境

```bash
# 若 conda 命令可用：
conda activate cisc7201

# 若提示 conda: command not found，先执行一次：
source /opt/anaconda3/bin/activate
conda activate cisc7201
```

### 2. 启动 Jupyter（两种界面任选）

```bash
jupyter lab        # 新版界面（功能更全，推荐）
jupyter notebook   # 经典界面
```

浏览器自动打开 `http://localhost:8888/lab`（或 `/tree`）。
新建 Notebook 时，内核选择 **「Python (cisc7201)」**。

> 内核已注册为系统级（`~/.jupyter/kernels/cisc7201`），该内核指向
> `/opt/anaconda3/envs/cisc7201/bin/python`，保证代码跑在独立环境里。

### 3. 直接运行 Python 脚本

```bash
conda activate cisc7201
python your_script.py
```

---

## 三、日常维护

### 安装新包（只装进本环境，不碰 base）

```bash
conda activate cisc7201
pip install 包名
```

### 查看环境内已装包及版本

```bash
conda activate cisc7201
pip list
```

### 删除环境（如需重建）

```bash
conda remove -n cisc7201 --all
```

---

## 四、为什么单独建环境？（背景说明）

- **conda 环境 = 仓库 + 账本**：conda 安装的包会登记依赖关系，保证环境自洽。
- **pip 覆盖 conda 包的问题**：用 pip 升级 conda 装的包，pip 只改文件、不改 conda 账本，
  导致账实不符；且部分包（如 scipy、scikit-learn）编译时链接了旧版 numpy 的二进制接口，
  pip 覆盖 numpy 后可能 ABI 不匹配，运行时崩溃。
- **base 是系统盘**：Anaconda base 被所有项目共用，搞坏影响面大。

因此本项目需要的都是较新版本（plotly≥7、polars≥1.44 等，Anaconda 仓库通常还没有），
最适合的做法就是**新建独立环境 + pip 管理**，坏了随时重建，互不影响。

---

## 五、常见问题排查

| 问题 | 解决方法 |
|---|---|
| `jupyter notebook` 报 Command not found | 该界面需要额外装 `notebook` 包：`pip install notebook` |
| 找不到「Python (cisc7201)」内核 | `python -m ipykernel install --user --name cisc7201 --display-name "Python (cisc7201)"` |
| 端口 8888 被占用 | `jupyter lab --port 8889` 换个端口 |
| 装了包但导入报错 | 确认已 `conda activate cisc7201`，且包是用环境内 pip 装的 |

---

## 六、快速自检命令

```bash
/opt/anaconda3/envs/cisc7201/bin/python - <<'EOF'
import importlib.metadata as md
for pkg in ["ipykernel","jupyterlab","matplotlib","numpy","pandas","plotly",
            "polars","requests","scikit-learn","scipy","seaborn","statsmodels","notebook"]:
    try:
        print(f"✅ {pkg:<14} {md.version(pkg)}")
    except Exception as e:
        print(f"❌ {pkg:<14} 未安装")
EOF
```

---

*记录：2026-08-31 安装并验证通过。*
