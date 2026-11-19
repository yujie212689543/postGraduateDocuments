# AHGC7315 PPT 课堂练习｜Syntax（句法学）

> 来源：`Syntax.pdf` P21、P22、P64、P65。
> 下面是 PPT 原题转录，暂不附答案。先做“成分判断”，再进入“歧义树”和“X-bar 画树”。

## 1. Constituency Tests（P21）

![[AHGC7315-Syntax-Exercise-P21.png]]

**Question:** Are the underlined parts in (a) and (b) a constituent?

| # | Sentence | Underlined part |
|---|---|---|
| a | *We ran out of house.* | **out of house** |
| b | *We ran out of gas.* | **out of gas** |

作答时用三种测试中的至少一种说明：

```text
stand alone / pronoun replacement / move as a unit
```

---

## 2. More Constituency Tests（P22）

![[AHGC7315-Syntax-Exercise-P22.png]]

**Question:** Which of the boldfaced portions in the sentences are constituents?

1. Martha found **a lovely pillow** for the couch.
2. The **light in this room** is terrible.
3. I wonder **if Bonnie has finished packing her books**.
4. Melissa slept **in her class**.
5. **Pete and Max** are fighting over the bone.
6. I gave a bone to Pete **and to Max** yesterday.
7. I gave a bone to **Pete and** to Max yesterday.
8. I gave **a bone to Pete** and to Max yesterday.
9. I gave **a bone to Pete**.

---

## 3. Structural Ambiguity（P64）

![[AHGC7315-Syntax-Exercise-P64.png]]

**Question:** Draw two different trees to explain the ambiguity in:

> *The magician touched the child with the wand.*

先判断两种意思：

1. `with the wand` 修饰哪个动作？
2. `with the wand` 修饰哪个名词？

---

## 4. X-bar Trees（P65）

![[AHGC7315-Syntax-Exercise-P65.png]]

**Question:** Draw phrase structure trees in X-bar for:

1. *The puppy found the child.*
2. *A surly passenger insulted the attendant.*
3. *The ice melted.*
4. *The house on the hill collapsed in the earthquake.*
5. *The hot sun melted the ice.*

画树前先标出：

```text
Head / Specifier / Complement / Adjunct
```

---

## 5. Constituency Tests：讲解版

### 判断公式

一个真正的 constituent 应该能够**作为一整块**参与句法操作：

```text
能用 wh-question 单独回答？
能整块被 pronoun / there 替代？
能整块移动？
```

三种测试中，满足一种通常就足以说明它是 constituent。

### P21

**a. We ran [out of house]. -> Yes**

- `out of house` 是 **PP（介词短语）**。
- Where did we run? -> *Out of house.*
- We ran there. 中 `there` 可以替代整个地点 PP。
- 结构是：`ran | [out of house]`。

**b. We ran [out of gas]. -> No**

- 这里不是一个普通 PP，而是短语动词 **run out of（用完）** 加宾语 `gas`。
- What did we run out of? -> *Gas.*
- We ran out of it. 中 `it` 替代的是 `gas`，不是整个 `out of gas`。
- 结构是：`[run out of] | [gas]`。

所以两句话表面都像“V + out of + N”，但内部结构不同：

```text
(a) ran | [out of house]       -> out of house = PP
(b) [run out of] | [gas]       -> gas = complement
```

### P22

| 题 | 回答 | 成分类型 | 最短测试 |
|---|---|---|---|
| a | **Yes** | NP | Martha found **it**. |
| b | **Yes** | N' | The **[light in this room]** 是主语 NP 内部的名词核心组 |
| c | **Yes** | CP | I wonder **if...**；整个 if-clause 可作 wonder 的补足语 |
| d | **Yes** | PP | Melissa slept **there**. |
| e | **Yes** | coordinated NP | **They** are fighting. |

题 b 最容易混：完整的 subject 是 `the light in this room`，即 NP；题目没有把 `the` 划进去，所以 boldfaced portion 是里面的 **N'（名词核心组）**，仍然是一个 constituent。

---

*最后整理：2026-11-19。*
