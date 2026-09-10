# LLM 学习笔记：Tiny Llama-2 作业实践

> 整理自 CISC 7021 Assignment 1 实践过程
> 涵盖：环境配置、模型生成、解码策略、困惑度评估、持续预训练

---

## 一、基础概念

### 1.1 基线（Baseline）

**定义**：一个最基础、最简单的可运行版本，作为后续所有改进和实验的参照点。

**作用**：
- 确认环境、数据、模型本身没有问题
- 后续改进效果的好坏，都要和基线对比才能判断

**本作业的基线预检标准**：

| 检查项 | 预期结果 |
|--------|----------|
| 模型参数量 | 41.69 M |
| 生成文本 | 通顺英文 |
| 迷你 PPL | ~10 |

---

### 1.2 挂载（Mount）

**定义**：把一个存储设备（硬盘、U 盘、云盘）接入到文件系统的某个目录下，让它成为系统的一部分。

**类比**：把 U 盘插到电脑 USB 接口，文件资源管理器里出现新的盘符。

**在 Colab 中的含义**：把 Google Drive 映射到 Colab 虚拟机的 `/content/drive` 路径下。

**代码**：
```python
from google.colab import drive
drive.mount('/content/drive')
```

**注意**：
- 每次打开新的 Colab 笔记本都要重新挂载
- 挂载成功后，文件路径为 `/content/drive/MyDrive/...`
- 常见错误：`credential propagation was unsuccessful` → 刷新页面 / 用 `force_remount=True` / 无痕模式

---

### 1.3 分词器（Tokenizer）

**定义**：把人类能读的**文本** ↔ 模型能读的**数字（token ID）**互相转换的工具。

```
"Once upon a time"  --tokenizer-->  [128, 3321, 440, 259]
       (文本)                            (token ID 序列)
```

**为什么需要它**：神经网络只能处理数字，不能直接吃字符串。所以要有一步"编码"，把文本切成 **token**（词/子词片段），再查表映射成整数 ID。

**关键点**：

| 概念 | 英文 | 含义 |
|------|------|------|
| 词元 | Token | 模型的最小处理单位，不一定是"一个词" |
| 词表 | Vocabulary | 所有 token 的集合，Llama 约 32000 个 |
| 编码 | encode | 文本 → token ID（模型输入方向） |
| 解码 | decode | token ID → 文本（模型输出方向） |
| 特殊 token | Special Token | 有专门用途的 token，如 `<s>`（句首）、`</s>`（句尾）、`<pad>`（填充） |

**例子**（Llama 的分词方式）：
- `"playing"` 可能被切成 `play` + `ing`（两个 token）
- `"cat"` 是 1 个 token
- 中文常常一个字 1~2 个 token，所以中文对英文模型来说"很贵、很陌生"

> 💡 这正是本作业**英文模型中文 PPL = 70030** 的直接原因。

**对应代码**（见 2.1 节）：
```python
tokenized_input = tokenizer.encode(prompt, return_tensors='pt').to(device)  # 编码
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)     # 解码
```

---

### 1.4 批大小（batch_size）

**定义**：一次同时喂给模型多少条数据。

```
batch_size = 1  →  [样本1]                        一次处理 1 条
batch_size = 4  →  [样本1, 样本2, 样本3, 样本4]     一次处理 4 条
```

| | batch_size 大 | batch_size 小 |
|--|--------------|--------------|
| 速度 | 更快（GPU 并行利用率高） | 慢 |
| 显存 | 占用大 | 占用小 |
| 训练稳定性 | 梯度更平滑、更稳 | 噪声大，震荡 |

> 💡 本作业报错表里的 `CUDA out of memory → 减小 batch_size` 就是从这来的。

---

### 1.5 为什么批处理会牵扯出 pad_token？

**批处理要求**：一个 batch 里的所有样本必须**长度一致**，才能拼成一个方正矩阵送进 GPU。但真实句子长短不一：

```
样本1: [128, 3321, 440, 259, 88, 12]       长度 6
样本2: [128, 3321, 440]                    长度 3  ← 太短
```

**解决办法 = 填充（Padding）**：把短的用 `<pad>` 补到一样长。

```
样本2: [128, 3321, 440, PAD, PAD, PAD]     补齐到 6
```

**问题来了**：Llama 的 tokenizer **默认没有 `pad_token`**（因为它常被单条推理使用，不需要补）。所以代码里要手动给它指定一个：

```python
if tokenizer.pad_token is None and batch_size > 1:
    #        ①还没有pad_token     ②且确实要批处理（>1 才有补齐需求）
    existing_special_tokens = list(tokenizer.special_tokens_map_extended.values())
    #        ③取出模型已有的所有特殊 token，如 ['<s>', '</s>', '<unk>']
    assert len(existing_special_tokens) > 0, "..."
    #        ④确保至少有一个能拿来复用，否则直接报错
    tokenizer.add_special_tokens({"pad_token": existing_special_tokens[0]})
    #        ⑤把第一个特殊 token（通常是 '<s>'）复用为 pad_token
```

**逐句拆解**：

| 代码片段 | 作用 | 通俗解释 |
|----------|------|----------|
| `tokenizer.pad_token is None` | 检查有没有 pad token | "你没带填充符号？" |
| `batch_size > 1` | 只有批处理才需要填充 | 单条推理不用补，跳过 |
| `special_tokens_map_extended.values()` | 列出已有特殊 token | 看看手头有哪些现成符号 |
| `assert len(...) > 0` | 一个都没有就报错 | 防止复用空气 |
| `add_special_tokens(...)` | 把第一个复用为 pad | "那就把 `<s>` 拿来当填充符" |

**为什么要"复用已有的"**：给 Llama 新增 token 会改变词表大小，导致 embedding 层和原来预训练权重**不匹配**（需要 resize 并重新训练）。复用已有的 `<s>` 当 pad 是低成本的常见做法。

> ⚠️ 小提醒：用 `<s>`（句首符）当 pad 其实不太规范（模型可能误以为那是句首）。更干净的做法是用 `</s>`（句尾符），即 `tokenizer.pad_token = tokenizer.eos_token`。本作业的 `generate` 函数里 `pad_token_id=tokenizer.eos_token_id`（见 8.1 节）就是这么干的。

---

## 二、文本生成核心

### 2.1 model.generate() 三步骤

```python
# Step 1: 编码输入（文本 → token IDs）
tokenized_input = tokenizer.encode(prompt, return_tensors='pt').to(device)

# Step 2: 生成（核心）
output_ids = model.generate(
    tokenized_input,
    do_sample=True,
    max_new_tokens=300,
    temperature=0.6
)

# Step 3: 解码输出（token IDs → 文本）
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
```

---

### 2.2 关键参数详解

| 参数 | 含义 | 效果 |
|------|------|------|
| `max_new_tokens` | 最多生成的新 token 数（不含 prompt） | 控制输出长度 |
| `temperature` | 温度，调节下一个 token 的概率分布 | 高 → 更多样；低 → 更确定 |
| `do_sample` | 是否随机采样 | True=采样；False=贪婪解码 |
| `top_p` | 核采样，只从累积概率前 p 的词中采样 | 控制候选词范围 |
| `top_k` | 只从概率最高的 k 个词中采样 | 控制候选词数量 |
| `skip_special_tokens` | 解码时是否跳过特殊 token（如 `<s>`） | True → 输出更干净 |

**贪婪解码的特殊设置**：
```python
do_sample=False
temperature=None
top_p=None
top_k=None
```

---

### 2.3 Greedy vs Sampling

| | Greedy（贪婪解码） | Sampling（采样） |
|--|-------------------|------------------|
| 选词方式 | 每次都选概率最高的词 | 按概率分布随机抽签 |
| 结果 | 永远一样（确定） | 每次可能不同 |
| 风格 | 安全、保守、易重复 | 生动、多样、有惊喜 |
| 缺点 | 容易停在套话式结尾 | 偶尔可能语法不通顺 |
| 代码 | `do_sample=False` | `do_sample=True` |

**直觉理解**：
- Greedy = 考试只抄学霸的答案
- Sampling = 全班投票，谁都有机会被选上

---

### 2.4 温度（Temperature）的作用

| 温度值 | 效果 | 类比 |
|--------|------|------|
| 0.3 | 很保守，接近贪婪 | 只选最稳妥的词 |
| 0.8 | 平衡，既多样又不乱 | 适度冒险 |
| 1.2 | 很随机，有创造力但可能跑偏 | 大胆尝试 |
| 1.0 | 使用原始概率分布 | 不调整 |

---

## 三、困惑度（Perplexity, PPL）

### 3.1 定义

衡量语言模型预测样本的能力，**值越低越好**。

数学定义：
$$\text{Perplexity}(X) = \exp \left( -\frac{1}{t} \sum_{i=1}^t \log p_\theta (x_i | x_{<i}) \right)$$

**直观理解**：模型在每一步预测下一个词时的"困惑程度"。PPL=10 表示模型平均在 10 个词之间犹豫。

---

### 3.2 本作业的 PPL 结果

| 数据类型 | 基线模型 PPL | 持续预训练后 PPL |
|----------|-------------|------------------|
| 英文测试集 | 4.14 | — |
| 中文测试集 | 70030.42 | 3.52 |

**结论**：
- 英文模型对中文的 PPL 极高 → 说明它完全不懂中文
- 持续预训练后中文 PPL 大幅下降 → 模型学会了中文

---

## 四、持续预训练（Continual Pre-training）

### 4.1 概念

在已有基础模型上，用新语言/新领域的数据继续训练，使模型获得新能力。

**本作业**：用 10,000 条中文故事数据，让英文 Tiny Llama-2 学会中文。

---

### 4.2 关键训练超参数

| 参数 | 含义 | 本作业设置 |
|------|------|-----------|
| `learning_rate` | 初始学习率 | 1 e-4 |
| `num_train_epochs` | 训练轮数 | 8 |
| `per_device_train_batch_size` | 训练批大小 | 32 |
| `per_device_eval_batch_size` | 评估批大小 | 16 |
| `save_steps` | 每多少步保存 | 200 |
| `evaluation_strategy` | 评估策略 | "steps" |
| `weight_decay` | 权重衰减 | 0.01 |
| `warmup_ratio` | 预热比例 | 0.01 |
| `lr_scheduler_type` | 学习率调度器 | "linear" |
| `optim` | 优化器 | "adamw_torch" |

---

### 4.3 训练结果解读

| Step | Training Loss | Validation Loss |
|------|--------------|-----------------|
| 200 | 3.2983 | 3.2439 |
| 1000 | 1.3137 | 1.3720 |
| 2000 | 1.1067 | 1.2627 |

**观察**：
- Loss 持续下降 → 模型在学习
- Validation Loss 略高于 Training Loss → 轻微过拟合，但在可接受范围
- 最终中文 PPL 从 70030 降到 3.52 → 效果显著

---

## 五、Colab 环境操作

### 5.1 每次重新打开需要做的事

| 项目 | 是否需要重做 | 原因 |
|------|-------------|------|
| 挂载 Google Drive | ✅ 需要 | 虚拟机重置 |
| 运行所有代码单元格 | ✅ 需要 | 内存变量丢失 |
| 安装依赖包 | ✅ 需要 | 新虚拟机无包 |
| 上传 zip 文件 | ❌ 不需要 | 存在 Drive 里 |
| 解压到 Drive 的文件 | ❌ 不需要 | 持久存储 |
| 训练好的 checkpoint | ❌ 不需要（如果在 Drive） | 持久存储 |

---

### 5.2 重要提醒：保存训练结果

Colab 的 `/content/` 是**临时目录**，关闭即丢失。训练好的模型必须保存到 Drive：

```python
import shutil
shutil.copytree(
    "/content/llama-42m-zh-fairytales",
    "/content/drive/MyDrive/assignment1/llama-42m-zh-fairytales"
)
```

下次直接从 Drive 加载：
```python
new_model_path = "/content/drive/MyDrive/assignment1/llama-42m-zh-fairytales/checkpoint-2000"
model = LlamaForCausalLM.from_pretrained(new_model_path).to(device)
```

---

### 5.3 解压 zip 文件

```python
# 方法一：命令行
!unzip -q "/content/drive/MyDrive/assignment1/Model and Datasets.zip" -d "/content/drive/MyDrive/assignment1/"

# 方法二：Python
import zipfile
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
```

---

## 六、常见报错与解决

| 报错 | 原因 | 解决方法 |
|------|------|----------|
| `credential propagation was unsuccessful` | 挂载授权失败 | 刷新页面 / `force_remount=True` / 无痕模式 |
| `NameError: name 'generate' is not defined` | 函数未定义或未运行定义单元格 | 先运行定义 `generate` 的单元格 |
| `NameError: name 'text_stats' is not defined` | 同上 | 先运行定义 `text_stats` 的单元格 |
| `No such file or directory` | 路径错误 | 检查路径大小写、确认文件存在 |
| `CUDA out of memory` | 显存不足 | 减小 batch_size |

---

## 七、实验设计要点

### 7.1 Task 1 实验矩阵

**3 个 Prompt × 4 种解码配置 = 12 次生成**

```python
PROMPTS = [
    "Once upon a time, there was a little girl named Lily who loved to explore.",
    "Tom is a cute kitty who lives with a kind old lady.",
    "Max found a magic door in his bedroom one morning.",
]

CONFIGS = [
    dict(name="greedy",   do_sample=False, temperature=None, top_p=None, top_k=None),
    dict(name="temp=0.3", do_sample=True,  temperature=0.3, top_p=1.0, top_k=0),
    dict(name="temp=0.8", do_sample=True,  temperature=0.8, top_p=0.9, top_k=0),
    dict(name="temp=1.2", do_sample=True,  temperature=1.2, top_p=1.0, top_k=0),
]
```

---

### 7.2 评估指标

| 指标 | 含义 | 计算方式 |
|------|------|----------|
| 词数（words） | 生成文本长度 | 按空格分词计数 |
| 句数（sents） | 句子数量 | 按句号等标点切分 |
| TTR | Type-Token Ratio，词汇丰富度 | 不同词数 / 总词数 |
| PPL | 困惑度 | 模型对文本的预测难度 |

**TTR 越高** → 用词越多样、越不重复。

---

## 八、核心代码模板

### 8.1 封装 generate 函数

```python
import torch

def generate(prompt, seed=None, do_sample=False, temperature=None, 
             top_p=None, top_k=None, max_new_tokens=200):
    if seed is not None:
        torch.manual_seed(seed)
    
    inputs = tokenizer.encode(prompt, return_tensors='pt').to(device)
    
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            pad_token_id=tokenizer.eos_token_id,
        )
    
    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    stopped = len(outputs[0]) >= inputs.shape[1] + max_new_tokens
    return full_text, stopped
```

---

### 8.2 文本统计函数

```python
def text_stats(text):
    words = text.split()
    sents = [s for s in text.split('.') if s.strip()]
    n_words = len(words)
    n_sents = len(sents)
    ttr = len(set(words)) / n_words if n_words > 0 else 0
    return {"n_words": n_words, "n_sents": n_sents, "ttr": ttr}
```

---

### 8.3 PPL 评估调用

```python
from datasets import load_dataset

test_dataset = load_dataset('json', data_files={'test': data_file})["test"]["text"]
results = compute_ppl(model=model, tokenizer=tokenizer, device=device, 
                      inputs=test_dataset, batch_size=16)
print(f"Perplexity: {results['mean_perplexity']:.2f}")
```

---

## 九、关键结论

1. **英文模型不懂中文**：中文 PPL 高达 70030，说明模型对中文完全无法预测
2. **持续预训练有效**：10,000 条中文数据 + 8 epoch 训练，中文 PPL 降到 3.52
3. **温度影响明显**：温度越高，文本越长、TTR 越高、越多样，但也越容易跑偏
4. **Greedy 最安全但最无聊**：容易重复、容易停在套话式结尾
5. **小模型能力有限**：42 M 参数模型只能生成短篇简单故事，复杂任务力不从心

---

## 十、术语速查表

| 术语 | 英文 | 含义 |
|------|------|------|
| 基线 | Baseline | 基础参照版本 |
| 挂载 | Mount | 把存储设备接入文件系统 |
| 贪婪解码 | Greedy Decoding | 每步选概率最高的词 |
| 采样 | Sampling | 按概率分布随机选词 |
| 温度 | Temperature | 控制随机性的参数 |
| 核采样 | Top-p Sampling | 从累积概率前 p 的词中采样 |
| 困惑度 | Perplexity (PPL) | 模型预测文本的难度 |
| 持续预训练 | Continual Pre-training | 在已有模型上继续训练 |
| 词汇丰富度 | Type-Token Ratio (TTR) | 不同词数/总词数 |
| 特殊 token | Special Token | 如 `<s>`、`</s>`、`<pad>` |
| 分词器 | Tokenizer | 文本 ↔ token ID 的转换器 |
| 词元 | Token | 模型处理的最小文本单位（词或子词） |
| 词表 | Vocabulary | 所有 token 的集合 |
| 批大小 | batch_size | 一次喂给模型的数据条数 |
| 填充 | Padding | 把短样本补齐到统一长度 |
| 填充 token | pad_token | 用于补齐的占位 token |

---

> 📝 笔记整理完毕，可直接导入 Obsidian。
> 建议标签：`#LLM` `#NLP` `#Colab` `#TinyLlama` `#作业笔记`