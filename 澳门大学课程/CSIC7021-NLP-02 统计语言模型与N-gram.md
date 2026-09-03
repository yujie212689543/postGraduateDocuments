# CSIC7021 · 统计语言模型与 N-gram

> 课程：[[CSIC7021-Applied Natural Language Processing]] ｜ 上一篇：[[CSIC7021-NLP-01 词表示 - BOW缺陷与BPE子词模型]] ｜ 下一篇：[[CSIC7021-NLP-03 神经语言模型 - RNN与CNN与Transformer]]
> 内容来源：课堂随记「Unigram Model」「N-gram Models」及「传统 LM 三大问题」部分

---

## 0. 一句话主线

**语言模型（Language Model, LM）** = 给「一句话 / 一串词」打分，衡量它有多**像人话**；等价地，也可以看成「预测下一个最可能的词」。本页讲解最经典的统计做法 **N-gram 模型**。

---

## 1. 先看它有什么用：机器翻译里的「语感裁判」

![[Pasted image 20260901191652.png]]

> 例：把西语 *Que hambre tengo yo* 翻译成英语。逐词直译是 "What hunger have"（不通），人会说 **"I am so hungry"**。

机器怎么选？——给每个候选句子打分：

$$\hat{e} = \arg\max_{e} \ \underbrace{p(s \mid e)}_{\text{翻译模型：意思对不对}} \times \underbrace{p(e)}_{\text{语言模型：像不像人话}}$$

- **$p(e)$（语言模型）**：候选英语句子本身有多通顺。`I am so hungry` 常见 → 概率高；`What hunger have` 几乎没人说 → 概率≈0。
- **$p(s \mid e)$（翻译模型）**：这个英语句子对应原句（西语）的可能性有多大。

| 候选翻译 | 通顺度 | $p(e)$ | 结果 |
|---|---|---|---|
| I am so hungry ✅ | 地道 | 相对高 | **胜出** |
| What hunger have ❌ | 直译、不通 | 极低 | 淘汰 |
| Hungry I am so ❌ | 语序怪 | 低 | 淘汰 |
| Have I that hungry ❌ | 语法错 | 低 | 淘汰 |

同样的思路也用于**拼写纠正**：把 "heva" 改成 "have"，就是比较「哪种原词 $e$ 使 $p(\text{上下文} \mid e) \times p(e)$ 最大」。

> **结论**：翻译软件不是「查字典直译」，而是**从一堆候选中挑出最像人话的一句**。

---

## 2. 语言模型的数学定义

一句话 $w_1 w_2 \dots w_n$ 的概率，用**链式法则**展开：

$$P(w_1 \dots w_n) = \prod_i P(w_i \mid w_1 \dots w_{i-1})$$

但「依赖前面所有词」太奢侈，于是引入 **Markov 假设**：当前词只依赖最近 $N-1$ 个词。

| 模型 | 公式 | 依赖前几个词 |
|---|---|---|
| **Unigram** (1-gram) | $P(w_i)$ | 0（每个词独立） |
| **Bigram** (2-gram) | $P(w_i \mid w_{i-1})$ | 1 |
| **Trigram** (3-gram) | $P(w_i \mid w_{i-2},\, w_{i-1})$ | 2 |
| **N-gram** | $P(w_i \mid w_{i-N+1} \dots w_{i-1})$ | $N-1$ |

参数用**数数（MLE 最大似然）**估计：

$$P(w_i \mid w_{i-1}) = \frac{\text{count}(w_{i-1}, w_i)}{\text{count}(w_{i-1})}$$

### 举例

句子：*I love natural language processing*

- **Unigram**：`love` 的出现与谁都不相关；
- **Bigram**：$P(\text{love}\mid\text{I})$、$P(\text{natural}\mid\text{love})$、$P(\text{language}\mid\text{natural})$ …；
- **Trigram**：$P(\text{natural}\mid\text{I love})$、$P(\text{language}\mid\text{love natural})$ …。

> N 越大，能利用的局部上下文越多，生成越通顺；但**参数越多、数据越稀疏**。

---

## 3. 致命伤：长距离依赖（Long-distance Dependencies）

> *"The computer which I had just put into the machine room on the fifth floor **crashed**."*

- 主语 `The computer` 和谓语 `crashed` 是**主谓呼应**的关系，但中间隔着长长的定语从句。
- 若用 **5-gram**，预测 `crashed` 时只能看到前 4 个词 `floor on the fifth`，**根本看不到**开头的 `The computer` → 无法判断主语单复数，也抓不住语义联系。
- 结论：**N-gram 的窗口是固定的，管不了「隔很远才呼应」的词。**

---

## 4. 但现实里常常「够用」（get away with）

习语 *get away with* = **勉强应付过去 / 凑合着用也能行**。

| 优点 | 说明 |
|---|---|
| 简单高效 | 只「数数」，不需要神经网络 |
| 数据驱动 | 在大语料上学到的常见搭配很准 |
| 工程成熟 | 早期机器翻译、语音识别、拼写检查、输入法预测都在用 |
| 可作基线 | 现在也常作为深度模型的对比对象 / 后处理工具 |

**例子**：手机输入法预测下一个词，用 3-gram / 4-gram 就够——「你吃__」→ 饭 / 了 / 过，并不需要理解整句结构。

### N-gram vs 现代模型

| 特性 | N-gram | 理想 LM（如 Transformer） |
|---|---|---|
| 上下文长度 | 固定（$N-1$ 个词） | 可变，理论上无限（注意力机制） |
| 长距离依赖 | ❌ 不能 | ✅ 能 |
| 计算量 | 低 | 高 |
| 数据需求 | 少 | 海量 |
| 应用 | 轻量任务仍广泛使用 | 主流大模型的基础 |

---

## 5. 三个经典痛点 → 通往神经网络的引子

![[Pasted image 20260901202140.png]]

这张图是传统 LM（N-gram）的「体检报告」：三大痛点各有**历史补丁**，也预告了**神经网络的终极解法**。

### 痛点 ① 相似词之间无法共享经验
*Cannot share strength among similar words*

- **表现**：学过 `She bought a car`，不等于懂 `She bought a bicycle`；学过 `bought`，不等于懂 `purchased`。每个词都要单独学，**浪费数据**。
- **历史补丁**：**基于类别的语言模型（Class-based LM）**——把词归类：`car/bicycle → <交通工具>`、`bought/purchased → <购买>`。学会「`<购买>` + `<交通工具>`」就能举一反三。
- **终极解法**：**词嵌入**——每个词一个稠密向量，相似词向量相近，模型自动共享统计（见 [[CSIC7021-NLP-01 词表示 - BOW缺陷与BPE子词模型]]）。

### 痛点 ② 隔了词的上下文用不上
*Cannot condition on context with intervening words*

- **表现**：`She bought a blue car` vs `... a red car`；`like those movies` vs `like these movies`。中间形容词 / 指示代词一变，传统模型就当全新情况，学不会「结构其实相同」。
- **历史补丁**：**Skip-gram 语言模型**——允许「跳过」中间词，用隔开的上下文做预测。
- **终极解法**：神经网络用隐藏层把**所有上文词的向量揉在一起**，并不要求它们紧挨着。

### 痛点 ③ 长距离依赖
*Cannot handle long-distance dependencies*

- **表现**：`The house that they built on the hill has a stunning view.` —— `house` 与 `view` 语义相关，中间却隔了一长串。传统模型「记性差」，读到 `view` 时早忘了 `house`。
- **历史补丁**：**Cache（缓存近词）、Trigger、Topic（主题）、Syntactic（句法）** 等模型——本质是给模型「加记忆 / 加关注」。
- **终极解法**：**RNN（循环记忆）** 与 **Transformer（注意力让任意两词直接互连）** → [[CSIC7021-NLP-03 神经语言模型 - RNN与CNN与Transformer]]。

> **一句话总结**：这三张「病假条」，正是后来**深度学习取代 N-gram** 的根本原因。

---

## 6. 速查表

| 概念 | 一句话 |
|---|---|
| 语言模型 | 给词串打分 / 预测下一个词 |
| Noisy-channel MT | 选 $p(s\mid e)\cdot p(e)$ 最大的翻译 |
| Unigram / Bigram / Trigram | 分别看 0 / 1 / 2 个前词 |
| Markov 假设 | 只看最近 $N-1$ 个词 |
| N-gram 的伤 | 长距离依赖、数据稀疏、无法共享相似词 |
| 历史补丁 | 类别模型 / Skip-gram / Cache-Topic |
| 终极解法 | 神经网络（词嵌入 + RNN / 注意力） |

> 下一步：看看神经网络怎么彻底解决这些痛点 → [[CSIC7021-NLP-03 神经语言模型 - RNN与CNN与Transformer]]
