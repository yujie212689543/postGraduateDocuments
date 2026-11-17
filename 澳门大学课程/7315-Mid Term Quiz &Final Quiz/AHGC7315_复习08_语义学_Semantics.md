# AHGC7315 考前复习 08｜Semantics（语义学）：意义、词汇关系与 thematic roles

> **考试重点**：Semantics。优先掌握 **compositionality、entailment、reference vs. sense、lexical relations、semantic features、thematic roles**。
>
> **材料依据**：Semantics 课件 P1–51。★ = 高概率考点。

## 先背这 12 句（考前最后 3 分钟）

1. **Semantics（语义学）**研究 linguistic meaning（语言意义）。
2. **Compositionality（组合性）**：大单位的意义 = 小单位的意义 + 它们的 syntactic structure（句法组合方式）。
3. **Entailment（蕴含）**：A true 时 B 必真；但 B true 时 A 未必真。`Jack swims beautifully` entails `Jack swims`。
4. Mutual entailment = **synonymy / paraphrase（同义/释义）**；A entails not-B = **contradiction（矛盾）**。
5. **Anomaly（语义异常）**句子可能 grammatical 但意义违反常识/选择限制；metaphor（隐喻）可使表面异常变得可理解。
6. **Idiom（习语）**整体意义不可由词义预测，如 *drop the ball* = make a mistake。
7. **Reference（指称）** = form 到现实 referent（所指对象）的映射；**sense（意义内容）** = 除指称外的内在意义。
8. Synonym、antonym、homonym、homograph、homophone、heteronym、polysemy 要按 meaning / spelling / sound 分。
9. **Hypernym（上义词）**更宽泛；**hyponym（下义词）**更具体：animal → dog。
10. **Semantic features（语义特征）**是词义属性，可写成 `+animate` 等；word embedding 是连续数值向量，不等于手写 0/1 特征表。
11. **Thematic roles（题元角色）**是 verb 的 arguments 与事件的语义关系，**不等于 grammatical subject/object**。
12. 被动只改变 syntax position，不改变 role：*The stick was bitten by the dog* 中 stick 仍是 Theme，dog 仍是 Agent。

## 1. Compositional semantics（组合语义）与 entailment（P2–11）★

### 1.1 Compositionality（组合性）

**Compositional semantics（组合语义）**：larger linguistic unit 的 meaning 能由 smaller components 的 meanings 加上其 syntactic structure 推出。像积木：`car + key → car key`。

句子的意思不只由 word meaning 决定，还取决于 **how words combine（句法结构）**；这正是 Syntax 和 Semantics 相连之处。

### 1.2 Entailment（蕴含）★★

**A entails B** iff whenever A is true, B must also be true。方向不能倒。

```text
Jack swims beautifully.  ⇒  Jack swims.       ✓
Jack swims.              ⇒  Jack swims beautifully.  ✗
```

![[AHGC7315-Semantics-P5.png]]

| 关系 | 判断方式 | 课件例子 |
|---|---|---|
| **Entailment（蕴含）** | A 真 → B 必真；单向 | `Jack swims beautifully` → `Jack swims` |
| **Synonymy / paraphrase（同义/释义）** | A entails B 且 B entails A | `postponed the meeting` = `put off the meeting` |
| **Contradiction（矛盾）** | A entails NOT B | `Jack is alive` vs `Jack is dead` |

### 1.3 Non-compositional meaning（非组合性）

| 现象 | 定义/判断 | 例子 |
|---|---|---|
| **Semantic anomaly（语义异常）** | grammar OK，语义特征/常识冲突 | *Colorless green ideas sleep furiously.* |
| **Metaphor（隐喻）** | 表面 anomalous，但借现实知识理解 hidden meaning | *Time is money*；*Walls have ears* |
| **Idiom（习语）** | 整体义不能从单词义加出来 | *drop the ball* = make a mistake；*hit it off* = become friendly immediately |

理解 metaphor 需要：**individual words + literal meaning + facts about the world（世界知识）**。所以 metaphor 是对组合性较“elastic（有弹性）”的例外，并不是语法错误。

---

## 2. Reference（指称）与 sense（意义内容）（P13–19）★

| 术语 | 定义 | 例子 |
|---|---|---|
| **Referent（所指对象）** | word/NP 在现实中指向的 entity/object | 某个实际的人 Jack |
| **Reference（指称关系）** | linguistic form → referent 的 mapping | `Jack`、`the happy swimmer`、`that guy` 可指同一人 |
| **Sense（意义内容）** | independent of reference 的 inherent content | `the happy swimmer` 除“那个人”还含“他很快乐” |

同一个 referent 可以有不同 senses：`Barack Obama`、`a man`、`former US President`、`Michelle Obama’s husband`。反过来，`No one` 没有特定现实个体 referent，仍然有意义。

**考法：**若题目问为什么 `Jack swims` 不必 entail `The happy swimmer swims`，答案是后者额外 entail subject is happy。

---

## 3. Lexical relations（词汇关系）（P20–28）★★★

### 3.1 总表：用 meaning / spelling / sound 判断

| 术语 | Meaning | Spelling | Sound | 例子 |
|---|---|---|---|---|
| **Synonym（同义词）** | same/similar | different | different | sofa / couch |
| **Antonym（反义词）** | opposite | different | different | alive / dead |
| **Homonym（同形同音异义词）** | different | same | same | bark（狗叫 / 树皮） |
| **Homograph（同形异义词）** | different | same | same or different | dove N `[dʌv]` / dove V `[doʊv]` |
| **Homophone（同音异义词）** | different | same or different | same | bear / bare |
| **Heteronym（同形异音异义词）** | different | same | different | dove N / dove V |
| **Polysemy（多义）** | multiple **related** meanings | same | — | diamond（几何形 / baseball field） |

![[AHGC7315-Semantics-P20.png]]

**最常见陷阱：**

- **Homonym** 需要 spelling 和 sound 都相同；它是大类。
- **Heteronym** 是 homograph 的一种：同拼写、不同发音。
- **Polysemy** 的多个意思是 conceptually/historically **related（相关）**；若意义无关，更接近 homonym。
- Synonyms 没有完全所有语境都可互换的两个词，课件说的是 same or very similar in some/all contexts。

### 3.2 Four types of antonyms（四类反义）★

| 类型 | 关键 | 例子 |
|---|---|---|
| **Complementary pair（互补反义）** | 非此即彼；not A = B | alive/dead, present/absent, awake/asleep |
| **Gradable pair（等级反义）** | 连续 scale，中间可有程度 | big/small, hot/cold, happy/sad |
| **Relational opposite（关系反义）** | 同一关系的对称两端 | give/receive, buy/sell, teacher/student |
| **Autoantonym / contranym（自反义词）** | 同一词有相反意义 | *dust* shelves（去灰）/ dust cake（撒粉）；`借` 可 borrow 或 lend |

![[AHGC7315-Semantics-P22.png]]

### 3.3 Hypernym 与 hyponym

| 广义 → 狭义 | 关系 |
|---|---|
| animal → dog, cat, bird | `animal` = **hypernym**；其他 = **hyponyms** |
| fruit → apple, banana, cherry | fruit 是上义词 |
| vehicle → car, bicycle, train | vehicle 是上义词 |

![[AHGC7315-Semantics-P28.png]]

---

## 4. Semantic features（语义特征）与 word embedding（P29–39）★★

**Semantic features（语义特征）**是构成 word meaning 的属性，也反映我们知道一个词“是什么”。课件例：**assassin** 必须 `+human`，且杀的是 important people。

| Feature | Cat | Dog |
|---|---:|---:|
| `+animate` | 1 | 1 |
| `+four-legs` | 1 | 1 |
| `+mammal` | 1 | 1 |
| `+feline` | 1 | 0 |
| `+canine` | 0 | 1 |

**Word embedding（词向量）**同样把 word 表示为 features/vector，但它是从数据学得的连续 numeric vector（如 **Word2Vec、GloVe**），而不是人工填的少量 0/1 标签。它可做 analogy：`king − queen + sister ≈ brother`（课件例）。

> 易错点：semantic feature 是可解释、离散的意义属性；embedding 的每一维通常没有直接可读的名字。

---

## 5. Thematic roles（题元角色 / 语义角色）（P40–51）★★★

**Thematic roles（题元角色）** = verb 的 arguments 和该 verb 描述的 situation 之间的 semantic relation。也叫 **thematic relations / semantic roles**。

| Role | 定义 | 例子 |
|---|---|---|
| **Agent（施事）** | volitional doer / causer | *The dog* bit the stick. |
| **Theme / Patient（受事）** | most directly affected / undergoer | The dog bit *the stick*. |
| **Goal（目标）** | endpoint of change in location/possession | Mary gave *John* a book. |
| **Source（来源）** | where action originates | She took the key *from him*. |
| **Location（地点）** | where action occurs | The kids played *in the park*. |
| **Instrument（工具）** | means used to accomplish action | He opened the door *with a key*. |
| **Experiencer（体验者）** | receives sensory input | *Many people* fear snakes. |

![[AHGC7315-Semantics-P41.png]]

### 5.1 Roles ≠ grammatical positions（角色不等于主宾语）

| 句子 | Subject | Object / PP | roles |
|---|---|---|---|
| *The dog bit the stick.* | dog | stick | Agent / Theme |
| *The stick was bitten by the dog.* | stick | by the dog | **Theme / Agent**（被动后不变） |
| *Mary gave John a book.* | Mary | John / a book | Agent / Goal / Theme |
| *He put the coffee on the table.* | he | coffee / on the table | Agent / Theme / Goal |
| *The key opened the door.* | key | door | Instrument / Theme |
| *The ball rolled down the hill.* | ball | — | Theme（不是 Agent：没有 volition） |

![[AHGC7315-Semantics-P45.png]]

**三步标注法：**

1. 找 verb 表达的 event/state；
2. 问“谁有意发动？”→ Agent；“谁最受影响？”→ Theme；
3. 再找到达点 Goal、来源 Source、发生处 Location、工具 Instrument、感受者 Experiencer。不要先把 subject 自动写 Agent。

---

## Semantics 自测（10 题）

1. If A entails B, then ____. A. B true guarantees A true B. A true guarantees B true C. A and B are antonyms D. A is ungrammatical
2. Which pair are paraphrases according to mutual entailment? A. alive/dead B. Jack swims/Jack swims beautifully C. postpone a meeting/put off a meeting D. bear/bare
3. *Time is money* is best analysed as ____. A. an ungrammatical sentence B. a metaphor C. a homonym D. a contradiction
4. Which phrase is idiomatic? A. green car B. drop the ball (= make a mistake) C. happy swimmer D. dog bark
5. `Barack Obama` and `Michelle Obama’s husband` can have the same ____, but different ____. A. spelling; sound B. reference; sense C. entailment; contradiction D. hypernym; hyponym
6. Which is a heteronym? A. bear/bare B. bark (dog/tree) C. dove N `[dʌv]` / dove V `[doʊv]` D. sofa/couch
7. Which pair is gradable rather than complementary? A. alive/dead B. awake/asleep C. hot/cold D. present/absent
8. Which is the hypernym in `vehicle → car, bicycle, train`? A. car B. bicycle C. train D. vehicle
9. In *The key opened the door*, `the key` is ____. A. Agent B. Theme C. Instrument D. Goal
10. In *Many people fear snakes*, `many people` is most naturally ____. A. Experiencer B. Source C. Instrument D. Location

### 答案

| 题 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 答 | **B** | **C** | **B** | **B** | **B** | **C** | **C** | **D** | **C** | **A** |

---

## 易混淆速查

| 不要混 | 正确区分 |
|---|---|
| entailment vs synonymy | entailment 可单向；synonymy = 双向 entailment。 |
| anomaly vs ungrammaticality | anomaly 是语义/世界知识冲突；ungrammaticality 是句法规则不合法。 |
| reference vs sense | reference 指现实对象；sense 是表达所带的意义内容。 |
| homonym vs polysemy | homonym 意义不同（常无关）；polysemy 意义多但相关。 |
| complementary vs gradable antonym | complementary 没中间值；gradable 有程度和中间状态。 |
| Agent vs subject | Agent 必须是有意的 doer；subject 可为 Theme 或 Instrument。 |
