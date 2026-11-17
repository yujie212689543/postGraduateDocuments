# AHGC7315 Final Exam｜08 Semantics（语义学）

> **优先级：最高。** 老师明确提示 Final Exam 重点考 **Syntax** 与 **Semantics**。
>
> **这一章到底学什么：** 一个词/一句话为什么有这种意思？词与词是什么关系？句子之间什么时候一定互相推出？谁在动作中扮演什么角色？
>
> **来源：** `Semantics.pdf`，P1–P51。★ 越多，越应优先掌握。

## 一张考试地图

| 必会能力 | 典型问法 | 核心区别 | 页码 |
|---|---|---|---|
| 1. 用 compositionality 解释句义 | 句子意义从哪里来？ | words + syntactic structure | P2–4 |
| 2. 判断 entailment / paraphrase / contradiction ★★★ | A 真是否保证 B 真？ | 单向蕴含 vs 双向蕴含 | P5–6 |
| 3. 识别 anomaly / metaphor / idiom | 为什么“不合常理”仍有解释？ | 语义冲突 vs 隐喻 vs 整体习语义 | P7–11 |
| 4. 区分 reference 与 sense ★★ | 同一人为什么有不同说法？ | 现实对象 vs 表达内含意义 | P13–19 |
| 5. 判断 lexical relations ★★★ | synonym / homonym / polysemy 怎么分？ | meaning、spelling、sound | P20–28 |
| 6. 判断四种 antonym | 是“非此即彼”还是有程度？ | complementary / gradable / relational / autoantonym | P22–24 |
| 7. 区分 semantic features 与 word embedding | 0/1 属性还是连续向量？ | 人工可解释特征 vs 学习得到数值特征 | P29–38 |
| 8. 标 thematic roles ★★★ | subject 一定是 Agent 吗？ | Agent / Theme / Goal / Source / Location / Instrument / Experiencer | P40–51 |

---

## 1. Compositional semantics（组合语义）

### 1.1 人话解释

句子的意思像搭 LEGO：

```text
句义 = 每个词的意义 + 它们按什么句法结构组合
```

例：

```text
car + key → car key
```

你不需要提前背过 `car key`，仍能由 `car`、`key` 和名词修饰结构推出它是“车钥匙”。

**所以 Semantics 与 Syntax 不是两件无关的事。** 同样几个词，若它们在 tree 中先和不同的词组合，最后的意义也会不同。

### 1.2 非组合性：三种例外

#### Semantic anomaly（语义异常）

句子语法没问题，但词义搭配违反常识或选择限制：

```text
Colorless green ideas sleep furiously.
```

问题不在句法，而在 `colorless + green`、`ideas sleep` 等语义组合异常。

#### Metaphor（隐喻）

表面看似 anomaly，但借现实知识可以理解其隐藏意义：

```text
Time is money.
Walls have ears.
```

理解 metaphor 需要三样东西：

1. 每个词的字面意义；
2. 整句的字面意义；
3. 关于世界的知识。

#### Idiom（习语）

整体意思不能从单词意义直接相加：

```text
drop the ball = make a mistake
put his foot in his mouth = say something embarrassing
hit it off = become friendly immediately
```

`idiom` 不是“语法错误”，而是组合规则不再按字面逐词套用。

---

## 2. Entailment（蕴含）：最常考的推理关系 ★★★

### 2.1 定义

**A entails B** 的意思是：

```text
只要 A 是真的，B 就一定是真的。
```

但反过来不一定：

```text
Jack swims beautifully.
⇒ Jack swims.                    ✓

Jack swims.
⇒ Jack swims beautifully.        ✗
```

为什么第二个不能推出？因为 Jack 可能在游泳，但游得不漂亮。

### 2.2 三种关系放在一起

| 关系 | 判断 | 课件例子 |
|---|---|---|
| **Entailment（单向蕴含）** | A 真 → B 真；B 真不保证 A 真 | *Jack swims beautifully* → *Jack swims* |
| **Synonymy / paraphrase（同义/释义）** | A 蕴含 B **且** B 蕴含 A | *postponed the meeting* = *put off the meeting* |
| **Contradiction（矛盾）** | A 蕴含 NOT B | *Jack is alive* vs *Jack is dead* |

![[AHGC7315-Semantics-P5.png]]

### 2.3 做题时不要靠“感觉相近”

只问一句：

```text
假设 A 已经为真，我能不能保证 B 也一定为真？
```

如果能，就是 entailment。不能，就不是。

---

## 3. Reference（指称）与 sense（意义内容）★★

### 3.1 人话解释

- **Reference（指称）**：语言表达指向现实世界里的哪个对象。
- **Referent（所指对象）**：被指到的那个具体对象。
- **Sense（意义内容）**：不管现实对象是谁，这个表达本身包含什么信息。

例：

```text
Jack
the happy swimmer
that guy
```

如果在某个场合三者都指同一个人，它们可以有同一个 **referent**，但 sense 不同：

- `Jack` 只是名字；
- `the happy swimmer` 额外告诉你“那个人在游泳且快乐”；
- `that guy` 只是远指一个人。

### 3.2 为什么这个区别重要？

```text
Jack swims.
```

不一定能推出：

```text
The happy swimmer swims.
```

因为后一句 subject 额外要求“happy”。**reference 可以相同，sense 不同，因此蕴含关系会改变。**

`No one swims` 没有某个具体现实中的 referent，但它仍然有明确 sense，也仍然可以被理解。

---

## 4. Lexical relations（词汇关系）★★★

### 4.1 一张表分清所有“-onym”

| Term | Meaning（意义） | Spelling（拼写） | Sound（发音） | 例子 |
|---|---|---|---|---|
| **Synonym（同义词）** | same / very similar | different | different | sofa / couch |
| **Antonym（反义词）** | opposite | different | different | alive / dead |
| **Homonym（同形同音异义词）** | different | **same** | **same** | *bark* 狗叫 / 树皮 |
| **Homograph（同形异义词）** | different | **same** | same or different | *dove*（名词）/ *dove*（动词） |
| **Homophone（同音异义词）** | different | same or different | **same** | bear / bare |
| **Heteronym（同形异音异义词）** | different | **same** | **different** | dove `[dʌv]` / dove `[doʊv]` |
| **Heterograph（同音异形异义词）** | different | **different** | **same** | bear / bare |
| **Polysemy（多义）** | **多个相关意义** | same | — | diamond 几何形 / 棒球场 |

### 4.2 用三个问题判断

1. 拼写一样吗？
2. 发音一样吗？
3. 几个意义是相关的，还是明显无关？

最容易考的例子：

| 对比 | 答案 |
|---|---|
| *bear / bare* | **Homophone**：发音相同，拼写不同 |
| *bark*（狗叫 / 树皮） | **Homonym**：拼写、发音都相同而意义不同 |
| *dove* 名词 / *dove* 动词 | **Heteronym**：拼写同，发音不同 |
| *diamond*（形状 / 棒球场） | **Polysemy**：多个意义有概念联系 |

**注意：**课件特别说明，没有任何两个 synonym 在所有语境中都能百分之百互换。

![[AHGC7315-Semantics-P20.png]]

### 4.3 四种 antonym（反义词）

| 类型 | 核心 | 例子 | 判断口诀 |
|---|---|---|---|
| **Complementary pair（互补反义）** | 非此即彼，没有中间态 | alive/dead、present/absent、awake/asleep | NOT A 就等于 B |
| **Gradable pair（等级反义）** | 有程度、可在 scale 上比较 | big/small、hot/cold、happy/sad | 可说 very、somewhat |
| **Relational opposite（关系反义）** | 同一关系的两端，方向相反 | give/receive、buy/sell、teacher/student | 一定有同一个关系里的另一方 |
| **Autoantonym / contranym（自反义词）** | 同一个词可有相反意义 | *dust* shelves（去灰）/ dust cake（撒粉） | 看搭配语境 |

![[AHGC7315-Semantics-P22.png]]

### 4.4 Hypernym 与 hyponym

| 关系 | 意思 | 例子 |
|---|---|---|
| **Hypernym（上义词）** | 更宽泛的类别 | animal、fruit、vehicle |
| **Hyponym（下义词）** | 属于该类别、更具体的词 | dog/cat/bird；apple/banana/cherry |

记忆：

```text
Animal（hypernym）→ dog, cat, bird（hyponyms）
```

![[AHGC7315-Semantics-P28.png]]

---

## 5. Semantic features（语义特征）与 word embedding（词向量）

### 5.1 Semantic features：人能解释的 0/1 属性

一个词的意义可由若干属性组成。例如：

```text
assassin：+human，并且 kills important people
```

| Feature | Cat | Dog |
|---|---:|---:|
| `+animate` | 1 | 1 |
| `+four-legs` | 1 | 1 |
| `+mammal` | 1 | 1 |
| `+feline` | 1 | 0 |
| `+canine` | 0 | 1 |

这类特征由分析者写出，含义通常可以直接解释。课件还指出，noun 的 semantic features 会与 **morphology、syntax、semantics** 互动。

### 5.2 Word embedding：电脑学出来的连续数字

**Word embedding（词向量）**如 Word2Vec、GloVe，会把一个词表示成一串连续数值：

```text
cat  → [0.97, 0.94, 0.89, 0.92, 0.07, ...]
dog  → [0.95, 0.96, 0.88, 0.02, 0.94, ...]
```

它也能表示词义，但每个数字通常不是一个可直接命名的 `+mammal`、`+feline`。

课件原例：

```text
X = king − queen
X ≈ “male”方向
sister + X ≈ brother
```

**考试区别：**

| Semantic features | Word embedding |
|---|---|
| 通常是人工定义、离散 0/1 属性 | 从数据学习、连续向量 |
| 每项大体可解释 | 单个维度通常不可直接解释 |
| `+human`、`+animate` | `[0.97, 0.02, ...]` |

---

## 6. Thematic roles（题元角色）★★★

### 6.1 不要从“主语 / 宾语”直接推角色

**Thematic roles（题元角色，也叫 thematic relations / semantic roles）**描述的是：

```text
动词所描写的事件中，每个参与者和事件是什么语义关系？
```

它不等于 grammatical subject / object。

| Role | 人话理解 | 典型问法 |
|---|---|---|
| **Agent（施事）** | 有意发起事件的人/物 | 谁主动做？ |
| **Theme / Patient（受事）** | 被动作影响、经历变化者 | 谁最直接承受事件？ |
| **Goal（目标）** | 终点、目的地、接受者 | 到哪里 / 给谁？ |
| **Source（来源）** | 起点或来源 | 从哪里来？ |
| **Location（地点）** | 事件发生的位置 | 在哪里发生？ |
| **Instrument（工具）** | 用来完成动作的手段 | 用什么做？ |
| **Experiencer（体验者）** | 接收感觉、情绪、认知的人 | 谁感受到？ |

### 6.2 原例逐个看

| 句子 | 角色标注 |
|---|---|
| *The dog bit the stick.* | dog = **Agent**；stick = **Theme** |
| *The stick was bitten by the dog.* | stick = **Theme**；dog = **Agent** |
| *Mary gave John a book.* | Mary = **Agent**；John = **Goal**；book = **Theme** |
| *He put the coffee on the table.* | he = **Agent**；coffee = **Theme**；table = **Goal** |
| *He opened the door.* | he = **Agent**；door = **Theme** |
| *The key opened the door.* | key = **Instrument**；door = **Theme** |
| *The kids played in the park.* | kids = **Agent**；park = **Location** |
| *She took the key from him.* | she = **Agent**；key = **Theme**；him = **Source** |
| *Many people fear snakes.* | people = **Experiencer**；snakes = **Theme** |

![[AHGC7315-Semantics-P41.png]]

### 6.3 被动语态不改变 thematic role

```text
The dog bit the stick.
Agent     Verb Theme

The stick was bitten by the dog.
Theme      Verb        Agent
```

被动只改变语法位置，事件中“谁做、谁承受”没有变。

### 6.4 三步标角色

1. 先找动词描述的事件；
2. 问谁是有意发起者 → **Agent**；谁最直接受影响 → **Theme**；
3. 再找终点 **Goal**、来源 **Source**、地点 **Location**、工具 **Instrument**、感受者 **Experiencer**。

**最容易错的判断：** 主语不等于 Agent。`The key opened the door` 中 subject 是 `key`，但它是 Instrument。

---

## 7. 高频对比

| 对比 | 一句话区分 |
|---|---|
| **Entailment vs paraphrase** | Entailment 可单向；paraphrase 必须双向 entail |
| **Anomaly vs ungrammaticality** | Anomaly 是意义冲突；ungrammatical 是句法规则不允许 |
| **Reference vs sense** | Reference 指现实对象；sense 是表达自身携带的意义 |
| **Homonym vs polysemy** | Homonym 意义通常无关；polysemy 的多个意义相关 |
| **Complementary vs gradable antonym** | Complementary 没中间状态；gradable 有程度 |
| **Semantic feature vs embedding** | 前者可解释、离散；后者学习得到、连续 |
| **Subject vs Agent** | Subject 是句法位置；Agent 是“有意发起者”的语义角色 |

---

## 8. 10 道英文自测

1. If A entails B, ____.  
   A. B being true guarantees A  
   B. A being true guarantees B  
   C. A and B are antonyms  
   D. A is ungrammatical

2. Which pair is a paraphrase through mutual entailment?  
   A. *alive / dead*  
   B. *Jack swims / Jack swims beautifully*  
   C. *postpone a meeting / put off a meeting*  
   D. *bear / bare*

3. *Time is money* is best described as ____.  
   A. ungrammatical  
   B. a metaphor  
   C. a homonym  
   D. a contradiction

4. Which is an idiom?  
   A. *green car*  
   B. *drop the ball* meaning “make a mistake”  
   C. *happy swimmer*  
   D. *dog bark*

5. *Barack Obama* and *Michelle Obama’s husband* can share the same ____ but differ in ____.  
   A. spelling；sound  
   B. reference；sense  
   C. entailment；contradiction  
   D. hypernym；hyponym

6. Which is a heteronym?  
   A. *bear / bare*  
   B. *bark*（dog sound / tree skin）  
   C. *dove* `[dʌv]` / *dove* `[doʊv]`  
   D. *sofa / couch*

7. Which pair is gradable rather than complementary?  
   A. *alive / dead*  
   B. *awake / asleep*  
   C. *hot / cold*  
   D. *present / absent*

8. In *vehicle → car, bicycle, train*, the hypernym is ____.  
   A. *car*  
   B. *bicycle*  
   C. *train*  
   D. *vehicle*

9. In *The key opened the door*, *the key* is ____.  
   A. Agent  
   B. Theme  
   C. Instrument  
   D. Goal

10. In *Many people fear snakes*, *many people* is ____.  
    A. Experiencer  
    B. Source  
    C. Instrument  
    D. Location

### 答案与一句订正

| 题 | 答案 | 记忆点 |
|---|---|---|
| 1 | **B** | A 真时 B 必真，方向不能倒 |
| 2 | **C** | 同义要双向蕴含 |
| 3 | **B** | 表面异常，借世界知识理解 |
| 4 | **B** | 整体意义不能由单字相加 |
| 5 | **B** | 同一对象，不同意义内容 |
| 6 | **C** | 拼写相同、发音不同 |
| 7 | **C** | 冷热有程度 |
| 8 | **D** | vehicle 是更宽泛类别 |
| 9 | **C** | key 是完成动作的手段 |
| 10 | **A** | people 接收 fear 这一感受 |

---

## 考前最后 3 分钟

1. **句义 = 词义 + syntactic structure。**
2. **A entails B：A 真，B 必真。**
3. **双向蕴含 = paraphrase。**
4. **Metaphor 借世界知识理解；idiom 整句意义不能逐词算。**
5. **Reference 指对象；sense 是表达内含的意义。**
6. **Homonym 同拼同音；heteronym 同拼异音；homophone 同音。**
7. **Polysemy 的多个意义相关。**
8. **Complementary 无中间值；gradable 有程度。**
9. **Semantic features 可解释；embedding 是学习出来的连续向量。**
10. **Thematic roles 看事件关系，不由 subject/object 决定。**

*最后整理：2026-11-17。*
