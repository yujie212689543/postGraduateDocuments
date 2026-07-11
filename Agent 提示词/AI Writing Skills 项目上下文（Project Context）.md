这是我建议你保存的新对话开场内容。它不是聊天记录，而是一份**项目状态（Project Context）**，以后你开新对话直接贴给我，我就能无缝继续完善整个 Skills 库。

---

# AI Writing Skills 项目上下文（Project Context）

## 一、项目目标

我正在建立一套长期维护的 AI Writing Skills 知识库，供 Claude Code、ChatGPT、DeepSeek 等大模型共同使用。

目标不是收集 Prompt，而是建立一套**可持续演进的写作知识体系（Knowledge System）**。

整个知识库遵循：

> 实践（Project）  
> → 复盘（Notes）  
> → 总结（Style Guide）  
> → 长期迭代（Knowledge）

所有规则都必须来源于真实项目，而不是凭空制定。

---

# 二、整体目录

目前目录：

```text
writing/
├── README.md
├── 00-Notes.md
├── 01-Chinese-Writing.md
├── 02-Government-Proposal.md
├── 03-Academic-Paper.md
├── 04-Technical-Document.md
└── 99-Anti-Pattern.md
```

各文件定位如下：

## README

整个 Writing Skills 的索引。

介绍每个 Skills 的作用。

---

## 00-Notes

不是 Prompt。

不是规则。

而是经验库（Knowledge Base）。

记录：

- Case Study
    
- Lessons Learned
    
- Candidates
    
- Ideas
    

只有同类问题反复出现（建议≥3 次），才升级进入 Style Guide。

---

## 01-Chinese-Writing

中文正式写作规范。

适用于：

- 公文
    
- 汇报
    
- 方案
    
- 新闻稿
    
- 各类正式中文写作
    

强调：

自然表达

中文母语者语感

信息组织

段落衔接

逻辑递进

---

## 02-Government-Proposal

政务项目申报。

适用于：

数据大赛

优秀案例

网络强省

创新成果

项目申报书

重点：

不是介绍技术。

而是说明：

为什么做

解决什么

带来什么价值

---

## 03-Academic-Paper

研究生论文 Skills。

适用于：

Research Proposal

Literature Review

Course Report

Conference Paper

Master Thesis

强调：

Research Gap

Evidence First

Discussion

Academic Tone

---

## 04-Technical-Document

暂未完成。

未来用于：

API

README

Architecture

Design Doc

PRD

Agent Design

---

## 99-Anti-Pattern

暂未完成。

记录：

AI 最容易犯的写作错误。

例如：

机械连接词

连续短句

数字堆砌

技术堆砌

AI 腔

---

# 三、本次项目（江苏数据大赛）最大的收获

本次几乎重写了一整份《江苏数据大赛项目申报书》。

重点不是润色。

而是重新组织信息。

得到很多长期规律。

## 最大发现

AI 不太会写文章。

AI 很会写句子。

真正决定文章质量的是：

信息组织。

不是措辞。

---

## AI 最典型的问题

① 一句话一个信息。

导致：

读起来一直停顿。

没有中文阅读节奏。

---

② 每一句都是完整句。

没有：

承接

递进

解释

补充

转折

读起来像 PPT。

---

③ 技术堆砌。

喜欢介绍：

Transformer

Paddle

昇腾

Token

参数

但是没有回答：

为什么。

---

④ 数字堆砌。

喜欢：

21.1 亿

2.4 万

99.83%

全部连续出现。

读者不知道重点。

---

⑤ 段落之间互相独立。

没有形成：

问题

↓

原因

↓

方案

↓

成效

↓

价值

这样的完整论证。

---

# 四、本次修改形成的核心原则

## 原则一

技术不是价值。

技术解决的问题才是价值。

---

## 原则二

数字是论据。

不是正文。

---

## 原则三

不要介绍。

要解释。

介绍：

是什么。

解释：

为什么。

---

## 原则四

段落比句子更重要。

真正优秀的文章：

先设计段落。

再写句子。

---

## 原则五

逻辑衔接比连接词重要。

不要大量：

此外

与此同时

首先

其次

最后

真正自然的过渡来自：

因果

递进

解释

比较

补充

---

## 原则六

永远站在读者角度。

写之前先问：

读者是谁？

他最关心什么？

什么应该前置？

什么可以删？

---

# 五、我们形成的新工作流

以后任何项目都采用：

```
项目开始
      │
      ▼
AI 初稿
      │
      ▼
人工修改
      │
      ▼
总结经验
      │
      ▼
记录 Notes
      │
      ▼
重复出现
      │
      ▼
升级 Style Guide
```

因此：

Notes 是经验池。

Style Guide 是规则库。

---

# 六、未来规划

下一步继续完善：

① 04-Technical-Document

包括：

API

README

Architecture

Design

PRD

Agent Design

GitHub Documentation

---

② 99-Anti-Pattern

建立：

AI 写作黑名单。

以后任何模型生成内容前都检查：

有没有：

AI 腔

机械衔接

连续短句

数字堆砌

介绍技术

没有价值表达

---

③ 后续如果研究生论文、技术文档、产品文档出现新的规律，也按照：

Case → Notes → Style Guide

持续沉淀。

---

# 七、我的长期目标

我的目标不是积累 Prompt，而是建立一套可以陪伴整个研究生阶段、工作阶段甚至未来职业发展的 AI 协作知识库。

ChatGPT 负责：

规划

复盘

总结

沉淀

Claude Code 负责：

执行

开发

实现

DeepSeek 等模型负责：

生成

扩写

初稿

整个知识库不断演进，最终形成属于自己的 AI 工作流和知识体系。

---

## 我最后补充一个建议

经过这几天一起做申报书和搭建 Skills，我发现你的思路已经从「让 AI 帮我写」转变为「让 AI 成为我的能力放大器」。这是一个很大的变化。

因此，我建议以后整个项目不要叫 **Writing Skills**，而是在仓库更高一级建立一个总目录，例如：

```text
knowledge/
│
├── writing/
├── coding/
├── research/
├── workflow/
├── prompting/
├── thinking/
└── review/
```

其中 `writing/` 只是第一块。随着你研究生期间做论文、开发 Agent、写技术文档、做项目规划，这套知识库会逐渐成长为你的**个人 AI Operating System（AI 工作系统）**。我认为，这会比单纯积累 Prompt 的价值高得多。