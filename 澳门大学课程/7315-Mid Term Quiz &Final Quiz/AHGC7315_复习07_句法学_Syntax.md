# AHGC7315 考前复习 07｜Syntax（句法学）：句子结构、树状图与 X-bar

> **考试重点**：Syntax。要会判断 grammaticality、constituent、structural ambiguity、phrase category；尤其会画/读 **phrase structure tree（短语结构树）** 与 **X-bar tree（X-bar 树）**。
>
> **材料依据**：Syntax 课件 P1–65。★ = 高概率考点。

## 先背这 12 句（考前最后 3 分钟）

1. **Syntax（句法）** = 关于句子及其结构的 grammar knowledge；有限规则能产生无限句子。
2. **Grammatical（合语法）** 不等于 meaningful（有意义）：*Colorless green ideas sleep furiously* 是 grammatical 但语义异常。
3. English 的基本语序是 **SVO**；Korean/Japanese 常为 **SOV**；Mandarin 是 **topic-prominent（话题突出）**。
4. **Constituent（成分）** 是自然成组的词；用 stand-alone、pronoun replacement、movement 检验。
5. **Lexical ambiguity（词汇歧义）** 来自一个词的多义；**structural ambiguity（结构歧义）** 来自两种树形结构。
6. **NP, VP, PP, AdjP, AdvP** 都是 phrase（短语）；PP 必须从 P 开始。
7. 基本规则：**S/TP → NP VP；NP → Det N；VP → V NP；PP → P NP**。
8. 每个 phrase 的 **head（中心语）** 必有；**specifier（标示语）** 与 **complement（补足语）** 可选；**adjunct（附加语）** 可有无限多个。
9. Complement 是 head 需要来完成意义的成分；adjunct 只是可删的时间/地点/方式等额外信息。
10. English/Mandarin 是 **head-initial / right-branching（中心语在前/右分叉）**；Japanese/Korean 是 **head-final / left-branching（中心语在后/左分叉）**。
11. Yes–no question 把 **T/auxiliary（时态/助动词）**移到句首；wh-question 再把要问的 constituent 换成并移成 **wh-word**。
12. **Deep structure（深层结构）**保留谁对谁做什么的基本关系；movement 后得到表面的 **surface structure（表层结构）**。主谓一致仍看 tree，不看最近的 noun。

## 1. Syntax、语法性与语序（P2–12）

### 1.1 Syntax 的核心

**Syntax（句法）**是 grammar 中关于 sentence（句子）及其 structure（结构）的知识。人脑里是 **finite rules → infinite sentences（有限规则 → 无限句子）**，所以不可能靠死记所有句子。

| 判断 | 例子 | 为什么 |
|---|---|---|
| grammatical but odd | *Colorless green ideas sleep furiously.* | 词序和结构合规则，但意义奇怪 |
| ungrammatical | \*Furiously sleep ideas green colorless. | 违反 English word-order rule |

> `*` = **ungrammatical / ill-formed（不合语法）**；`!` = **semantic anomaly（语义异常）**，两者不要混淆。

### 1.2 Word order（语序）★

| 类型 | 顺序 | 例子 | 课件信息 |
|---|---|---|---|
| **SVO** | Subject–Verb–Object | *Romeo loves Juliet.* | English；约 42% 语言 |
| **SOV** | Subject–Object–Verb | “Ting a burger ate.” | Korean/Japanese；约 45% |
| **VSO** | Verb–Subject–Object | “Ate Sam apples.” | 约 9% |

**Mandarin（汉语）**表面基本为 SVO：`我 买 书 了`；但它也是 **topic-prominent language（话题突出语言）**，可将已知话题前置：`书 我 买 了`。结构是 **topic + comment（话题 + 评述）**，不是随意乱序。

---

## 2. Constituents（成分）与三种检验（P13–22）★

**Constituent（成分）** = tree 中的一个 branch / natural grouping，即由一个 node 支配的一组词。

例：*The child found a puppy.*

```text
[The child] [found [a puppy]]
    NP             VP
                 V    NP
```

![[AHGC7315-Syntax-P15.png]]

### 2.1 三种 constituency tests

只要满足至少一种，通常就可视为 constituent。

| 检验 | 做法 | 例子 | 结论 |
|---|---|---|---|
| **Stand alone（独立回答）** | 用 wh-question 问出该串词 | *What did the child find? — A puppy.* | `a puppy` 是 NP |
| **Replacement（代词替换）** | 用 pronoun / here / there 替换 | *The child found it.* | `it` 替代 `a puppy` |
| **Movement（整体移动）** | 整串移动仍 grammatical | *In the garden, the puppy played.* | `in the garden` 是 PP |

例：*The puppy played in the garden.*

- `Where did the puppy play? — In the garden.`
- `The puppy played there.`
- `It was in the garden that the puppy played.`

**易错点：**字面连续不等于 constituent。`ran out of` 在 *We ran out of gas* 中可和 `gas` 构成 VP 的一部分；具体要用 test，不要凭停顿猜。

---

## 3. Ambiguity（歧义）与树（P23–28）★

| 类型 | 来源 | 例子 | 两种意思 |
|---|---|---|---|
| **Lexical ambiguity（词汇歧义）** | 一个 word/phrase 多义 | *We saw her duck.* | 看见她的鸭子 / 看见她低头躲避 |
| **Structural ambiguity（结构歧义）** | 同一词串有两种 constituent structure | *Sue saw the man with the telescope.* | Sue 用望远镜看；男人带着望远镜 |

在 *Sue saw the man with the telescope* 中，PP `with the telescope`：

1. attach 到 **VP**：`[saw … with the telescope]` → Sue 用它看。
2. attach 到 **NP**：`[the man with the telescope]` → 男人带着它。

![[AHGC7315-Syntax-P25.png]]

**画歧义树的口诀：先问 PP 修饰谁。** 修饰动作 → VP adjunct；修饰名词 → NP 内的 adjunct/complement。

---

## 4. Syntactic categories（句法范畴）与基础树（P29–40）★

### 4.1 必背类别

| 类别 | 全称 | 例子 |
|---|---|---|
| **N** | Noun（名词） | puppy, happiness |
| **V** | Verb（动词） | find, sleep, realize |
| **P** | Preposition（介词） | in, with, from |
| **A** | Adjective（形容词） | red, lucky |
| **Adv** | Adverb（副词） | carefully, very |
| **Det** | Determiner（限定词） | a, the, this, every |
| **T** | Tense（时态；含 modal auxiliary） | will, can, might |
| **C / Comp** | Complementizer（补语标记） | that, if, whether |

| Phrasal category（短语范畴） | 核心 / 识别法 | 例子 |
|---|---|---|
| **NP** | functions as noun | *the man of her dreams* |
| **VP** | functions as verb | *found the cake in the cupboard* |
| **PP** | **starts with P** | *in the cupboard* |
| **AdjP** | functions as adjective | *very proud of her children* |
| **AdvP** | functions as adverb | *very carefully* |

### 4.2 Phrase structure rules（短语结构规则）

```text
S  → NP VP
NP → Det N
VP → V NP
VP → V PP
PP → P NP
CP → C S
V  → V CP
```

箭头 `→` 可读成 **consists of / is rewritten as / is composed of（由……构成）**。

例：*The sheepdog rolled in the mud.*

```text
S
├── NP → Det the + N sheepdog
└── VP → V rolled + PP
                 └── P in + NP → Det the + N mud
```

![[AHGC7315-Syntax-P37.png]]

Tree 要表达三件事：**linear order（线性顺序）**、**category（范畴）**、**hierarchical structure（层级结构）**。

**关系术语：**高 node **dominates（支配）**下方所有 node；直接支配是 **immediately dominates**；同一个 mother 下的两个 node 是 **sisters（姐妹节点）**。

### 4.3 树状图其实在画什么？白话四步法 ★★★

把句子想成一堆**套盒子**，不是把每个词排成一排：先把自然成组的词放进小盒子（NP/VP/PP），再把小盒子放进句子的大盒子（S/TP）。**一根线只说明“这个词/短语属于那个盒子”。**

例句：`The puppy found the child.`

**第 1 步：先找动词。** `found` 是 V；它后面“找到谁”是 `the child`，所以先圈 `[found the child]` = VP。

**第 2 步：找名词短语 NP。** `the puppy` 是一个“谁” → NP；`the child` 是一个“谁” → NP。`the` 不可单独当 NP，它和名词绑在一起。

**第 3 步：先摆最简单骨架。** 英语陈述句最常用 `S → NP VP`。把主语 NP 放左，VP 放右。

```text
S                         读法：一个句子 S
├── NP                    左边是主语 NP
│   ├── Det  The          NP 里面：Det + N
│   └── N    puppy
└── VP                    右边是谓语 VP
    ├── V    found        VP 里面：V + NP
    └── NP
        ├── Det  the
        └── N    child
```

**第 4 步：用规则检查，不靠猜。** 这棵树逐条满足 `S → NP VP`、`NP → Det N`、`VP → V NP`，所以对。

### 4.4 遇到长句时只做“拆盒子”

例句：`The puppy found the child in the park.`

1. 先得到三个大盒子：`[The puppy]` NP、`[found the child]` VP、`[in the park]` PP。
2. `in the park` 从介词 `in` 开始，所以必定是 **PP → P NP**。
3. 最后才问 PP 挂到哪里：若是“在公园里找到”→ 挂到 VP；若是“那个在公园里的孩子”→ 挂进 object NP。这个不同挂法就是 structural ambiguity。

**考试的稳妥顺序：**先圈 NP → 找 V → 圈 VP → 看到 preposition 就圈 PP → 从 `S → NP VP` 往下补标签。不要一上来就画很复杂的 X′。

![[AHGC7315-TreeGuide-P20.png]]

### 4.5 X-bar 只是在普通树上多看一层

普通树说 `VP → V NP`；X-bar tree 只是把“动词和它必须带的对象先抱成一组”写得更清楚：

```text
VP
└── V′                    V′ = “动词这一小组”
    ├── V  found          head（核心）
    └── NP the child      complement（动词必须/常常需要的对象）
```

若加一个可有可无的地点：`found the child in the park`，`in the park` 是 **adjunct（附加语）**，可以删掉，句子还完整。它挂在较高的 V′ 外面；`the child` 不能随意删（会少“找到谁”），所以它更靠近 V。

**你不必先背一堆 X′ 关系；先能说对“谁和谁先组成一个短语”，再补 X′ 标签。**

---

## 4.6 Transformational rules（转换规则）：把陈述句变问题（考试范围）★★★

**Deep structure（深层结构）**可以先理解为“原本的陈述句骨架”；**surface structure（表层结构）**就是你实际说出来、可能经过 movement（移动）的句子。移动后，原位置常留下 `t` / trace（痕迹）。

### A. Yes–no question（一般疑问句）

口诀：**先找 T/auxiliary，再把它搬到最前面。**

```text
Deep/basic:    The puppy will find the child.
Surface Q:     Will the puppy t find the child?
                         ↑ 原来 will 的位置
```

- `will / can / is / are / has` 这类 T/auxiliary move 到句首。
- 不是把 main verb `find` 搬到句首：`*Find the puppy the child?` ✗
- 没有明显 auxiliary 的简单 present/past，英语用 **do-support**：`The puppy found the child.` → `Did the puppy find the child?`（`did` 到句首，main verb 回 base form `find`）。

### B. Wh-question（特殊疑问句）

口诀：**先把答案位置换成 who/what/where；再把 auxiliary 搬到句首。**

```text
Basic:      The puppy found the child.
Ask object: The puppy found who?
Surface:    Who did the puppy find t?
```

另一个例子：`The puppy slept in the garden.` → `Where did the puppy sleep t?`

| 你要问的成分 | wh-word | 例子 |
|---|---|---|
| 人 | who | Who did the puppy find? |
| 物 | what | What did the puppy find? |
| 地点 | where | Where did the puppy sleep? |
| 时间 | when | When did the puppy sleep? |

**最易错：**wh-word 已经是 subject 时，不做 do-support：`The puppy found the child.` → `Who found the child?`，不是 `*Who did find the child?`。

![[AHGC7315-TreeGuide-P18.png]]

---

## 5. Head、selection 与 X-bar theory（P42–59）★★★

### 5.1 Phrase 的内部

| 成分 | 定义 | `the mother of James Whistler` 中 |
|---|---|---|
| **Head（中心语）** | phrase 的核心；**唯一 obligatory** | `mother` |
| **Specifier（标示语）** | head 前、限定/指明 head | `the` |
| **Complement（补足语）** | 紧邻 head、完成其意义 | `of James Whistler` |
| **Adjunct（附加语）** | optional extra information | time/place/manner PP、adverbs |

![[AHGC7315-Syntax-P43.png]]

### 5.2 C-selection 与 S-selection

| 选择 | 问题 | 例子 |
|---|---|---|
| **Category-selection / C-selection（范畴选择）** | head 需要哪类 complement？ | transitive `blow` 可接 NP：*The wind blew the kite*；intransitive `sleep` 不可接 NP：\*Michael slept an afternoon |
| **Semantic-selection / S-selection（语义选择）** | subject/complement 是否符合 head 的语义要求？ | `drink` 的 agent 要能喝：`!The beer drank the student.` |

一句话：well-formed sentence 同时要过 **PS rule（结构/语序）**、**C-selection（类别）**、**S-selection（意义）** 三关。

### 5.3 X-bar（X′）结构 ★

```text
XP
├── Specifier
└── X′
    ├── X′
    │   ├── X (Head)
    │   └── Complement
    └── Adjunct
```

![[AHGC7315-Syntax-P50.png]]

- **Specifier**：sister of X′，daughter of XP。
- **Complement**：sister of X，daughter of X′；通常一个，直接 object 必为 VP 的 complement。
- **Adjunct**：sister of X′，daughter of X′；可重复。

例：*I loved the policeman intensely with all my heart.*

- `the policeman` = complement（direct object，不能随便移到 V 前后）。
- `intensely`、`with all my heart` = adjunct（可删、可多、可前置）。
- `*I loved intensely the policeman …` 不合课件所示 English order。

### 5.4 Branching 与语序

| 类型 | rule | 语言 |
|---|---|---|
| **head-initial / right-branching（中心语前）** | `XP → X Complement` | English, Mandarin；VO；P + NP |
| **head-final / left-branching（中心语后）** | `XP → Complement X` | Japanese, Korean；OV；NP + postposition |

![[AHGC7315-Syntax-P59.png]]

---

## 6. Tense 与 structural dependency（P58–63）★★

课件将 sentence 视为 **TP（Tense Phrase）**：T（tense marker / modal）是 sentence 的 head；subject 是 TP 的 specifier，predicate 是 complement。

### Subject–verb agreement（主谓一致）

错误的 linear rule：verb 和左边最近的 noun 一致。

正确的 **structure-dependent rule（结构依赖规则）**：verb 与 **TP/S 直接支配的 subject NP** 一致。

| 句子 | 正确 | 原因 |
|---|---|---|
| *This guy seems kind of cute.* | `seems` | subject `guy` singular |
| *These guys seem kind of cute.* | `seem` | subject `guys` plural |
| *The guy sitting behind those tables seems …* | `seems` | 最近 noun 是 plural `tables`，但 subject 是 singular `guy` |

![[AHGC7315-Syntax-P62.png]]

---

## Syntax 自测（10 题）

1. Which sentence is grammatical but semantically anomalous? A. \*Furiously sleep ideas green colorless. B. Colorless green ideas sleep furiously. C. \*Romeo Juliet loves. D. \*Slept the child puppy a.
2. The usual basic word order of Korean is ____. A. SVO B. SOV C. VSO D. VOS
3. In *The child found a puppy*, which is a constituent by pronoun replacement? A. found a B. child found C. a puppy D. found a puppy the
4. The two readings of *Sue saw the man with the telescope* arise from ____. A. homophony B. structural ambiguity C. antonymy D. inflection
5. Which phrase must begin with a preposition? A. NP B. VP C. PP D. AdjP
6. Which rule correctly builds *the puppy*? A. NP → Det N B. VP → V NP C. PP → P NP D. S → V NP
7. In *the mother of James Whistler*, the head of the NP is ____. A. the B. mother C. of D. James Whistler
8. Which item is normally a VP complement in *I loved the policeman intensely*? A. I B. loved C. the policeman D. intensely
9. \*Michael slept an afternoon violates mainly ____. A. C-selection B. structural ambiguity C. word embedding D. phonology
10. In *The guy behind the tables seems kind*, the verb agrees with ____. A. tables B. the nearest noun C. guy D. kind

### 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **B** | **C** | **B** | **C** | **A** | **B** | **C** | **A** | **C** |

---

## 易混淆速查

| 不要混 | 正确区分 |
|---|---|
| grammatical vs meaningful | grammatical 看规则；meaningful 看语义。可 grammatical 但 absurd。 |
| lexical vs structural ambiguity | 前者一个词多义；后者同一词串两种 tree。 |
| complement vs adjunct | complement 完成 head 意义、位置紧；adjunct 是可删的额外信息。 |
| C-selection vs S-selection | C 选 syntactic category；S 选 semantic properties。 |
| closest noun vs subject | 主谓一致找 tree 中的 subject NP，不找最近 noun。 |
