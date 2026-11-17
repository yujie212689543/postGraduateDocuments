# AHGC7315 Final Exam｜07 Syntax（句法学）

> **优先级：最高。** 老师明确提示 Final Exam 重点考 **Syntax** 与 **Semantics**。
>
> **这一章到底学什么：** 不看句子的“意思是否合理”，只看词怎样组成短语、短语怎样组成句子。核心能力是：判断成分、识别歧义、画/读句法树、区分 complement 与 adjunct、解释移动和主谓一致。
>
> **来源：** `Syntax.pdf`，P1–P65。★ 越多，越应优先掌握。

## 一张考试地图

| 必会能力 | 典型问法 | 关键工具 | 页码 |
|---|---|---|---|
| 1. 判断 grammatical（合语法） | 为什么一句怪话仍合语法？ | word order + phrase structure rules | P2–12 |
| 2. 判断 constituent（成分）★ | 哪一串词是一个整体？ | stand-alone / pronoun replacement / movement | P13–22 |
| 3. 区分两种 ambiguity（歧义）★★ | 为什么会 Chicken 有歧义？ | lexical ambiguity vs structural ambiguity | P23–28 |
| 4. 画 phrase structure tree（短语结构树）★★★ | 给句子画树 | `S → NP VP` 等规则 | P29–41 |
| 5. 区分 head / specifier / complement / adjunct ★★★ | “the mother of…”里谁是什么？ | 短语内部结构 | P42–54 |
| 6. 理解 X-bar 与语序 | English 与 Japanese 为何树形相反？ | head-initial / head-final | P48–57 |
| 7. 解释问句移动 | 助动词为什么跑到句首？ | T-to-C movement、trace、do-support | P58–63 |
| 8. 解释主谓一致 | verb 跟最近的 noun 还是真正的 subject？ | structure-dependent rule | P60–63 |

---

## 1. Syntax：一句话的人话解释

**Syntax（句法学）**研究的是：**词和短语必须按什么规则组合，才能成为该语言允许的句子。**

人脑并不是把所有句子都背下来。规则数量有限，但可以组合出无限多句子：

```text
Snorlax is asleep.
Everybody knows that Snorlax is asleep.
Everybody knows that everybody knows that Snorlax is asleep.
```

这种“规则套规则”的能力叫 **recursion（递归）**，是句子可以无限变长的原因。

### 1.1 Grammatical ≠ meaningful ★

| 句子 | 判断 | 理由 |
|---|---|---|
| *Colorless green ideas sleep furiously.* | **grammatical（合语法）** | 词序和结构都符合 English rules；只是意思荒谬 |
| `*Furiously sleep ideas green colorless.` | **ungrammatical（不合语法）** | 词序违反 English rules |

所以考试看到“奇怪、无意义”不要立刻判 ungrammatical。先分别回答两件事：

1. **语法问题：** 词序和组合规则对不对？
2. **语义问题：** 意义是否符合常识或选择限制？

`*` 表示 **ungrammatical / ill-formed（不合语法）**；`!` 表示 **semantic anomaly（语义异常）**。

### 1.2 Word order（基本语序）

| 类型 | 顺序 | 例子 | 常见语言 |
|---|---|---|---|
| **SVO** | Subject–Verb–Object | *Sam ate apples.* | English、多数欧洲语言 |
| **SOV** | Subject–Object–Verb | *Sam apples ate.* | Korean、Japanese |
| **VSO** | Verb–Subject–Object | *Ate Sam apples.* | 部分 Celtic、Filipino |

**Mandarin（普通话）**的基本语序看起来是 **SVO**：

```text
我 买 书 了。
```

但普通话也是 **topic-prominent language（话题突出语言）**。已知信息可以放到句首当 **topic（话题）**，后面是 **comment（评述）**：

```text
书，我买了。
[topic] [comment]
```

考试只需记住：**Mandarin 不是“随便乱序”，而是常用话题—评述结构。**

---

## 2. Constituent（成分）：哪些词是一个整体？★★

**Constituent（成分）**是句子里自然抱成一团、在树中由同一个 node 支配的一串词。

例：

```text
[The child] [found [a puppy]].
```

这里：

- `the child` 是一个 NP；
- `a puppy` 是一个 NP；
- `found a puppy` 是一个 VP。

### 2.1 三种 constituency tests（成分测试）

课件给出三种方法。按课件标准，一串词满足其中至少一种，就可以视为 constituent。

| 测试 | 怎么问 | 例子 | 结论 |
|---|---|---|---|
| **Stand-alone（独立回答）** | 能否单独回答 wh-question？ | —What did the child find? —*A puppy.* | `a puppy` 是成分 |
| **Replacement（替换）** | 能否用 pronoun / there / here 代替？ | *The child found **it**.* | `a puppy` 是成分 |
| **Movement（整体移动）** | 整串一起移动后句子仍合语法？ | *In the garden the puppy played.* | `in the garden` 是成分 |

原句：

```text
The puppy played in the garden.
```

对 `in the garden` 做三次检查：

1. *Where did the puppy play? — In the garden.*
2. *The puppy played there.*
3. *It was in the garden that the puppy played.*

三种都通过，因此它明显是一个 **PP（介词短语）**。

![[AHGC7315-Syntax-P15.png]]

### 2.2 易错点

- 两个词相邻，不代表它们就是一个 constituent。
- `ran out of gas` 中，`out of gas` 与格，`out of` 常常可以一起移动或替换；但判断仍应做测试，不能只看空格和停顿。
- Pronoun replacement 只能检验某些类型。`there` 往往替换地点 PP，`it` 可替换 NP。

---

## 3. Ambiguity（歧义）：一个词多义，还是一种结构有两种树？★★

### 3.1 Lexical ambiguity（词汇歧义）

一个词或短语本身有多个 dictionary meanings。

```text
We saw her duck.
```

两种意思：

1. 我们看见她的鸭子；
2. 我们看见她低头躲避。

差别来自 **duck**：名词“鸭子” vs 动词“躲避”。

### 3.2 Structural ambiguity（结构歧义）

词义不变，但词串可以组成两种不同结构：

```text
Sue saw the man with the telescope.
```

意思一：Sue 用望远镜看那个男人。

```text
Sue [saw the man] [with the telescope]
                       ↑ PP 修饰 VP
```

意思二：Sue 看见那个带着望远镜的男人。

```text
Sue saw [the man [with the telescope]]
                   ↑ PP 修饰 NP
```

**判断口诀：先问 PP 修饰谁。**

- 修饰动作 → VP 里的 adjunct；
- 修饰名词 → 挂到 NP 里面。

![[AHGC7315-Syntax-P25.png]]

---

## 4. Syntactic categories（句法范畴）

### 4.1 词的类别

| 类别 | 全称 | 例子 |
|---|---|---|
| **N** | Noun（名词） | puppy, girl, happiness |
| **V** | Verb（动词） | find, run, sleep, realize |
| **P** | Preposition（介词） | in, on, with, from |
| **A** | Adjective（形容词） | red, lucky, large |
| **Adv** | Adverb（副词） | carefully, very, again |
| **Det** | Determiner（限定词） | a, the, this, every |
| **T** | Tense（时态/情态助动词） | will, can, might |
| **C / Comp** | Complementizer（补语标记） | that, if, whether |

### 4.2 短语类别

| 短语 | 最简单的识别方法 |
|---|---|
| **NP（名词短语）** | 整体功能像名词，如 `the man of her dreams` |
| **VP（动词短语）** | 整体功能像动词，如 `found the cake in the cupboard` |
| **PP（介词短语）** | 以 preposition 开头，如 `in the cupboard` |
| **AdjP（形容词短语）** | 整体功能像 adjective，如 `very proud of her children` |
| **AdvP（副词短语）** | 整体功能像 adverb，如 `very carefully` |

**考试最先看开头词：** PP 必须从 P 开始；`the cupboard` 是 NP，`in the cupboard` 才是 PP。

---

## 5. Phrase structure tree（短语结构树）★★★

### 5.1 句法树同时表达三件事

1. **Linear order（线性顺序）：** 谁在谁前面；
2. **Syntactic categories（句法范畴）：** 这是 N、V、NP 还是 VP；
3. **Hierarchical structure（层级结构）：** 哪些词先组成小组，再组成更大的组。

### 5.2 基本规则

```text
S  → NP VP
NP → Det N
VP → V NP
VP → V PP
PP → P NP
CP → C S
V  → V CP
```

`→` 读作 **consists of / is rewritten as / is composed of（由……组成）**。

原句：

```text
The sheepdog rolled in the mud.
```

规则匹配：

```text
S
├── NP
│   ├── Det: the
│   └── N: sheepdog
└── VP
    ├── V: rolled
    └── PP
        ├── P: in
        └── NP
            ├── Det: the
            └── N: mud
```

### 5.3 画树不要猜：按这个顺序做

1. 找主要动词 V。
2. 找动词后必须与它组合的 NP 或 PP。
3. 先圈最容易识别的 PP：看到 preposition，就圈到它的 NP 结束。
4. 圈出主语 NP。
5. 用 `S → NP VP` 搭最外层。
6. 每加一条线，都要能说出一条例句规则。

例：

```text
The puppy found the child.
```

| 步骤 | 操作 | 结果 |
|---|---|---|
| 1 | 找主要 V | `found` |
| 2 | 找宾语 | `the child` = NP |
| 3 | 动词 + 宾语 | `found the child` = VP |
| 4 | 找主语 | `the puppy` = NP |
| 5 | 套句子规则 | `S → NP VP` |

![[AHGC7315-Syntax-P37.png]]

### 5.4 Tree 的关系词

| 关系 | 意思 |
|---|---|
| **dominates（支配）** | 高 node 包含下面所有 node |
| **immediately dominates（直接支配）** | 上下直接连一条线 |
| **sisters（姐妹节点）** | 被同一个 mother node 直接支配 |

---

## 6. Phrase 内部：head、specifier、complement、adjunct ★★★

以 NP 为例：

```text
the mother of James Whistler
 ↑     ↑       ↑
Spec  Head   Complement
```

| 成分 | 人话理解 | 是否必需 |
|---|---|---|
| **Head（中心语）** | 短语的“主角” | **必需，且通常只有一个** |
| **Specifier（标示语）** | 在 head 前，限定或指向它，如 `the` | 可选 |
| **Complement（补足语）** | 紧贴 head，把 head 的意思补完整 | 可选，但若动词需要宾语就很重要 |
| **Adjunct（附加语）** | 时间、地点、方式等额外信息 | 可选，可出现多个 |

### 6.1 Complement 与 adjunct 的直白区别

问两个问题即可：

1. **删掉后，head 的意思还完整吗？**
2. **它是在完成 head 的核心需要，还是只是补充额外信息？**

| 句子 | 成分 | 判断 |
|---|---|---|
| *I loved **the policeman**.* | complement | `love` 需要知道“爱谁” |
| *I loved the policeman **intensely**.* | adjunct（manner） | 删掉后仍是完整句子 |
| *I loved the policeman **with all my heart**.* | adjunct | 额外信息，可删、可移动 |
| *the mother **of James Whistler*** | complement | 说明“谁的母亲” |

课件还强调 English 的顺序：

```text
I loved [the policeman] [intensely] [with all my heart].
        complement       adjunct      adjunct
```

通常不能写成：

```text
*I loved intensely the policeman with all my heart.
```

![[AHGC7315-Syntax-P43.png]]

### 6.2 C-selection 与 S-selection

| 概念 | 在问什么 | 例子 |
|---|---|---|
| **Category-selection / C-selection（范畴选择）** | head 允许接哪一类 syntactic category？ | `blow` 可接 NP：*The wind blew the kite.*；`sleep` 不能：`*Michael slept an afternoon.` |
| **Semantic-selection / S-selection（语义选择）** | subject / complement 的意义是否讲得通？ | `!The beer drank the student.` 中 `beer` 不能做有意的 drinker |

一句话：句子 well-formed 必须同时通过：

```text
word order / PS rule  +  C-selection  +  S-selection
```

---

## 7. X-bar theory（X′ 理论）

普通 PS rule 需要写很多条。X-bar theory 说：所有短语其实都有同一套三层模板。

```text
XP
├── Specifier
└── X′
    ├── X′
    │   ├── X (Head)
    │   └── Complement
    └── Adjunct
```

| 节点 | 位置关系 | 人话理解 |
|---|---|---|
| **Head X** | 最底层核心 | 这个短语到底在说名词、动词、介词还是形容词 |
| **Complement** | sister to X，daughter of X′ | 动词的宾语、介词的宾语等“完成 head 意义”的部分 |
| **Adjunct** | sister to X′，daughter of X′ | 可删、可反复添加的时间/地点/方式信息 |
| **Specifier** | sister to X′，daughter of XP | 位于较高层，限定 head |

课件规则可以概括成：

```text
一个 phrase：通常 1 个 specifier、1 个 complement，但可以有无限多个 adjunct
```

![[AHGC7315-Syntax-P50.png]]

### 7.1 Head-initial 与 head-final

| 类型 | 结构 | 语言 | 表面现象 |
|---|---|---|---|
| **head-initial / right-branching（中心语在前）** | `XP → X Complement` | English、Mandarin | VO；Preposition + NP |
| **head-final / left-branching（中心语在后）** | `XP → Complement X` | Japanese、Korean | OV；NP + Postposition |

English：

```text
VP → V NP
     ↑ head 在前
```

Japanese：

```text
VP → NP V
          ↑ head 在后
```

注意：这里比较的是 **head 与 complement 的相对顺序**，不要把它和 topic-prominent 混淆。

---

## 8. Sentence 的 head：Tense（时态）

课件把 sentence 看成 **TP（Tense Phrase）**：

| 位置 | 内容 | 例子 |
|---|---|---|
| Head | **T（tense marker / modal）** | `will`, `can`, `may`, `-ed` |
| Specifier | **Subject（主语）** | `the child` |
| Complement | **Predicate（谓语）** | `ate` |

可理解为：

```text
TP / S
├── Specifier: Subject
└── T′
    ├── Head: T
    └── Complement: Predicate
```

Tense 提供事件发生的时间框架，所以所有完整 finite sentence 都离不开 T。

---

## 9. Yes–no question 与 wh-question

### 9.1 Yes–no question（一般疑问句）

把 **T / auxiliary（时态助动词）** 从原来的 T 位置移到句首：

```text
Basic:   The puppy will find the child.
Question: Will the puppy [trace] find the child?
```

不能说：

```text
*Find the puppy the child?
```

因为移动的是 auxiliary，不是主要动词 `find`。

如果没有 overt auxiliary，就使用 **do-support（do 支持）**：

```text
The puppy found the child.
→ Did the puppy find the child?
```

`did` 承担过去时；主要动词 `found` 回到原形 `find`。

### 9.2 Wh-question（特殊疑问句）

两步：

1. 把要问的成分换成 `who / what / where / when`；
2. 把 auxiliary 移到 wh-word 后面。

```text
The puppy found the child.
→ The puppy found who?
→ Who did the puppy find [trace]?
```

如果 wh-word 本身就是 subject，不做 do-support：

```text
Who found the child?
```

不是：

```text
*Who did find the child?
```

---

## 10. Structural dependency（结构依赖）与主谓一致 ★★

### 错误规则：linear agreement

“动词跟左边最近的 noun 一致”是错的。

反例：

```text
The guy sitting behind those tables seems kind of cute.
```

| 候选词 | 为什么不能控制 verb |
|---|---|
| `tables` | 虽然离 `seems` 较近，但只是 PP 里的 noun |
| `guy` | 是句子的 subject，因此 `seems` 用单数 |

正确规则是 **structure-dependent agreement（结构依赖一致）**：

```text
动词与 S / TP 直接支配的 subject NP 一致。
```

再比较：

```text
This guy seems kind of cute.
These guys seem kind of cute.
```

**考试口诀：不看最近，先找主语。**

![[AHGC7315-Syntax-P62.png]]

---

## 11. 高频原例速记

| 原例 | 必须能说出什么 |
|---|---|
| *Colorless green ideas sleep furiously.* | grammatical but semantically anomalous |
| *Sue saw the man with the telescope.* | structural ambiguity；PP 可挂 VP 或 NP |
| *The child found a puppy.* | NP/VP constituents；可画树 |
| *The sheepdog rolled in the mud.* | `S → NP VP`、`VP → V PP`、`PP → P NP` |
| *the mother of James Whistler* | Specifier–Head–Complement |
| *I loved the policeman intensely with all my heart.* | complement + two adjuncts |
| *The guy behind those tables seems cute.* | 与 `guy` 一致，不与 `tables` 一致 |
| *The horse raced past the barn fell.* | 对应下一章 Garden Path；PP attachment 与 reanalysis |

---

## 12. 10 道英文自测

1. Which sentence is grammatical but semantically anomalous?  
   A. *Furiously sleep ideas green colorless.*  
   B. *Colorless green ideas sleep furiously.*  
   C. *Romeo Juliet loves.*  
   D. *Slept the child a puppy.*

2. Korean is most commonly ____.  
   A. SVO  
   B. SOV  
   C. VSO  
   D. VOS

3. In *The child found a puppy*, which string passes the pronoun-replacement test as one constituent?  
   A. *found a*  
   B. *child found*  
   C. *a puppy*  
   D. *a puppy the child*

4. The two readings of *Sue saw the man with the telescope* come from ____.  
   A. homophony  
   B. structural ambiguity  
   C. antonymy  
   D. inflection

5. Which phrase must start with a preposition?  
   A. NP  
   B. VP  
   C. PP  
   D. AdjP

6. Which rule produces *the puppy*?  
   A. `NP → Det N`  
   B. `VP → V NP`  
   C. `PP → P NP`  
   D. `S → V NP`

7. In *the mother of James Whistler*, the head is ____.  
   A. *the*  
   B. *mother*  
   C. *of*  
   D. *James Whistler*

8. In *I loved the policeman intensely*, the direct object is the ____.  
   A. subject  
   B. complement  
   C. adjunct  
   D. specifier

9. `*Michael slept an afternoon.` mainly violates ____.  
   A. C-selection  
   B. structural ambiguity  
   C. word embedding  
   D. phonotactics

10. In *The guy behind those tables seems kind*, the verb agrees with ____.  
    A. *tables*  
    B. the nearest noun  
    C. *guy*  
    D. *kind*

### 答案与一句订正

| 题 | 答案 | 记忆点 |
|---|---|---|
| 1 | **B** | 语法和意义分开判断 |
| 2 | **B** | Korean 是 SOV |
| 3 | **C** | `a puppy` 可替换为 `it` |
| 4 | **B** | 同一个词串，两种 PP attachment |
| 5 | **C** | PP 必须从 P 开始 |
| 6 | **A** | `the + puppy` = Det + N |
| 7 | **B** | 短语核心是 `mother` |
| 8 | **B** | direct object 是 VP complement |
| 9 | **A** | `sleep` 的选择限制不允许接 NP |
| 10 | **C** | agreement 看结构上的 subject |

---

## 考前最后 3 分钟

1. **Grammatical 看规则；meaningful 看语义。**
2. **Constituent 靠三项测试，不靠“看起来像一组”。**
3. **Lexical ambiguity 是词多义；structural ambiguity 是结构有两种。**
4. **PP 挂哪里最关键：挂 VP 是动作信息，挂 NP 是名词信息。**
5. **PP 一定从 P 开始。**
6. **画树先找 V，再找 NP/PP，最后由 `S → NP VP` 往下补。**
7. **Head 必需；specifier、complement、adjunct 可选。**
8. **Complement 完成核心意义；adjunct 可删、可多。**
9. **English 是 head-initial；Japanese/Korean 是 head-final。**
10. **主谓一致永远找真正的 subject，不找最近 noun。**

*最后整理：2026-11-17。*
