# CISC7021 · Chapter 1 Introduction（模块版笔记）

> 课程：[[CISC7021-Applied Natural Language Processing]] ｜ 相关主题：[[CISC7021-NLP-01 词表示 - BOW缺陷与BPE子词模型]]、[[CISC7021-NLP-02 统计语言模型与N-gram]]、[[CISC7021-NLP-03 神经语言模型 - RNN与CNN与Transformer]]、[[CISC7021-NLP-04 文本生成 - 温度与采样策略]]
> 来源：课件 `Chapter 1 - Introduction.pdf`（P1–P75）｜ 场景：随堂测验复习（30 分钟、全选择题）
> 用法：每个模块 = 一块知识点 → 立刻做后面的 5–10 道题 → 对答案。术语统一写成 **English（中文）**，带 ★ 的是高频考点。

| 1 | 自然语言与语言的四大特性 | P12–14 |
| 2 | NLP 是什么：定义、四大用途、典型任务 | P15–24 |
| 3 | 语言六大层次 ★ | P25–37 |
| 4 | 自然语言理解 NLU 的流程 | P38 |
| 5 | NLP 难在哪：歧义与世界知识 | P39–41 |
| 6 | NLP 发展史 | P43 |
| 7 | 通用框架 `Y = f(X)` 与开发循环 | P44–45 |
| 8 | 三种建系统的方法 + 数据需求 | P46–47 |
| 9 | 情感分类器完整案例 ★ | P48–58 |
| 10 | 改进循环 + 五类难点案例 | P58–64 |
| 11 | 机器学习、BOW 与结构化感知机 ★ | P65–70 |
| 12 | 神经网络 + 课程大纲 | P71–73 |

---

## 模块 1：自然语言与语言的四大特性（P12–14）

### 1.1 定义

- **Natural language（自然语言）** = 人类语言，如中文、英文。
- 与之相对的是：
  - **constructed language（人造语言 / 构造语言）**，如世界语
  - **artificial language（人工语言）**
  - **machine language（机器语言）**
  - **language of formal logic（形式逻辑语言）**
- 自然语言也称为 **ordinary language（日常语言）**。

### 1.2 所有自然语言共有的四个特性（高频考点）

| 特性 | 英文 | 含义 |
|---|---|---|
| 语言系统性 | **Language Systematics** | 语言系统性地包含 **phonology（音系）**、**graphics（文字书写，通常有）**、**morphology（形态）**、**syntax（句法）**、**lexicon（词汇）**、**semantics（语义）** |
| 约定俗成且任意性 | **Conventional and Arbitrary** | 某个词被指派给某个事物或概念，本身没有必然理据（arbitrary = 任意的） |
| 冗余性 | **Redundancy** | 信息常常以不止一种方式被表达（signaled in more than one way） |
| 语言演变 | **Language Evolution** | 所有自然语言都因各种因素而发生变化 |

> 记忆口诀：**系统性、任意性、冗余性、演变性**。

---


### 模块 1 练习（8 题）

1. Which term refers to a language such as Chinese or English, as opposed to a constructed or machine language? A. formal language B. natural language C. artificial language D. programming language
2. According to the lecture, natural language is also called: A. ordinary language B. formal language C. machine language D. logical language
3. All of the following are properties shared by ALL natural languages EXCEPT: A. systematics B. conventional and arbitrary mapping C. redundancy D. a fixed and unchanging vocabulary
4. "A particular word is assigned to a specific thing or concept without inherent reason" describes: A. redundancy B. language evolution C. conventional and arbitrary D. language systematics
5. Which best illustrates redundancy in language? A. "bank" can mean a river bank or a financial institution B. In English, plurality is marked both by the numeral and by the noun ending ("two book-s") C. New words such as "selfie" enter the language D. Chinese and English use different words for water
6. Which of the following is NOT listed as part of the language system in the lecture? A. phonology B. graphics C. lexicon D. discourse
7. Which statement about language evolution is correct? A. Natural languages never change B. Only constructed languages change C. All natural languages undergo change due to various factors D. Only written languages change
8. A student argues: "Since word-meaning pairs are arbitrary, we can rename anything we want at any time." Which aspect does this ignore? A. language systematics B. the "conventional" part — the pairing is fixed by agreement within a speech community C. redundancy D. graphics

### 模块 1 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **A** | **D** | **C** | **B** | **D** | **C** | **B** |

---

## 模块 2：NLP 是什么：定义、四大用途、典型任务（P15–24）

### 2.1 定义

**NLP（Natural Language Processing，自然语言处理）** = **computers using natural language as input and/or output**（计算机把自然语言作为输入和/或输出）。

### 2.2 NLP 的四个用途（P16，必背）

1. **Handle Human Language Using Computers**（用计算机处理人类语言：文本与语音）
2. **Aid Human-machine Communication**（辅助人机交流：Q&A 问答、Dialog 对话）
3. **Aid Human-human Communication**（辅助人际交流：Translation 翻译、Writing 写作）
4. **Analyze / Understand Language**（分析与理解语言：Lexical 词汇层、Syntax 句法层、Semantic 语义层）

### 2.3 典型任务术语

- **Speech Recognition（语音识别）**：语音 → 文本
- **Speech Synthesis（语音合成）**：文本 → 语音
- **Speech Translation（语音翻译）**：语音 → 另一种语言的语音
- **Text Translation / Machine Translation（文本翻译 / 机器翻译）**
- **Generation（文本生成）**
- **Understanding（语言理解）**
- **Question Answering / Q&A（问答）**
- **Dialog（对话）**

### 2.4 NLP 能答什么、不能答什么（P17–18）

- **能答**：How many people live in the Macao SAR? → 给出约 680,000 的估计（并提示应以官方统计为准）。
- **不能答**：How many MEDALS will be awarded at Los Angeles 2028? → 未来事件，数据不存在，模型只能含糊其辞。
- 启示：语言模型的知识来自训练数据，**没有依据时会含糊、编造**，这属于 **hallucination（幻觉）** 问题。

### 2.5 机器翻译的注意点（P19–20）

- 官方新闻翻译示例（葡萄牙语 ↔ 中文，utran-i.com）。
- **ChatGPT translation cautions（ChatGPT 翻译的注意事项）**：
  - **Prompt translation may miss info (e.g., names)**（提示式翻译可能漏信息，例如人名）
  - 但 **in-context learning（上下文学习）** 能提升准确率
  - **ChatGPT may generate incorrect translations and fabricate information during multiple rounds of conversation**（多轮对话中可能译错并编造信息）

### 2.6 语言分析作为科学探究（Language Analysis: Scientific Inquiry，P21–23）

- **Computational social science（计算社会科学）**：given observational data（给定观测数据）来回答关于社会的问题。
- 例子（Sap et al., 2017）：电影的剧本中，女性与男性角色谁更有 **power or agency（权力或能动性）**？
- 分析手段：
  - **Semantic Roles（语义角色）**：句子标注为 person / agent / relation / role / ...
  - **AMR（Abstract Meaning Representation，抽象语义表示）**：一个等价的语义图（Song et al., 2019）。
- 现实打击：用 **Stanford CoreNLP（Manning et al., 2014）** 解析 UM News 的简单句子也会出错 → 说明 SOTA（state-of-the-art，最先进）系统在简单情形照样失败。

### 2.7 本课程要讨论的三个大问题（P24）

1. **What** makes the state-of-the-art NLP systems that work well at some tasks?（是什么让当前最先进系统在某些任务上表现良好？）
2. **Why and where** do current state-of-the-art NLP systems still fail?（它们为什么、在哪里仍然失败？）
3. **How** can we make appropriate improvements and achieve our objectives with NLP?（如何做出恰当的改进、达成目标？）

同时课件给出「数据规模 vs 成本」的对照：

| 资源 | Creation & Management（创建与管理成本） | Scale of Rules / Data（规则/数据规模） |
|---|---|---|
| Rules（规则） | Expensive（昂贵） | 10s（几十条） |
| Cases（案例/实例） | Moderate（中等） | 100s（几百条） |
| Parallel Data（平行语料） | Cheap（便宜） | Millions（百万级） |
| Monolingual Data（单语语料） | Cheap（便宜） | In 10Bs（百亿级） |

技术演进路径：**RBMT（规则机器翻译）→ EBMT（基于实例的机器翻译）→ SMT（统计机器翻译）→ NMT（神经机器翻译）→ Pre-training（预训练）**，时间跨度 1950 → 2020。红色曲线代表 **Trans. Quality（翻译质量）** 随单语数据规模快速上升。

---


### 模块 2 练习（9 题）

1. According to the lecture, NLP is defined as: A. computers using natural language as input and/or output B. the study of linguistic sound C. building formal logics D. translating programs into natural language
2. Which is an example of "Aid Human-machine Communication"? A. translation and writing B. lexical and syntactic analysis C. Q&A and dialog D. phonology and morphology
3. Which belongs to "Analyze/Understand Language" rather than aiding communication? A. dialog systems B. lexical and syntactic analysis C. machine translation D. question answering
4. The question "How many medals will be awarded at Los Angeles 2028?" is used to show that: A. NLP systems always answer correctly B. future events are easy for NLP C. the answer requires phonology D. the model may lack the required information and cannot give a reliable answer
5. Which is listed as a caution when using ChatGPT for translation? A. it may miss information such as names, and may fabricate information during multiple rounds of conversation B. it always misses all proper names C. it cannot translate Portuguese D. it refuses to translate news reports
6. The study by Sap et al. (2017) on movie scripts is an example of: A. speech recognition B. morphological analysis C. speech synthesis D. computational social science
7. Which representation is described as "an equivalent graph" of a sentence's meaning? A. AMR (Abstract Meaning Representation) B. POS tag C. parse tree D. syllable structure
8. According to the lecture's chart, the largest amount of data is available in the form of: A. rules (10s) B. cases (100s) C. parallel data (millions) D. monolingual data (in 10 billions)
9. The evolution path of machine translation methods shown in the lecture is: A. SMT → RBMT → NMT → EBMT B. NMT → SMT → RBMT C. RBMT → EBMT → SMT → NMT → Pre-training D. Pre-training → NMT → SMT → RBMT → EBMT

### 模块 2 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 答 | **A** | **C** | **B** | **D** | **A** | **D** | **A** | **D** | **C** |

---

## 模块 3：语言六大层次（P25–37）

### 3.0 六大层次总表（必须能背）

| 层次 | 英文 | 定义 |
|---|---|---|
| 音系学 | **Phonology** | Study of linguistic sound（研究语言的声音） |
| 形态学 | **Morphology** | Study of word components（研究词内部的组成成分） |
| 句法学 | **Syntax** | Study of words relationships（研究词与词之间的关系） |
| 语义学 | **Semantics** | Study of literal meaning（研究字面意义） |
| 语用学 | **Pragmatics** | Study of meanings-goals relationship（研究意义与目标/意图的关系） |
| 篇章语言学 | **Discourse** | Study of larger linguistic units（研究比单个句子更大的语言单位） |

> 易错点：**Semantics 是"字面意义"，Pragmatics 才是"意图/目的"**；**Syntax 是"词与词的结构关系"，不是意思**。

### 3.1 语音学与音系学（Phonetics & Phonology）（P27–31）

- **Phonetics（语音学）**：语言声音 **如何物理地形成**（how they physically formed）。
- **Phonology（音系学）**：**离散声音的系统** —— 语言的音节结构（systems of discrete sounds / syllable structure）。
- 例：disconnect 的音节切分 [dis-kə-ˈnekt]；**syllable（音节）**。
- 同音串歧义（homophone / 语音歧义）：
  - "It's easy to **recognize speech**."（很容易识别语音）
  - "It's easy to **wreck a nice beach**."（很容易毁掉一片美丽的海滩）
  - 两句话读音几乎相同 → 这就是语音识别难的原因。
- 中文绕口令《季姬擊雞記》（全篇同音）→ 说明**声调与同音字**让中文语音处理也极难。

### 3.2 形态学（Morphology）（P32）

- **Morphology（形态学）** = 研究词内部成分的意义。
- 结构示例：**prefix（前缀）+ stem（词干）+ suffix（后缀）**
  - **dis**connecting = dis-（"not"，否定前缀）+ connect（"to attach"，词干/词根）+ -ing（Tense，时态后缀）
- 土耳其语极端例子：**uygarlastiramadiklarimizdanmissinizcasina**
  = uygar + las + tir + ama + dik + lar + imiz + dan + mis + siniz + casina
  = "**(behaving) as if you are among those whom we could not civilize**"（表现得仿佛你属于我们无法教化的那群人之一）。
- 启示：**agglutinative language（黏着语）** 必须做形态分析，否则一个词会被当成完全没见过的词。

### 3.3 词汇歧义（Lexical Ambiguity）（P33）★

经典例句：**"I made her duck."**

| 解读 | 中文 | 歧义类型 | 具体说明 |
|---|---|---|---|
| I caused her to quickly lower her head/body | 我让她赶紧低头（躲闪） | **Lexical category ambiguity（词性歧义）** | "duck" 可以是 **N（名词）** 也可以是 **V（动词）** |
| I cooked waterfowl belonging to her | 我把她的鸭子煮了 | **Lexical category ambiguity（词性歧义）** | "her" 可以是 **possessive pronoun（所有格代词，"她的"）** 也可以是 **dative pronoun（与格代词，"为她/给她"）** |
| I made the (plaster) duck statue she owns | 我做了她拥有的那只（石膏）鸭子雕像 | **Lexical Semantics（词义/词汇语义）** | "make" 可以表示 **create（制造）** 也可以表示 **cook（烹饪）** |

> 归纳：**词性歧义（lexical category）** 看的是"这个词是名词还是动词"；**词义歧义（lexical semantics）** 看的是"这个词是哪个意思"。考试常在这两个词上设陷阱。

### 3.4 句法学（Syntax —— Grammatical Structure）（P34）

- 定义：**the study of structural relationships between words**（研究词与词之间的结构关系）。
- 用 **parse tree / syntax tree（句法树）** 表示结构，节点标签如：
  - **S（Sentence，句子）**、**NP（Noun Phrase，名词短语）**、**VP（Verb Phrase，动词短语）**、**SBAR（Subordinate Clause，从句）**、**CONJ（Conjunction，连词）**、**NNP（Proper Noun，专有名词）**
- 例句：*I know that you and Frank were planning to disconnect me.*
  - 结构歧义：`that` 从句到底修饰谁？→ **structural / syntactic ambiguity（结构歧义）**
- *I made her duck* 同样存在句法结构歧义。
- **Part-of-speech（POS，词性/词类）** 歧义是句法分析的主要难点之一。

### 3.5 语义学（Semantics）（P35）

- 定义：**the study of meaning of sentence**（研究句子的意义）。
- 例句：*I know that you and Frank were planning to disconnect me.*
  - **ACTION（动作）= disconnect**
  - **ACTOR（施事者）= you and Frank**
  - **OBJECT（受事者/对象）= me**
  - 这些叫 **thematic roles（题元角色）** / semantic roles（语义角色）。
- 相关术语：
  - **selectional restrictions（选择限制）**：动词对论元语义类别的限制（如"吃"要求宾语可食用）。
  - **logic / meaning representation（逻辑式 / 意义表示）**：如 `made(I, her(duck))`。

### 3.6 语用学（Pragmatics）（P36）

- 定义：**the study of the relationship of meaning to the goals and intentions of the speaker**（研究意义与说话人目标、意图之间的关系）。
- 核心两问：
  - **What should you conclude from the fact I said something?**（我说了这句话，你应该推断出什么？）
  - **How should you react?**（你该如何反应？）
- 例子：
  - **Quick! Fire!**（快！着火/开枪！）→ 你知道必须跑
  - **He's got a knife!**（他有刀！）→ 你不会去问刀有多锋利
  - **I said, 'Now!'**（我说的是"现在"！）→ 你知道是什么时候
- 关键：语用学关心的是 **utterance（话语）** 在语境中的言外之意。

### 3.7 篇章语言学（Discourse）（P37）

- 定义：**the study of linguistic units larger than a single utterance**（研究大于单个话语的语言单位）。
- 关注：
  - **the structure of conversations（对话的结构）**
  - **turn taking（话轮转换）**
  - **thread of meaning（意义主线/话题连续性）**
- 例子（《2001 太空漫游》HAL 对话）：
  - Dave: *Open the pod bay doors, Hal.*
  - HAL: *I'm sorry Dave, I'm afraid I can't do that.*
  - Dave: *What are you talking about, Hal?*
  - HAL: *I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen.*

---


### 模块 3 练习（10 题）

1. "The study of word components" refers to: A. phonology B. syntax C. morphology D. semantics
2. Which layer studies the relationship of meaning to the goals and intentions of the speaker? A. semantics B. syntax C. pragmatics D. discourse
3. In "I know that you and Frank were planning to disconnect me," analyzing ACTION / ACTOR / OBJECT belongs to: A. semantics B. syntax C. phonology D. discourse
4. In "I made her duck," the fact that "her" can be a possessive pronoun or a dative pronoun is an example of: A. lexical semantics B. lexical category ambiguity C. syntactic ambiguity D. no ambiguity
5. Which is the lecture's definition of phonology? A. the study of systems of discrete sounds and syllable structure B. the study of how sounds are physically formed C. the study of word components D. the study of literal meaning
6. The pair "It's easy to recognize speech." / "It's easy to wreck a nice beach." illustrates: A. morphological variation B. negation C. the need for world knowledge D. ambiguity at the sound level (homophony)
7. "Turn taking" and "thread of meaning" are studied at which level? A. syntax B. semantics C. pragmatics D. discourse
8. The Turkish word "uygarlastiramadiklarimizdanmissinizcasina" is used to show the need for: A. syntactic analysis B. speech recognition C. pragmatic reasoning D. morphological analysis
9. The difference between "I cooked waterfowl belonging to her" and "I made the (plaster) duck statue she owns" lies in: A. the lexical semantics of "make" B. the lexical category of "duck" C. the syntax of the sentence D. phonology
10. "He's got a knife!" — concluding that you should run rather than ask how sharp it is, is an example of: A. phonology B. morphology C. pragmatics D. syntax

### 模块 3 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **C** | **C** | **A** | **B** | **A** | **D** | **D** | **D** | **A** | **C** |

---

## 模块 4：自然语言理解 NLU 的流程（P38）

**Pipeline（流水线）逐级如下**：

1. **Spoken Input（语音输入）**
2. **Phonological / Morphological Analyzer（音系 / 形态分析器）** ← 用 **Phonological & Morphological Rules（音系与形态规则）**
3. 输出 **Sequence of Words（词序列）**
4. **Syntactic Analyzer（句法分析器）** ← 用 **Grammatical Knowledge（语法知识）**
5. 输出 **Syntactic Structure（句法结构）**，并确定 **Thematic Roles（题元角色）**
6. **Semantic Interpreter（语义解释器）** ← 用 **Semantic Knowledge（语义知识）** 与 **Selectional Restrictions（选择限制）**
7. 输出 **Logic（逻辑式）**
8. **Contextual Reasoner（语境推理器）** ← 用 **Pragmatic & World Knowledge（语用与世界知识）**
9. 输出 **Meaning Representation（意义表示）**，如 `made(I, her(duck))`

> 记忆要点：**每一步都需要不同的知识源**；越往后越依赖外部世界知识。

---


### 模块 4 练习（8 题）

1. Which NLU component converts the spoken input into a sequence of words? A. syntactic analyzer B. phonological/morphological analyzer C. semantic interpreter D. contextual reasoner
2. Which knowledge source does the syntactic analyzer use? A. grammatical knowledge B. semantic knowledge C. world knowledge D. selectional restrictions
3. Which component uses selectional restrictions? A. phonological analyzer B. syntactic analyzer C. semantic interpreter D. contextual reasoner
4. Which component uses pragmatic and world knowledge? A. phonological analyzer B. syntactic analyzer C. semantic interpreter D. contextual reasoner
5. The output of the semantic interpreter is: A. a sequence of words B. a syntactic structure C. logic D. speech
6. NLU differs from NLG in that NLU: A. maps language into a meaning representation B. generates text from meaning C. trains language models D. translates speech into text
7. In the pipeline, the representation `made(I, her(duck))` is produced by: A. the phonological analyzer B. the morphological analyzer C. the syntactic analyzer D. the contextual reasoner
8. Which statement about the pipeline is correct? A. every stage uses the same knowledge source B. each stage relies on a different knowledge source, and later stages need more world knowledge C. simple sentences need no analysis D. only written input is supported

### 模块 4 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **A** | **C** | **D** | **C** | **A** | **D** | **B** |

---

## 模块 5：NLP 难在哪：歧义与世界知识（P39–41）

### 5.1 歧义（Ambiguity）

- 天然语言在**所有层次**都存在歧义（ambiguities at all layers）。
- 课件原话：
  - Computational linguists are **obsessed with ambiguity**（计算语言学家对歧义痴迷）
  - Ambiguity is a **fundamental problem** of computational linguistics（歧义是计算语言学的根本问题）
  - **Resolving ambiguity is a crucial goal**（消解歧义是核心目标）
- 重要观点：**各层语言知识可以看作"消歧组件"（ambiguity-resolving components）**。
  - 词性歧义靠句法知识消解
  - 词义歧义靠语义知识消解
  - 指代、讽刺、隐喻靠语用与世界知识消解

### 5.2 世界知识（World Knowledge）

- **Definition（定义）**：what we know about the world and what we can assume our hearer knows about the world is intimately tied to our ability to use language（我们对世界的认知、以及我们假定听者知道什么，与语言使用能力紧密相连）。
- 例子：
  - *I took the cake from the plate and ate it.* → 指代消解需要知道"吃"的对象是蛋糕
  - **911 attack on America**（9·11 事件）
  - *Tiangong-1 and Shenzhou-8 rendezvous and docked in orbit* / 天宫一号与神舟八号交会对接
  - 我们去金沙 → **Let's go to the Sands casino**（"金沙"是赌场，不是"金沙江"）

---


### 模块 5 练习（8 题）

1. According to the lecture, what is a fundamental problem of computational linguistics? A. missing training data B. ambiguity C. slow hardware D. spelling errors
2. Each layer of language knowledge can be thought of as: A. an ambiguity-resolving component B. a translation rule C. a training set D. a speech signal
3. Which example is used in the lecture to show the need for world knowledge? A. disconnect [dis-kə-ˈnekt] B. uygarlastiramadiklarimizdanmissinizcasina C. "I took the cake from the plate and ate it." D. "I know that you and Frank were planning to disconnect me."
4. Rendering 我們去金沙 as "Let's go to the Sands casino" requires: A. morphological analysis B. phonology C. negation handling D. world knowledge
5. In "I made her duck," deciding whether "duck" is a noun or a verb mainly requires: A. discourse knowledge B. world knowledge C. phonetic knowledge D. syntactic knowledge
6. Which statement is correct according to the lecture? A. Ambiguity only appears at the semantic layer B. Ambiguity is a fundamental problem of computational linguistics C. World knowledge is not needed for language use D. Natural languages are unambiguous
7. The 911 attack and the Tiangong-1 / Shenzhou-8 docking examples illustrate: A. world knowledge B. morphological variation C. syllable structure D. language evolution
8. Resolving ambiguity in a sentence typically requires: A. looking only at the last word B. using knowledge at multiple layers C. increasing the speech rate D. translating into another language

### 模块 5 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **A** | **C** | **D** | **D** | **B** | **A** | **B** |

---

## 模块 6：NLP 发展史（P43）

| 阶段 | 时间 | 特征（原文） | 代表系统 |
|---|---|---|---|
| **Rule-Based（规则驱动）** | **1950–1990** | **Intent recognition based on keywords**（基于关键词的意图识别） | Georgetown-IBM（1954）、ELIZA（1965）、SHRDLU（1968） |
| **Statistics-Based（统计驱动）** | **1990–2010** | **Intent recognition based on syntax analysis**（基于句法分析的意图识别） | ALICE（1995）、IBM's Watson（2006） |
| **Deep Learning-Based（深度学习驱动）** | **2014–Now** | **Semantic Feature Extraction**（语义特征抽取） | Apple SIRI（2010）、Microsoft Cortana（2015）、OpenAI ChatGPT（2023） |

- 纵轴是 **Quality（质量）**，曲线随时代快速上升；三大阶段的底色分别是 **Rule-based → Statistical → Neural + Pre-training（神经+预训练）**。
- 补充术语：
  - **Rule-based system（规则系统）** = 人工编写规则
  - **Statistical model（统计模型）** = 从数据估计概率/权重
  - **Deep learning（深度学习）** = 多层神经网络
  - **Pre-training（预训练）** = 先在大规模语料上训练，再迁移

---


### 模块 6 练习（8 题）

1. The rule-based era of NLP is: A. 1950–1990 B. 1990–2010 C. 2014–now D. 2000–2010
2. Which era is characterized by "intent recognition based on syntax analysis"? A. rule-based B. statistics-based C. deep-learning-based D. none of the above
3. The deep-learning era is characterized by: A. hand-written rules B. keyword matching C. statistical machine translation D. semantic feature extraction
4. Which system appeared FIRST? A. ELIZA B. SHRDLU C. Georgetown-IBM D. ALICE
5. ALICE is dated: A. 1954 B. 1965 C. 1968 D. 1995
6. Which belongs to the statistics-based era? A. IBM's Watson B. ELIZA C. SHRDLU D. ChatGPT
7. The vertical axis of the development chart represents: A. data size B. quality C. cost D. number of rules
8. Which label is used for the shaded band of the current era? A. Rule-based B. Statistical C. Neural + Pre-training D. Symbolic

### 模块 6 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **A** | **B** | **D** | **C** | **D** | **A** | **B** | **C** |

---

## 模块 7：通用框架 Y = f(X) 与开发循环（P44–45）

### 7.1 核心思想

- **Create a function to map an input X into an output Y, where X and/or Y involve language.**
  - 造一个函数，把输入 **X** 映射为输出 **Y**，其中 X 和/或 Y 涉及语言。
- 统一表达：**Y = f(X)**

| 任务 | 英文名 | X | Y |
|---|---|---|---|
| 分类 | **Classification** | Text（文本） | **Label（标签）** |
| 翻译 | **Translation** | Text | **Target Language（目标语言）** |
| 语言建模 | **Language Modeling** | Text | **Continue Text（续写文本）** |
| 语言分析 | **Analysis** | Text | **Linguistic Structure（语言结构）** |
| 图像描述 | **Captioning** | Image（图像） | **Text（文本）** |

### 7.2 通用开发循环（A General Development Cycle）（P45）

- **Data Engineering（数据工程）**：Training Data（训练数据，含 **Labeled Data 标注数据**）
- **Feature Engineering（特征工程）**
- **Learning Algorithms（学习算法）**：
  - **Supervised Learning（监督学习）**
  - **Semi-Supervised Learning（半监督学习）**
  - **Self-Supervised Learning（自监督学习）**
  - **Pre-Trained LMs or LLMs（预训练语言模型 / 大语言模型）**
  - **Prompting（提示）**
  - **Online Learning（在线学习）**
  - **Agents（智能体）**
- 流程：Training Data → Trained Model（训练好的模型）→ Test Data（测试数据）→ Results（结果）→ Real Data（真实数据，回流）


### 模块 7 练习（8 题）

1. In the general framework `Y = f(X)`, X and/or Y involve: A. language B. only images C. only speech D. only formal logic
2. For classification, Y is: A. the target language B. linguistic structure C. continue text D. a label
3. For which task is X an image and Y a text? A. language modeling B. captioning C. translation D. classification
4. Which task has Y = linguistic structure? A. translation B. classification C. analysis D. captioning
5. Which of the following is NOT listed as a learning algorithm/approach in the development cycle? A. supervised learning B. self-supervised learning C. agents D. gradient boosting decision trees
6. In the development cycle, "data engineering" is associated with: A. decision function B. error analysis C. training data (labeled data) D. speech synthesis
7. Which pair is correct? A. translation: Y = a label B. language modeling: Y = continue text C. captioning: X = text, Y = image D. classification: X = image only
8. The development cycle ends with: A. training data B. test data C. labeled data D. real data

### 模块 7 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **A** | **D** | **B** | **C** | **D** | **C** | **B** | **D** |

---

## 模块 8：三种建系统的方法 + 数据需求（P46–47）

| 方法 | 英文 | 做法 | 需要数据？ |
|---|---|---|---|
| 规则 | **Rules** | Manual creation of rules（手工写规则） | 不需要 |
| 微调 | **Fine-tuning** | Machine learning from paired data ⟨X, Y⟩（从成对数据学习） | 需要训练集 |
| 提示 | **Prompting** | Prompting a language model w/o training（不训练，直接提示语言模型） | 不需要训练 |

**规则示例（代码思路）**：

```
sports_keywords = ["baseball", "soccer", "football", "tennis"]
if any(keyword in x for keyword in sports_keywords): return "sports"
else: return "other"
```

**微调示例（成对数据）**：

| X（输入） | Y（标签） |
|---|---|
| I love to play baseball. | sports |
| The stock price is going up. | other |
| He got a hat-trick yesterday. | sports |
| He is wearing tennis shoes. | other |

**提示示例（不训练）**：给 LLM 一句指示 —— "If the following sentence is about 'sports' reply 'sports'. Otherwise reply 'other'."

### 8.2 建系统所需的数据量（Data Requirements）（P47）★

| 层次 | 说明 |
|---|---|
| Rules/prompting based on **intuition**（凭直觉） | No data needed（不需要数据），but also **no performance guarantees**（但也没有性能保证） |
| Rules/prompting based on **spot-checks**（凭抽查） | A small amount of data with **input X only**（少量只有输入 X 的数据） |
| Rules/prompting with **rigorous evaluation**（严格评估） | **Development set（开发集）** with input X and output Y，**e.g., 200–2000 examples**；additional **held-out test set（留出测试集）** also preferable |
| **Fine-tuning（微调）** | Additional **train set（训练集）**。**More is often better —— constant accuracy increase when data size doubles**（数据量翻倍，准确率通常稳定提升） |

> 三件套顺序：**Train（训练）/ Dev（开发）/ Test（测试）**。开发集用来调参、做决策，测试集只在最后用一次。

---


### 模块 8 练习（8 题）

1. Which method is described as "manual creation of rules"? A. fine-tuning B. prompting C. rules D. pre-training
2. Fine-tuning learns from: A. unlabeled text B. hand-written rules C. dictionaries D. paired data ⟨X, Y⟩
3. Prompting differs from fine-tuning because prompting: A. requires a large training set B. needs paired data ⟨X, Y⟩ C. is done without training the model D. cannot be evaluated
4. "Rules/prompting based on intuition" means: A. no data are needed, but there are no performance guarantees B. a full training set is required C. a held-out test set is required D. accuracy increases when data size doubles
5. "Rules/prompting based on spot-checks" require: A. a small amount of data with input X only B. no data at all C. paired data ⟨X, Y⟩ for training D. a test set
6. For rigorous evaluation of rules/prompting, the lecture suggests a development set of about: A. 20–50 examples B. 200–2000 examples C. 20k–50k examples D. 200k+ examples
7. For fine-tuning, when the data size doubles, accuracy: A. always doubles B. usually decreases C. stays the same D. usually increases by a constant amount
8. Which order of datasets is used in the lecture? A. test → dev → train B. train → dev → test C. dev → test → train D. train → test → dev

### 模块 8 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **C** | **D** | **C** | **A** | **A** | **B** | **D** | **B** |

---

## 模块 9：情感分类器完整案例（P48–58）

### 9.1 任务定义

- 输入 **X**：a review on a movie reviewing web site（影评网站的一条评论）
- 输出 **Y**：标签，三分类
  - **Positive（正面）= 1**
  - **Negative（负面）= −1**
  - **Neutral（中性）= 0**
- 例句：
  - "The movie is great!" → Positive (1)
  - "The movie is poor!" → Negative (−1)
  - "We saw this movie after dinner." → Neutral (0)

### 9.2 预测的三个步骤（To Make a Prediction: Three-step Process）（P50–51）★

1. **Feature Extraction（特征抽取）**：从文本中抽取显著特征 → 数据点写成 `⟨b₀, b₁, …, b₁₁, label⟩`
   - 公式：**h = f(x)**
2. **Score Calculation（分数计算）**：为一个或多个可能性计算分数
   - 二分类：**s = wᵀh**（权重向量与特征向量的点积）
   - 多分类：**s = Wh**（权重矩阵乘特征向量，每个类别一个分数）
3. **Decision Function（决策函数）**：从若干可能中选一个
   - 公式：**Y = predict(s)**

### 9.3 完整五步流程（P52）

1. **Featurization（特征化）**
2. **Scoring（打分）**
3. **Decision rule（决策规则）**
4. **Accuracy calculation（准确率计算）**
5. **Error analysis（错误分析）**

### 9.4 特征抽取与权重（代码细节，P53）

**Good words（正面词表）**：`love, good, nice, great, enjoy, enjoyed`
**Bad words（负面词表）**：`hate, bad, terrible, disappointing, sad, lost, angry`

```python
def extract_features(x: str) -> dict[str, float]:
    features = {}
    x_split = x.split(' ')
    # Count the number of "good words" and "bad words" in the text
    good_words = ['love', 'good', 'nice', 'great', 'enjoy', 'enjoyed']
    bad_words = ['hate', 'bad', 'terrible', 'disappointing', 'sad', 'lost', 'angry']
    for x_word in x_split:
        if x_word in good_words:
            features['good_word_count'] = features.get('good_word_count', 0) + 1
        if x_word in bad_words:
            features['bad_word_count'] = features.get('bad_word_count', 0) + 1
    # The "bias" value is always one, allows us to assign a "default" score to the text
    features['bias'] = 1
    return features

feature_weights = {'good_word_count': 1.0, 'bad_word_count': -1.0, 'bias': 0.5}
```

**关键术语**：

- **Feature（特征）**：能支持判断的文本属性，这里就是"好词个数""坏词个数""偏置"。
- **Bias（偏置/截距项）**：**always one**（恒为 1），允许给文本一个 **default score（默认分数）**。

### 9.5 决策规则（Make Decision，P54）★

```python
def run_classifier(x: str) -> int:
    score = 0
    for feat_name, feat_value in extract_features(x).items():
        score = score + feat_value * feature_weights.get(feat_name, 0)
    if score > 0:   return 1     # Positive
    elif score < 0: return -1    # Negative
    else:           return 0     # Neutral
```

**分数算例（必会算）**：文本 `I love this great product`

- 特征：`{'good_word_count': 2, 'bad_word_count': 0, 'bias': 1}`（love、great 都是好词）
- 打分：`score = 0 + (2 × 1.0) + (0 × −1.0) + (1 × 0.5) = 2.5`
- 决策：`2.5 > 0` → 预测 **1（Positive）**

> 规则总结：**score > 0 → 1；score < 0 → −1；score = 0 → 0**。

### 9.6 准确率计算（Accuracy Calculation，P55）

```python
def calculate_accuracy(x_data: list[str], y_data: list[int]) -> float:
    total_number = 0
    correct_number = 0
    for x, y in zip(x_data, y_data):
        y_pred = run_classifier(x)
        total_number += 1
        if y == y_pred:
            correct_number += 1
    return correct_number / float(total_number)
```

- **Accuracy（准确率） = 预测正确的样本数 / 总样本数**（correct_number / total_number）。

### 9.7 错误分析（Error Analysis，P56）

```python
def find_errors(x_data, y_data):
    error_ids = []
    y_preds = []
    for i, (x, y) in enumerate(zip(x_data, y_data)):
        y_preds.append(run_classifier(x))
        if y != y_preds[-1]:
            error_ids.append(i)
    for _ in range(5):   # 随机抽 5 个错误案例查看
        my_id = random.choice(error_ids)
        ...
```

**典型错误案例**：

| 句子 | True label（真实标签） | Predicted label（预测标签） |
|---|---|---|
| But its storytelling prowess and special effects are both **listless**. | −1 | 1 |
| How **inept** is Serving Sara? | −1 | 1 |

**错因**：`listless`（无精打采的）、`inept`（无能的）不在词表里；`prowess`（高超技艺）看着像褒义但实际不决定情感。→ 属于 **low-frequency / rare words（低频罕见词）** 问题。

### 9.8 数据长什么样（What Does the Data Look Like?，P57）

数据格式：**`label ||| text`**（三竖线分隔）

```
1  ||| A warm , funny , engaging film .
1  ||| It 's a lovely film with lovely performances by Buy and Accorsi .
0  ||| No one goes unindicted here , which is probably for the best .
-1 ||| Too much of the humor falls flat .
-1 ||| Detox is ultimately a pointless endeavor .
0  ||| This is nothing but familiar territory .
```

```python
def read_xy_data(filename: str) -> tuple[list[str], list[int]]:
    x_data, y_data = [], []
    with open(filename, 'r') as f:
        for line in f:
            label, text = line.strip().split(' ||| ')
            x_data.append(text)
            y_data.append(int(label))
    return x_data, y_data
```

---


### 模块 9 练习（10 题）

1. In this task, the labels are: A. Positive = 1, Negative = −1, Neutral = 0 B. Positive = 0, Negative = 1, Neutral = 2 C. Positive = 1, Negative = 0 D. a 1-to-5 scale
2. Weights: good = 1.0, bad = −1.0, bias = 0.5. The score of "I love this great product" is: A. 1.5 B. 2.0 C. 2.5 D. 3.0
3. Same weights. The score of "I hate this terrible movie" is: A. −2.5 B. −2.0 C. −1.5 D. 0.5
4. Same weights. What is predicted for "We saw this movie after dinner." (no word from either list)? A. 1 B. −1 C. 0 D. an error
5. The score of "I love this movie" is 2.5. Without the bias term it would be: A. 1.5 B. 2.5 C. 0.5 D. 2.0
6. In the code, `features['bias'] = 1` means: A. the bias is 1 only for neutral sentences B. the bias is learned from the data C. the sentence contains a bias word D. the feature is added for every input regardless of its content
7. Accuracy is computed as: A. correct predictions / total predictions B. total predictions / correct predictions C. errors / total predictions D. correct predictions − errors
8. If the classifier is correct on 27 of 30 reviews, its accuracy is: A. 0.27 B. 0.80 C. 0.90 D. 0.30
9. The data format used in the lecture's file is: A. text ||| label B. label ||| text C. label, text D. text: label
10. The review "…special effects are both listless." (true label −1) was predicted as 1 mainly because: A. of negation B. the words listless/inept are not in the word lists C. the sentence has no bias D. the accuracy formula is wrong

### 模块 9 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **A** | **C** | **C** | **A** | **D** | **D** | **A** | **C** | **B** | **B** |

---

## 模块 10：改进循环 + 五类难点案例（P58–64）

### 改进系统的循环（P58）★

1. **What's going wrong with my system?** → Look at **error analysis**（哪里出了问题？→ 看错误分析）
2. **Modify the system**（修改系统：featurization 特征化、scoring function 打分函数等）
3. **Measure accuracy improvements, accept/reject change**（测准确率提升，决定接受还是回退）
4. **Repeat from (1)**（重复）
5. **Finally, when satisfied with dev accuracy, evaluate on test!**（开发集满意后，最后才在**测试集**上评估！）

> 考点：**开发集（dev）用来迭代，测试集（test）只在最后用**；如果在测试集上反复调参，就变成了数据泄漏（data leakage）。

---


### 困难案例与解决方案（P60–P64）★


| # | 挑战 | 英文 | 例句 | 解决方案 |
|---|---|---|---|---|
| 1 | 低频罕见词 | **Low-Frequency (Rare) Words** | "…the material link is too tenuous to anchor the emotional connections…" (Negative) | Keep working till we get all of them；**Incorporate external resources such as sentiment dictionaries**（引入情感词典等外部资源） |
| 2 | 词形变化 | **Conjugation / Morphological Variation** | "entertainingly acted, magnificently shot…" (Positive)；"an overlong episode…" (Negative) | **Morphological analysis**（形态分析）还原 **root form（词根形式）** 与 **POS（词性）** |
| 3 | 否定 | **Negation** | "This one is **not** nearly as dreadful as expected." (Positive)；"Serving Sara **doesn't** serve up a whole lot of laughs." (Negative) | If a negation modifies a word, it should be **disregarded**（否定词修饰的极性应被忽略）；**Syntactic analysis would probably be necessary**（需要句法分析） |
| 4 | 隐喻与类比 | **Metaphor and Analogy** | "Puts a human face on a land most Westerners are unfamiliar with."；"Has all the depth of a wading pool." (Negative) | You probably need **world knowledge**（世界知识） |
| 5 | 多语言 | **Multilingual** | "Este é um trabalho que conquista com sucesso o coração do público." (Positive, 葡萄牙语) | **Learn other languages, e.g., Portuguese**（要会别的语言，如葡语） |

> 记忆串联：**罕见词→查词典；词形变化→形态分析；否定→句法分析+忽略；隐喻→世界知识；多语言→多语言能力**。

---


### 模块 10 练习（10 题）

1. According to the improvement loop, the first step is: A. evaluate on the test set B. look at error analysis to see what is going wrong C. immediately add new features D. retrain the model
2. When should the test set be used? A. after every modification B. before training the model C. it should be used for tuning D. only once, when satisfied with dev accuracy
3. "Keep working till we get all of them; incorporate external resources such as sentiment dictionaries" is the solution for: A. negation B. metaphor and analogy C. low-frequency (rare) words D. multilingual
4. The solution "morphological analysis would be needed to recover the root form and POS" addresses: A. conjugation / morphological variation B. rare words C. negation D. multilingual
5. "This one is not nearly as dreadful as expected." (labeled POSITIVE) illustrates: A. rare words B. metaphor C. multilingual D. negation
6. The lecture says that handling negation "would probably be necessary" with: A. syntactic analysis B. world knowledge C. speech recognition D. sentiment dictionaries
7. "Has all the depth of a wading pool." (Negative) requires: A. morphological analysis B. a bigger word list C. world knowledge D. OCR
8. The Portuguese review is used to illustrate: A. negation B. the multilingual challenge C. rare words D. metaphor
9. Step 3 of the improvement loop is to: A. repeat from step 1 B. evaluate on the test set C. look at error analysis D. measure the accuracy improvement and accept/reject the change
10. The examples containing "tenuous" and "glitches" are used to show the problem of: A. low-frequency (rare) words B. negation C. metaphor D. multilingual

### 模块 10 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **D** | **C** | **A** | **D** | **A** | **C** | **B** | **D** | **A** |

---

## 模块 11：机器学习、词袋模型 BOW 与结构化感知机（P65–70）

### 11.1 机器学习：超越手工规则（P66）

- 仍用 `h = f(x)`、`s = wᵀh`，但把"写规则"换成 **Learning Algorithm（学习算法）**：从 `X_Train / Y_Train` 学出权重，再在 `X_Dev / Y_Dev` 上调，最后在 `X_Test` 上评估。

### 11.2 词袋模型（Bag of Words / BOW）（P67）

- 做法：把句子里的词逐个 **lookup（查表）** 取出各自的向量，**相加（+）** 得到句子表示，再与 **weights（权重）** 做 **dot product（点积）** 得到 **score（分数）**。
- 例句：`I like this movie` → 查表 → 相加 → 点乘权重 → 分数
- 核心结论：**Features f are based on word identity（特征基于"词本身"）and weights w are learned（权重是被学出来的）**。
- 关键词：**word identity（词的身份/词形）**，即只看"出现了哪个词、出现几次"，**不看词序**。

### 11.3 向量代表什么（What do Our Vectors Represent?）（P68）

- **Binary classification（二分类）**：每个词只有一个标量，正数表示"是（yes）"，负数表示"否（no）"
  - love 2.4 ／ hate −3.5 ／ nice 1.2 ／ no −0.2 ／ dog −0.3
- **Multi-class classification（多分类）**：每个词有多个分量，例如 5 类对应 **[very good, good, neutral, bad, very bad]**
  - love：[2.4, 1.5, −0.5, −0.8, −1.4]
  - hate：[−3.5, −2.0, −1.0, 0.4, 3.2]
  - nice：[1.2, 2.1, 0.4, −0.1, −0.2]
  - no：[−0.2, 0.3, −0.1, 0.4, 0.5]
  - dog：[−0.3, 0.3, 0.6, 0.2, −0.2]

> 注意：BOW 学到的"权重"本质上是**词的情感极性打分**（如 love 很正面、hate 很负面），dog 接近中性。

### 11.4 BOW 的训练：结构化感知机（Training of BOW Models: Structured Perceptron）（P69）★

```python
feature_weights = {}
for x, y in data:
    # Make a prediction
    features = extract_features(x)
    predicted_y = run_classifier(features)
    # Update the weights if the prediction is wrong
    if predicted_y != y:
        for feature in features:
            feature_weights[feature] = feature_weights.get(feature, 0) + y * features[feature]
```

- 算法名：**Structured Perceptron（结构化感知机）**（课件原话：An algorithm called "Structured Perceptron"）
- 更新规则：**只在预测错误时更新**，`weight[feature] += y × feature_value`
  - 若真实标签 y 为正而预测错 → 好词的权重被加大
  - 若真实标签 y 为负而预测错 → 好词的权重被减小（y 为负数）
- 术语：**update the weights（更新权重）**、**prediction（预测）**。

### 11.5 BOW 缺什么（What's Missing in BOW?）（P70）★

| 缺失能力 | 英文 | 例子 |
|---|---|---|
| 处理词形变化/复合词 | **Handling of conjugated or compound words** | I love this move → I **loved** this **movie** |
| 处理词义相似 | **Handling of word similarity** | I love this movie → I **adore** this movie |
| 处理组合特征 | **Handling of combination features** | I love this movie → I **don't** love this movie；I hate this movie → I **don't** hate this movie |
| 处理句子结构 | **Handling of sentence structure** | It has an interesting story **but** is boring overall |

---


### 模块 11 练习（10 题）

1. In BOW, features are based on ___ and weights are ___: A. word order; learned B. sentence structure; hand-written C. word identity; learned D. word identity; hand-written
2. In the binary model, each word's weight is a single scalar where: A. positive indicates "yes" and negative indicates "no" B. the value is always positive C. it stores the word frequency D. it is hand-written
3. In the multi-class model, each word has one component per: A. sentence B. document C. hidden layer D. class (e.g., very good … very bad)
4. `love` has binary weight 2.4 and multi-class vector [2.4, 1.5, −0.5, −0.8, −1.4]. The binary weight equals: A. the average of the five components B. the first component (very good) C. the sum of the components D. the last component
5. The algorithm used to train the BOW weights is called: A. k-means B. backpropagation C. Structured Perceptron D. dynamic programming
6. In Structured Perceptron, the weights are updated: A. only when the prediction is wrong B. after every example C. once at the very end D. never
7. The update rule is: A. w[f] = y + f_value B. w[f] += y × feature_value C. w[f] = 0 D. w[f] −= feature_value
8. Which of the following is NOT listed as a limitation of BOW? A. conjugated or compound words B. word similarity C. combination features such as negation D. too few features
9. "I love this movie" vs "I don't love this movie" illustrates BOW's inability to handle: A. word similarity B. conjugated words C. combination features D. sentence length
10. Compared with the rule-based approach, the key difference of the machine-learning approach is: A. the weights are learned by a learning algorithm instead of being hand-written B. no features are needed C. the score is no longer computed D. there is no training data

### 模块 11 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **C** | **A** | **D** | **B** | **C** | **A** | **B** | **D** | **C** | **A** |

---

## 模块 12：神经网络 + 课程大纲（P71–73）

- 同样输入 `I like this movie`：**lookup → 相加 → weights → score**，但特征与权重由 **Neural Networks（神经网络）** 给出。
- 课件评价：**Powerful enough to perform classification, LM, any task!**（强大到可以做分类、语言建模乃至任何任务！）
- 关键区别：**"Some complicated functions to extract features"（用复杂的函数来抽特征）** —— 特征不再靠人工设计，而是学出来的。
- **LM = Language Modeling（语言建模）**：预测下一个词/给定前文生成文本的任务。

---


### 后续课程内容（Future Roadmap，P73）


1. **Word Representation and Text Classification**（词表示与文本分类）
2. **Language Modeling**（语言建模）
3. **Sequence Modeling**（序列建模）
4. **Transformers**（Transformer 架构）
5. **Machine Translation**（机器翻译）
6. **Pretraining**（预训练）
7. **Fine Tuning and Instruction Tuning**（微调与指令微调）
8. **Prompting**（提示学习）
9. **Benchmarks and Evaluations**（基准测试与评估）
10. **How to Conduct Research in NLP**（如何做 NLP 研究）

**参考来源（References）**：Eisenstein, *Natural Language Processing* (2018)；Bisong & Bisong, *Google Colaboratory* (2019)；部分幻灯片改编自 **Graham Neubig (2024)** 的课程。

---


### 模块 12 练习（8 题）

1. Compared with the rule-based system, the main change in the neural network model is: A. complicated functions extract the features instead of hand-written rules B. no features are used C. the score is not computed D. no weights are needed
2. The lecture says neural networks are powerful enough to perform: A. only classification B. only translation C. classification, language modeling, and any task D. only speech tasks
3. Which is the FIRST item in the tentative course content list? A. Transformers B. Word Representation and Text Classification C. Prompting D. Machine Translation
4. Which topic appears in the roadmap? A. Optical character recognition B. Speech signal processing C. Computer vision D. Fine Tuning and Instruction Tuning
5. In "perform classification, LM, any task," LM stands for: A. Language Modeling B. Logical Meaning C. Lexical Morphology D. Learning Machine
6. Which topic deals with evaluating NLP systems on standard datasets? A. Pretraining B. Prompting C. Benchmarks and Evaluations D. Sequence Modeling
7. The lecture notes that some slides are adapted from the course given by: A. Jacob Eisenstein B. Graham Neubig (2024) C. Daniel Jurafsky D. Philipp Koehn
8. Which of the following is NOT among the ten roadmap topics? A. Sequence Modeling B. Prompting C. Transformers D. Optical Character Recognition

### 模块 12 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 答 | **A** | **C** | **B** | **D** | **A** | **C** | **B** | **D** |

---

# 附录

## 附录 A：课程事务与政策（P1–P9）

### A.1 教材（Text Books）

- **主教材**：*Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition*, 3rd ed., Daniel Jurafsky & James Martin, Prentice Hall, 2024.

  - **Natural Language Processing（自然语言处理）** = 让计算机处理人类语言。
  - **Computational Linguistics（计算语言学）** = 用计算方法研究语言学的学科视角。
  - **Speech Recognition（语音识别）** = 把语音信号转成文字。

- *Neural Machine Translation*, Philipp Koehn, 2018.
  - **Neural Machine Translation / NMT（神经机器翻译）** = 用神经网络做翻译。
- *Deep Learning*, I. Goodfellow, Y. Bengio, A. Courville, MIT Press, 2017.

### A.2 参考书（Reference Books）

- *Foundations of Statistical Natural Language Processing*, D. Manning & H. Schütze, 1999.
- *Foundations of Large Language Models*, Tong Xiao & Jingbo Zhu, 2025.
  - **Large Language Model / LLM（大语言模型）** = 在海量文本上预训练的大型神经网络语言模型。

- **Course Website（课程网站）**：http://ummoodle.umac.mo/

### A.3 课程结构（Course Structure）

- **Assignments（作业）**：hands-on experiments（动手实验）；reading and problem solving（阅读与解题）。
  - 课件原话："No way to really internalize without doing it"（不亲手做就没法真正内化）。
- **Term Project（学期项目）**：
  - **Paper Reading（论文阅读）**：review selected state-of-the-art research topics（综述精选前沿课题），learn the research methodology and experiment results（学习研究方法与实验结果）。
  - **Development（开发实践）**：implement and extend based on the selected topic（在选定课题上实现并扩展）。

### A.4 考核（Assessment）

| 项目 | 比例 |
|---|---|
| Assignments（作业） | 40% |
| Term Projects（学期项目） | 60% |

**Late submission policy（迟交政策）**：

| 迟交时长 | 扣分 |
|---|---|
| 1 day late（迟 1 天） | 扣 15% |
| 2 days late（迟 2 天） | 扣 30% |
| 3 days late（迟 3 天） | 扣 50% |
| 4 or more days late（≥4 天） | 得 0% |

- Assignments have to be done **individually**（必须个人独立完成）→ **No collaboration with others（不得与他人合作）**。
- **Class Participation（课堂参与）**：in-class assignments（随堂作业）。

### A.5 生成式 AI 使用政策（Policy for Using Generative AI Tools）

**May be used as（可以用于）**：learning and problem-solving assistants（学习与解题助手）。

**Appropriate Use（合规用法）**：

- **Explain concepts** and clarify understanding（讲解概念、理清理解）
- Provide **hints**（提示）、**suggestions**（建议）、**alternative approaches**（替代思路）
- Help **debug** code（调试代码）and improve writing（改进写作）
- Offer **feedback** on solutions（对解答给出反馈）

**Not Permitted（禁止用法）**：

- **Generate complete assignment solutions for submission**（用 AI 生成完整作业解答直接提交）
- **Copy AI-generated answers without independent work and understanding**（不经独立思考与理解就照抄 AI 答案）

**核心原则**：GenAI should **support learning, not replace independent thinking and problem solving**（AI 应支持学习，而非替代独立思考与解题）。Students must **independently complete and submit their own work**（必须独立完成并提交自己的作品）。

### A.6 学术诚信（Academic Integrity）

- 必须遵守《澳门大学学术诚信与学术诚实政策》。
- **Permitted use of GenAI does not excuse（允许使用 AI 不能成为以下行为的借口）**：
  - **plagiarism（抄袭）**
  - **unauthorized collaboration（未经授权的合作）**
  - **fabrication（编造）**
  - **falsification（篡改）**
  - **misrepresentation（虚假陈述）**
  - **submitting AI-generated work as one's own（把 AI 生成的内容当作自己的成果提交）**
- Any use of GenAI must **support, not replace, the student's original intellectual contribution**（AI 只能支持、不能替代学生本人的智力贡献）。
- **Students MUST Declare any GenAI use（必须声明所有 AI 使用情况）**，包括如何使用。

### A.7 课程内容（Course Content，五点）

1. Learn in detail about **building NLP systems from a research perspective**（从研究视角细致了解如何构建 NLP 系统）
2. Learn **basic and advanced topics in machine learning approaches to NLP and language models**（NLP 的机器学习方法与语言模型，从基础到进阶）
3. Learn **basic linguistic knowledge useful in NLP**（对 NLP 有用的基础语言学知识）
4. See **case studies** of NLP applications and learn how to identify unique problems for each（看应用案例，学会识别每个任务特有的问题）
5. Learn how to **debug when and where NLP systems fail**（学会排查 NLP 系统在何时何处失败），and build improvements based on this（并据此改进）

### A.8 教学团队（Teaching Assistants & Project Advisors）

- Instructor（授课教师）：Derek F. Wong；隶属 **NLP2CT（Natural Language Processing & Portuguese-Chinese Machine Translation Research Group，自然语言处理与葡汉机器翻译研究组）** 与 **CAGI（Centre for Artificial General Intelligence，通用人工智能中心）**。
- 助教（TAs）与项目导师（PAs）：Zhaocong、Yingpeng、Yutong、Junchao、Jingkun、Kaixin、Fengying 等，部分 TBA（To Be Announced，待定）。

---


## 附录 B：术语总表（英中对照）
### 14.1 语言学基础

| English | 中文 | 一句话记忆 |
|---|---|---|
| natural language | 自然语言 | 中文、英文这类人类语言 |
| ordinary language | 日常语言 | 自然语言的别称 |
| constructed language | 人造语言 | 如世界语 |
| artificial language | 人工语言 | 与自然语言相对 |
| machine language | 机器语言 | 计算机指令语言 |
| language of formal logic | 形式逻辑语言 | 符号化、无歧义 |
| phonetics | 语音学 | 声音**如何物理形成** |
| phonology | 音系学 | 离散声音的**系统/音节结构** |
| syllable | 音节 | dis-connect |
| morphology | 形态学 | 词内部成分（前缀/词干/后缀） |
| prefix / stem / suffix | 前缀 / 词干 / 后缀 | dis- + connect + -ing |
| lexicon | 词汇（库） | 词表 |
| syntax | 句法学 | 词与词的**结构关系** |
| semantics | 语义学 | **字面意义** |
| pragmatics | 语用学 | 意义与**意图、目标**的关系 |
| discourse | 篇章/话语 | 大于单句的单位 |
| utterance | 话语/言语行为单位 | 一次说出的话 |
| turn taking | 话轮转换 | 对话轮流说话 |
| thread of meaning | 意义主线 | 话题连贯性 |
| ambiguity | 歧义 | NLP 的根本难题 |
| lexical ambiguity | 词汇歧义 | 一词多义或多词性 |
| lexical category | 词性/词类 | duck 是 N 还是 V |
| lexical semantics | 词汇语义 | make = create 还是 cook |
| structural / syntactic ambiguity | 结构/句法歧义 | 修饰关系不明 |
| world knowledge | 世界知识 | 金沙=赌场 |
| redundancy | 冗余性 | 信息多重表达 |
| language evolution | 语言演变 | 语言会变 |
| conventional and arbitrary | 约定俗成且任意 | 词与物无必然联系 |
| language systematics | 语言系统性 | 各层次成体系 |

### 14.2 NLP 任务与概念

| English | 中文 |
|---|---|
| natural language processing (NLP) | 自然语言处理 |
| computational linguistics | 计算语言学 |
| speech recognition | 语音识别 |
| speech synthesis | 语音合成 |
| speech translation | 语音翻译 |
| machine translation (MT) | 机器翻译 |
| neural machine translation (NMT) | 神经机器翻译 |
| language modeling (LM) | 语言建模 |
| generation | （文本）生成 |
| understanding | （语言）理解 |
| question answering (Q&A) | 问答 |
| dialog | 对话 |
| captioning | 图像描述/配文 |
| classification | 分类 |
| label | 标签 |
| sentiment analysis | 情感分析 |
| positive / negative / neutral | 正面 / 负面 / 中性 |
| hallucination | 幻觉（编造内容） |
| in-context learning | 上下文学习 |
| computational social science | 计算社会科学 |
| semantic roles / thematic roles | 语义角色/题元角色 |
| AMR (abstract meaning representation) | 抽象语义表示 |
| power or agency | 权力或能动性 |

### 14.3 系统构建与机器学习

| English | 中文 |
|---|---|
| rule-based | 规则驱动的 |
| statistics-based / statistical model | 统计驱动的 / 统计模型 |
| deep learning-based | 深度学习驱动的 |
| pre-training | 预训练 |
| fine-tuning | 微调 |
| prompting | 提示（学习） |
| instruction tuning | 指令微调 |
| supervised learning | 监督学习 |
| semi-supervised learning | 半监督学习 |
| self-supervised learning | 自监督学习 |
| online learning | 在线学习 |
| agent | 智能体 |
| feature extraction | 特征抽取 |
| feature engineering | 特征工程 |
| data engineering | 数据工程 |
| featurization | 特征化 |
| score calculation | 分数计算 |
| decision function | 决策函数 |
| decision rule | 决策规则 |
| accuracy | 准确率 |
| error analysis | 错误分析 |
| training set | 训练集 |
| development set (dev set) | 开发集 |
| test set | 测试集 |
| held-out test set | 留出测试集 |
| labeled data | 标注数据 |
| paired data ⟨X, Y⟩ | 成对数据 |
| bias | 偏置（恒为 1 的默认分数项） |
| weight | 权重 |
| dot product | 点积 |
| bag of words (BOW) | 词袋模型 |
| word identity | 词的身份/词形 |
| structured perceptron | 结构化感知机 |
| update the weights | 更新权重 |
| conjugation | 动词变位/词形变化 |
| compound word | 复合词 |
| word similarity | 词义相似度 |
| combination features | 组合特征 |
| selectional restrictions | 选择限制 |
| parse tree / syntax tree | 句法树 |
| part-of-speech (POS) | 词性/词类 |
| root form | 词根形式 |
| agglutinative language | 黏着语 |
| RBMT / EBMT / SMT / NMT | 规则/实例/统计/神经机器翻译 |
| state-of-the-art (SOTA) | 最先进的 |
| benchmark | 基准（测试集） |
| evaluation | 评估 |

---


## 附录 C：易错点对比速查
| 容易混 | 区别 |
|---|---|
| **Phonetics vs Phonology** | 前者：声音**如何物理形成**；后者：**声音系统/音节结构** |
| **Semantics vs Pragmatics** | 前者：**字面意义**；后者：**意图与目标**的关系 |
| **Syntax vs Semantics** | 前者：**结构关系**；后者：**意义** |
| **lexical category vs lexical semantics** | 前者：**词性**（N/V、所有格/与格）；后者：**词义**（create/cook） |
| **s = wᵀh vs s = Wh** | 前者：**二分类**（点积得一个数）；后者：**多分类**（每类一个分数） |
| **规则阶段 vs 统计阶段 vs 深度阶段** | 1950–1990 **关键词**；1990–2010 **句法分析**；2014–今 **语义特征抽取** |
| **Rules vs Fine-tuning vs Prompting** | 手工规则 / 从成对数据学 / 不训练只提示 |
| **Dev set vs Test set** | dev 用来**反复迭代**；test **只在最后**评估一次 |
| **Y = 标签 vs Y = 目标语言** | 分类 vs 翻译 |
| **BOW 能做 vs 不能做** | 能：按词学权重；不能：词序/句子结构、词形变化、同义词、否定组合 |

---


## 附录 D：数字与公式速查
- `Y = f(X)` ｜ `h = f(x)`（特征抽取）｜ `s = wᵀh`（二分类）｜ `s = Wh`（多分类）｜ `Y = predict(s)`
- 决策：**score > 0 → 1；score < 0 → −1；score = 0 → 0**
- 算例：好词权重 1.0，坏词权重 −1.0，bias 0.5；`I love this great product` → **2.5（Positive）**
- 准确率 = **correct_number / total_number**
- 感知机：**仅预测错误时**更新，`w[f] += y × f_value`
- 开发集规模：**200–2000** 条
- 迟交：**1 天 −15%、2 天 −30%、3 天 −50%、≥4 天 0%**
- 成绩：**作业 40% + 项目 60%**
- 历史年份：**1954** Georgetown-IBM、**1965** ELIZA、**1968** SHRDLU、**1995** ALICE、**2006** Watson、**2010** SIRI、**2015** Cortana、**2023** ChatGPT
- 阶段区间：**规则 1950–1990 ／ 统计 1990–2010 ／ 深度学习 2014–now**

---


## 附录 E：一页式考前速记
1. **语言四性**：系统性 / 约定任意性 / 冗余性 / 演变性
2. **六大层次**：Phonology 音系、Morphology 形态、Syntax 句法、Semantics 语义、Pragmatics 语用、Discourse 篇章
3. **NLP 四用途**：用计算机处理语言 / 助人机交流 / 助人际交流 / 分析理解语言
4. **`I made her duck`**：词性歧义（duck N/V；her 所有格/与格）+ 词义歧义（make = create/cook）
5. **流程**：语音 → 音系形态分析 → 词序列 → 句法分析 → 句法结构 → 语义解释 → 逻辑式 → 语境推理 → 意义表示
6. **发展史**：规则 1950–1990（关键词）→ 统计 1990–2010（句法分析）→ 深度学习 2014–今（语义特征）
7. **框架**：`Y = f(X)`；分类/翻译/语言建模/结构分析/图像描述
8. **三方法**：Rules（手工、无需数据）/ Fine-tuning（成对数据）/ Prompting（不训练）
9. **三步预测**：`h = f(x)` → `s = wᵀh` 或 `Wh` → `Y = predict(s)`
10. **情感算例**：2.5 → Positive；决策 >0→1、<0→−1、=0→0
11. **五难点**：罕见词→外部词典；词形变化→形态分析；否定→句法分析；隐喻→世界知识；多语言→多语言能力
12. **BOW**：按词学权重；缺词序、词形、同义、组合
13. **Structured Perceptron**：仅在错误时更新
14. **流程纪律**：dev 迭代，test 只测一次
15. **课程政策**：独立完成、必须声明 AI 使用、AI 不能代替你思考

---


## 附录 F：题库（共三组 74 题）

**题目**

1. Which of the following is NOT a property shared by all natural languages? A. Systematics B. Conventional and arbitrary C. Redundancy D. Fixed and unchanging
2. The study of word components is called: A. Phonology B. Morphology C. Syntax D. Pragmatics
3. Which layer studies the relationship of meaning to the goals and intentions of the speaker? A. Semantics B. Syntax C. Pragmatics D. Discourse
4. Semantics is best defined as the study of: A. linguistic sound B. word components C. structural relations between words D. literal meaning
5. In "I made her duck," the fact that "duck" can be a noun or a verb is an example of: A. lexical category ambiguity B. lexical semantics ambiguity C. pragmatic ambiguity D. no ambiguity
6. Which is NOT a way NLP is used, according to the lecture? A. Handle human language using computers B. Aid human-machine communication C. Aid human-human communication D. Replace natural languages with constructed ones
7. In the history of NLP, the rule-based era is: A. 1950–1990 B. 1990–2010 C. 2014–now D. 1965–1985
8. Which system came FIRST? A. ELIZA B. SHRDLU C. Georgetown-IBM D. ALICE
9. In the general framework `Y = f(X)`, for machine translation: A. Y = a label B. Y = linguistic structure C. Y = the target language D. Y = a caption
10. Fine-tuning differs from writing rules mainly because it: A. needs no data B. learns from paired data ⟨X, Y⟩ C. requires no training D. cannot be evaluated
11. A development set used for rigorous evaluation contains roughly: A. 10–50 examples B. 200–2000 examples C. 20k–50k examples D. no examples at all
12. In the three-step prediction process, `s = Wh` (matrix form) is used for: A. binary classification B. multi-class classification C. decision function D. feature extraction
13. With weights good_word_count = 1.0, bad_word_count = −1.0, bias = 0.5, the score of "I love this great product" is: A. 1.5 B. 2.0 C. 2.5 D. −2.5
14. "If a negation modifies a word, it should be disregarded" is the solution for which challenge? A. rare words B. negation C. metaphor D. multilingual
15. Which challenge probably requires world knowledge to solve? A. morphological variation B. metaphor and analogy C. negation D. conjugation
16. Which is a limitation of the bag-of-words model? A. It cannot handle word identity B. It cannot represent word order or sentence structure C. It cannot learn weights D. It cannot be used for binary classification
17. The algorithm used in the lecture to train BOW weights is: A. Structured Perceptron B. k-means C. backpropagation D. dynamic programming
18. In that training algorithm, weights are updated: A. on every example B. only when the prediction is wrong C. only at the end D. never
19. With the rule-based sentiment classifier, a score of exactly 0 predicts: A. Positive (1) B. Negative (−1) C. Neutral (0) D. error
20. According to the course's GenAI policy, which is permitted? A. Submitting AI-generated complete solutions B. Copying AI answers without understanding C. Using GenAI to explain concepts and give hints D. Using GenAI without declaring it

**答案与解析**

| 题 | 答案 | 解析 |
|---|---|---|
| 1 | **D** | 自然语言四大特性：系统性、约定任意性、冗余性、**演变性**——"固定不变"是错的 |
| 2 | **B** | Morphology = study of word components |
| 3 | **C** | Pragmatics = meaning ↔ goals and intentions |
| 4 | **D** | Semantics = literal meaning（句子的字面意义） |
| 5 | **A** | duck 名/动 → **词性**歧义（lexical category）；make=create/cook 才是词义歧义 |
| 6 | **D** | NLP 四种用途；"取代自然语言"不是 |
| 7 | **A** | 规则驱动 1950–1990，特征是基于关键词的意图识别 |
| 8 | **C** | Georgetown-IBM 1954 最早 |
| 9 | **C** | 翻译的 Y 是目标语言 |
| 10 | **B** | Fine-tuning = machine learning from paired data ⟨X, Y⟩ |
| 11 | **B** | 严格评估的开发集约 200–2000 条 ⟨X, Y⟩ |
| 12 | **B** | `s = Wh` 对应多分类；`s = wᵀh` 对应二分类 |
| 13 | **C** | 2×1.0 + 0×(−1.0) + 1×0.5 = 2.5 |
| 14 | **B** | 否定：被否定词修饰的极性应忽略，需句法分析 |
| 15 | **B** | 隐喻与类比需要世界知识 |
| 16 | **B** | BOW 不能表达词序与句子结构（权重是能学的） |
| 17 | **A** | Structured Perceptron（结构化感知机） |
| 18 | **B** | 只在预测错误时更新：`w += y × feature_value` |
| 19 | **C** | score = 0 → 预测中性（0） |
| 20 | **C** | 允许讲解概念、给提示；禁止提交 AI 答案、禁止不声明 |

---


**题目**

21. NLU (Natural Language Understanding) is best described as:
   A. converting meaning into natural language text
   B. mapping language into a meaning representation
   C. training large language models on unlabeled corpora
   D. translating one natural language into another
22. Which pair correctly matches an NLU pipeline stage with the knowledge it uses?
   A. Syntactic analyzer ← world knowledge
   B. Contextual reasoner ← grammatical knowledge
   C. Semantic interpreter ← selectional restrictions
   D. Morphological analyzer ← pragmatic knowledge
23. Which component of the NLU pipeline uses pragmatic and world knowledge?
   A. phonological/morphological analyzer
   B. syntactic analyzer
   C. semantic interpreter
   D. contextual reasoner
24. In the rule-based sentiment classifier, `features['bias'] = 1` is executed for every input. Its purpose is to:
   A. count the neutral words in the sentence
   B. provide a constant default score, shifting the decision boundary
   C. normalize the sentence length
   D. store the gold label
25. Weights: good_word_count = 1.0, bad_word_count = −1.0, bias = 0.5. The sentence "This film is boring and predictable." contains no word from either list. What does the classifier predict?
   A. 1
   B. −1
   C. 0
   D. It crashes
26. In the multi-class sentiment model, the label of a sentence is decided by:
   A. taking the sign of a single total score
   B. counting the good and bad words
   C. summing the word vectors and taking the class with the highest value
   D. comparing the score with the threshold 0.5
27. With classes [very good, good, neutral, bad, very bad], the vector of `nice` is [1.2, 2.1, 0.4, −0.1, −0.2]. `nice` most strongly supports:
   A. very good
   B. neutral
   C. good
   D. bad
28. Given nice = [1.2, 2.1, 0.4, −0.1, −0.2] and dog = [−0.3, 0.3, 0.6, 0.2, −0.2], the predicted class for "nice dog" is:
   A. very good
   B. good
   C. neutral
   D. bad
29. In the binary sentiment model each word has only a single scalar weight because:
   A. a single score per word suffices; its sign decides positive vs negative
   B. words are binary features
   C. there is no bias term
   D. the vocabulary is too small to store vectors
30. Which of the following is NOT one of the five challenges/difficult cases discussed in the lecture?
   A. negation
   B. spelling errors and typos
   C. metaphor and analogy
   D. low-frequency (rare) words
31. According to the lecture, the low-frequency (rare) word problem should be addressed by:
   A. discarding sentences that contain rare words
   B. ignoring the polarity of the whole sentence
   C. applying world knowledge
   D. incorporating external resources such as sentiment dictionaries
32. A student submits an assignment 4 days after the deadline. The penalty is:
   A. −15%
   B. −30%
   C. −50%
   D. no marks (0%)
33. In the assessment scheme, term projects account for:
   A. 60%
   B. 50%
   C. 40%
   D. 100%
34. "Intent recognition based on syntax analysis" characterizes which era?
   A. rule-based (1950–1990)
   B. statistics-based (1990–2010)
   C. deep-learning-based (2014–now)
   D. none of the above
35. Which system belongs to the deep-learning era in the lecture's timeline?
   A. SHRDLU
   B. ELIZA
   C. ALICE
   D. Microsoft Cortana
36. In the bag-of-words model: features are based on ____ and weights are ____.
   A. word order; learned from data
   B. sentence structure; hand-written by experts
   C. word identity; hand-written by experts
   D. word identity; learned from data
37. Which pair of sentences best illustrates the "combination features" limitation of BOW?
   A. "I love this movie." / "I loved this movie."
   B. "I love this movie." / "I adore this movie."
   C. "I love this movie." / "I don't love this movie."
   D. "It has an interesting story but is boring overall."
38. Structured Perceptron: `feature_weights = {}` initially. For an example whose features are `{'good_word_count': 1, 'bias': 1}` with gold label y = 1, the prediction was wrong. After the update, `feature_weights['bias']` equals:
   A. 0
   B. 0.5
   C. 1
   D. −1
39. You check accuracy after each modification while developing. When should you evaluate on the test set?
   A. after every modification
   B. only once, after you are satisfied with dev-set accuracy
   C. before training the model
   D. never; dev accuracy is enough
40. Which statement about the framework Y = f(X) is correct?
   A. For captioning, X is an image and Y is text
   B. Y is always a label
   C. X is always text
   D. For language modeling, X and Y are both labels
41. The pair "It's easy to recognize speech." / "It's easy to wreck a nice beach." shows a difficulty at which level?
   A. phonetics/phonology
   B. morphology
   C. syntax
   D. discourse
42. "我们去金沙 → Let's go to the Sands casino" illustrates the need for:
   A. morphological analysis
   B. syntactic analysis
   C. speech synthesis
   D. world knowledge

**答案与解析**

| 题 | 答案 | 解析 |
|---|---|---|
| 21 | **B** | NLU = 语言 → 意义表示；A 是 NLG，D 是翻译 |
| 22 | **C** | 语义解释器用语义知识与选择限制 |
| 23 | **D** | 语境推理器（contextual reasoner）用语用与世界知识 |
| 24 | **B** | bias 恒为 1，等于给每个句子垫一个常数底分，平移决策边界 |
| 25 | **A** | 分数 = 0 + 0 + 1×0.5 = 0.5 > 0 → 预测 1（正 bias 让模型默认偏正面，这题本该是中性） |
| 26 | **C** | 多分类：词向量逐维相加，取最大分量对应的类 |
| 27 | **C** | 2.1 最大，落在 good 上 |
| 28 | **B** | [1.2,2.1,0.4,−0.1,−0.2] + [−0.3,0.3,0.6,0.2,−0.2] = [0.9,**2.4**,1.0,0.1,−0.4] → good |
| 29 | **A** | 二分类一个标量即可，正负号决定类别 |
| 30 | **B** | 五类难点：罕见词、词形变化、否定、隐喻类比、多语言；拼写错误不在其中 |
| 31 | **D** | Incorporate external resources such as sentiment dictionaries |
| 32 | **D** | ≥4 天迟交得 0% |
| 33 | **A** | 作业 40% + 项目 60% |
| 34 | **B** | 统计阶段 1990–2010 |
| 35 | **D** | Cortana（2015）属深度学习阶段；SHRDLU、ELIZA、ALICE 都是规则阶段 |
| 36 | **D** | Features based on word identity, weights learned |
| 37 | **C** | 否定词改变了整体极性，属 combination features；A 是词形变化，B 是同义词 |
| 38 | **C** | w['bias'] = 0 + y × features['bias'] = 1 × 1 = 1（bias 的权重也是学出来的） |
| 39 | **B** | dev 迭代，test 只在最后评估一次 |
| 40 | **A** | 图像描述任务 X 是图像、Y 是文本 |
| 41 | **A** | 同音串歧义，属语音学/音系学层面 |
| 42 | **D** | "金沙"= 赌场，需要世界知识 |

---


> 只覆盖 NLP 正文（P10–P75），不含课程事务与政策。

**题目**

1. All natural languages share the following properties EXCEPT:
   A. language systematics B. conventional and arbitrary word assignment C. redundancy D. invariance over time
2. "Redundancy" in natural language means: A. information is often signaled in more than one way B. one word has several meanings C. sentences can be arbitrarily long D. languages borrow words from each other
3. The division of "disconnect" into [dis-kə-ˈnekt] is a matter of: A. phonology / syllable structure B. morphology C. syntax D. semantics
4. The Turkish word "uygarlastiramadiklarimizdanmissinizcasina" is used to show: A. the importance of world knowledge B. how many morphemes one word can carry, requiring morphological analysis C. that Turkish has no syntax D. that translation is impossible
5. "I made her duck" can mean "I cooked waterfowl belonging to her" or "I caused her to quickly lower her head." The key difference is: A. "duck" is a noun in one reading and a verb in the other B. "make" is a noun in one reading C. the sentence is ungrammatical D. it is only a pragmatic ambiguity
6. Which reading of "I made her duck" is explained by lexical semantics rather than lexical category? A. I caused her to lower her head B. I cooked waterfowl belonging to her C. I made the (plaster) duck statue she owns D. I asked her about the duck
7. "Quick! Fire!" and "He's got a knife!" are used to illustrate: A. phonology B. morphology C. pragmatics D. semantics
8. Turn taking and the thread of meaning belong to which level? A. syntax B. semantics C. pragmatics D. discourse
9. Which belongs to "Analyze/Understand Language" rather than aiding communication? A. text translation B. speech synthesis C. parsing a sentence into its syntactic structure D. dialog systems
10. The deep-learning era (2014–now) is characterized by: A. intent recognition based on keywords B. intent recognition based on syntax analysis C. semantic feature extraction D. hand-written transfer rules
11. Which system is matched with the WRONG year? A. Georgetown-IBM — 1954 B. ELIZA — 1965 C. SHRDLU — 1968 D. ALICE — 2015
12. In the framework Y = f(X), which task has Y = linguistic structure? A. classification B. analysis (parsing) C. translation D. language modeling
13. Which method requires NO data at all (the "based on intuition" row)? A. fine-tuning B. prompting with rigorous evaluation C. supervised learning D. rules or prompting based on intuition
14. "Rules/prompting based on spot-checks" require: A. a small amount of data with input X only B. a full training set with X and Y C. no data at all D. a held-out test set
15. For fine-tuning, when the data size doubles: A. accuracy always doubles B. accuracy decreases C. accuracy usually increases by a constant amount D. nothing changes
16. In the three-step prediction process, `h = f(x)` corresponds to: A. score calculation B. feature extraction C. decision function D. error analysis
17. In the three-step prediction process, `Y = predict(s)` corresponds to: A. feature extraction B. score calculation C. decision function D. training
18. In the rule-based sentiment classifier, which of the following is a FEATURE? A. good_word_count B. Positive C. 2.5 D. 1.0
19. Which is TRUE about the 'bias' feature? A. it equals 1 only for neutral sentences B. it equals 1 for every input C. it is learned from data D. it counts neutral words
20. The classifier predicts Neutral (0) only when: A. the numbers of good and bad words are equal B. the sentence is short C. the bias is removed D. the total score is exactly 0
21. Accuracy is computed as: A. correct predictions / total predictions B. total predictions / correct predictions C. errors / total predictions D. correct predictions − errors
22. In the lecture's error analysis, "…special effects are both listless." and "How inept is Serving Sara?" were both: A. correctly predicted negative B. predicted positive although they are negative C. labeled neutral D. mislabeled by the annotator
23. The recommended fix for the rare-word problem is to: A. use more training data only B. lower the bias weight C. remove rare words from the vocabulary D. incorporate external resources such as sentiment dictionaries
24. "This one is not nearly as dreadful as expected." is labeled positive to show that: A. dreadfulness is a good thing B. negation can flip polarity, and handling it probably needs syntactic analysis C. morphology is enough D. world knowledge is unnecessary
25. "Has all the depth of a wading pool." is negative; handling it requires: A. morphological analysis B. a bigger word list C. world knowledge D. OCR
26. In bag of words, the sentence representation is obtained by: A. summing the word vectors and taking a dot product with the weights B. concatenating word vectors in order C. parsing into a tree D. counting clauses
27. Which of the following CAN be handled by bag of words? A. negation ("I don't love this movie") B. sentence structure ("interesting story but boring overall") C. individual informative words ("great", "terrible") D. word similarity ("adore" ≈ "love")
28. Structured Perceptron: for an example with gold label y = −1 that was predicted wrong, the weights of its features are: A. increased B. decreased C. always unchanged D. set to zero
29. Compared with the rule-based system, the main change in the neural network model is: A. no features are used B. the score is no longer needed C. the bias term disappears D. complicated functions extract the features instead of hand-written rules
30. Which topic is NOT in the tentative roadmap of the course? A. Optical character recognition (OCR) B. Transformers C. Benchmarks and evaluations D. Word representation and text classification
31. Which NLU stage uses selectional restrictions? A. phonological/morphological analyzer B. syntactic analyzer C. semantic interpreter D. contextual reasoner
32. In the framework Y = f(X), "language modeling" means: A. Y = continue text B. Y = target language C. Y = label D. Y = linguistic structure

**答案**

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 答案 | D | A | A | B | A | C | C | D | C | C | D | B | D | A | C | B |

| 题 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 答案 | C | A | B | D | A | B | D | B | C | A | C | B | D | A | C | A |

**解析要点**

- 1：自然语言四性——系统性、约定任意性、冗余性、**演变性**（"不变"是错的）。
- 4：土耳其语例子说明一个词可含大量**语素（morpheme）**，需要形态分析。
- 5/6：duck 名/动 → 词性歧义；make = create/cook → 词义歧义。
- 11：ALICE 是 **1995**，不是 2015。
- 13：凭直觉的规则/提示**不需要数据**，但也没有性能保证。
- 14：抽查式只用**少量只有 X（没有 Y）**的数据。
- 15：数据量翻倍，准确率**通常稳定提升一个常量**。
- 18：特征是可用于判断的输入属性（good_word_count）；Positive 是标签，2.5 是分数，1.0 是权重。
- 20：三分类靠**总分与 0 比较**，score = 0 才判中性（好词数=坏词数时还有 bias 的 0.5，会判成正面）。
- 22：两个例句真实标签 −1 却预测成 1，因为 listless、inept 不在词表里。
- 25：隐喻（"像戏水池一样浅"）需要**世界知识**。
- 28：`w[f] += y × f_value`，y = −1 时权重被往负方向推。
- 29：神经网络的关键是**用复杂函数自动抽特征**，取代人工写规则。
