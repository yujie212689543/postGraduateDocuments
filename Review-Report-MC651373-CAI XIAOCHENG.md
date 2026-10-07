**Review Report Task 1 Applied Natural Language Processing**

**Locality Aware Knowledge Editing for Small Language Models**

**CAI XIAOCHENG | MC651373**CISC7021 Applied Natural Language Processing | October 2026

# **Abstract**

This report reviews four papers on large language models (LLMs), discipline-specific adaptation, knowledge editing, and attacks on large vision-language models (LVLMs), and uses them to define a course project. The general LLM literature shows that capability is shaped by pre-training, adaptation tuning, prompting, retrieval, tools, and evaluation. The discipline survey organizes specialization into internal knowledge optimization and external augmentation. The knowledge-editing study provides the strongest basis for a reproducible project: its KnowEdit benchmark and four evaluation dimensions expose a persistent trade-off among edit success, portability, locality, and fluency. For example, on WikiData\_recent, SERAC reaches 98.68 edit success and 100.00 locality, while ROME reaches 97.18 edit success but only 54.77 locality. The proposed project will reproduce ROME and MEMIT on TinyLlama-1.1B-Chat using KnowEdit subsets, then test a constrained update that combines causal layer selection with a null-space projection inspired by AlphaEdit. Evaluation will include edit success, portability, locality, fluency, runtime, and memory. A six-week schedule is provided.

# **1. Introduction and Scope**

The objective of this review is to build enough background to choose and justify a course project that reimplements and improves a research paper. I selected four recent works with complementary coverage. Zhao et al. provide the general LLM lifecycle from pre-training to evaluation. Xiang et al. explain how LLMs are adapted to scientific and humanistic disciplines. Zhang et al. define knowledge editing and evaluate it on a shared benchmark. Liu et al. review security risks in multimodal models. Together, these papers connect model construction, domain specialization, controllable factual updates, and safety.

The review has four analytical goals: identify the main methodologies used in related topics, summarize the experimental evidence reported by the works, compare the strengths and limitations of each method family, and define a feasible project with measurable deliverables. The project anchor is knowledge editing because the source paper supplies open datasets, baselines, metrics, and an implementation framework. This makes it possible to reproduce published behavior and test one focused technical improvement within the remaining course schedule.

# **2. Literature Read**

## **2.1 Core Papers Reviewed in Detail**

**Table 1.** Core papers and the purpose of each reading.

| **Paper** | **Main focus** | **Why it was read** |
| --- | --- | --- |
| Zhao et al. (2023/2024) | General LLM survey | Establishes the technical pipeline: pre-training, adaptation tuning, utilization, and capacity evaluation. |
| Xiang et al. (2025) | LLMs in discipline-specific research | Shows how domain knowledge is added through internal optimization and external augmentation. |
| Liu et al. (2024) | Attacks on large vision-language models | Defines the threat landscape and the evaluation practices used for multimodal safety. |
| Zhang et al. (2024) | Knowledge editing and KnowEdit | Provides the project anchor: task definition, taxonomy, benchmark, baselines, and evaluation metrics. |

## **2.2 Supporting Works Consulted Through the Core Papers**

The core surveys cite many primary works that define specific methods. I consulted the following supporting papers through the surveys for definitions and baseline context: ROME and MEMIT for locate-then-edit knowledge editing; MEND and SERAC for meta-learning and external memory; LoRA and adapters for parameter-efficient tuning; GPT-3 for in-context learning; Chain-of-Thought for reasoning prompts; retrieval-augmented generation and dense passage retrieval for external knowledge; AlphaEdit for null-space constrained editing; EasyEdit for the implementation framework; and Llama 2 for the main model used in the KnowEdit experiments. Full details appear in the References section.

# **3. Main Methodologies in Related Work**

## **3.1 General LLM Development and Use**

Zhao et al. organize the field into four broad stages. Pre-training builds general language ability from large corpora using Transformer architectures, scaling laws, data cleaning and scheduling, mixed-precision optimization, and distributed parallelism. Adaptation tuning then aligns or specializes the model through instruction tuning, alignment tuning such as reinforcement learning from human feedback, and parameter-efficient methods such as adapters, LoRA, and prompt tuning. Utilization covers zero-shot and few-shot prompting, in-context learning, chain-of-thought reasoning, planning, retrieval, and tool use. Capacity evaluation measures these abilities with benchmark tasks, human judgment, or LLM-based judging.

**Table 2.** The four-stage methodology of general LLM development and use.

| **Stage** | **Representative methods** | **Purpose** | **Main limitation** |
| --- | --- | --- | --- |
| Pre-training | Transformer, scaling laws, data scheduling, distributed training | Build general language and world knowledge | High compute and data quality requirements |
| Adaptation | Instruction tuning, RLHF, adapters, LoRA, prompt tuning | Align behavior or adapt to tasks efficiently | Can overfit, forget, or shift safety behavior |
| Utilization | Few-shot prompting, CoT, RAG, tools, planning | Apply the model without full retraining | Sensitive to prompts, retrieval, and context limits |
| Evaluation | Task benchmarks, human evaluation, LLM-as-a-judge | Measure capability and identify failure modes | Results vary by prompt, parsing, and judge bias |

## **3.2 Discipline-Specific Specialization**

Xiang et al. divide discipline adaptation into internal knowledge optimization and external interaction. Internal methods modify the model through continual pre-training, supervised fine-tuning, or alignment tuning. These methods can deepen domain competence but are computationally expensive and may cause catastrophic forgetting. External methods keep the base model fixed and add capability through prompt engineering, retrieval-augmented generation, agents, or tools. They can access current databases and specialized software, but depend on retrieval quality and integration design.

The survey applies this taxonomy to mathematics, physics, chemistry, biology, and the humanities and social sciences. Mathematics uses LLMs for problem solving, formal proof, and tool-assisted reasoning. Physics uses them for hypothesis generation, simulation analysis, and experimental assistance. Chemistry covers molecular representation, property prediction, reaction prediction, and tool-using agents. Biology covers biomolecular analysis, protein understanding, and genomic research. The humanities and social sciences use LLMs for textual interpretation, cultural heritage, cross-cultural comparison, human behavior modeling, social simulation, and political analysis. Across domains, the recurring constraints are scarce expert data, weak standardization of evaluation, usability barriers for non-AI specialists, and high computation cost.

## **3.3 Knowledge Editing for LLMs**

Knowledge editing aims to change a specific factual behavior without retraining the whole model. Zhang et al. define the edited model as the result of applying an edit function to the original model and a requested knowledge item. A successful edit should change the target answer while preserving behavior on unrelated inputs. The paper studies knowledge insertion, knowledge modification, and knowledge erasure. Modification is divided further into amendment and disruption, while erasure is treated as removing unwanted or sensitive information.

**Table 3.** Method families in knowledge editing for LLMs.

| **Family** | **Mechanism** | **Representative methods** | **Strength** | **Main risk** |
| --- | --- | --- | --- | --- |
| External knowledge | Store edits in memory and retrieve them during inference | SERAC, IKE, ICE, MemPrompt, MeLLo | Preserves model parameters and often preserves locality | Retrieval quality, prompt length, and inference overhead |
| Knowledge merging | Add knowledge through hidden states, patches, or adapters | GRACE, T-Patcher, CaliNET, LoRA, MELO | Lightweight, composable, and relatively local | Interference and capacity limits under many edits |
| Intrinsic editing | Modify selected model parameters | ROME, MEMIT, MEND, KE, SLAG, PMET, AlphaEdit | Directly changes model behavior and can achieve high edit success | Locality and portability trade-offs; unintended side effects |

The taxonomy follows a human-learning analogy: recognition stores knowledge externally, association merges it into model representations, and mastery edits intrinsic knowledge. Inside the mastery family, meta-learning methods such as MEND train a hypernetwork to predict edits, while locate-then-edit methods such as ROME and MEMIT use causal tracing to modify feed-forward layers. ROME computes a rank-one update for a single fact. MEMIT spreads a batch of edits over several layers. AlphaEdit adds a null-space constraint to reduce interference with preserved knowledge.

Zhang et al. evaluate editing with four dimensions. Edit success combines reliability on the edited example and generalization to similar expressions. Portability tests whether the model can use the edited fact in related reasoning, including aliases, composition, and logical generalization such as reversed relations. Locality checks whether unrelated in-distribution and out-of-distribution knowledge remains unchanged. Fluency measures generation diversity with weighted bigram and trigram entropy. For ConvSent, locality is reported as KL divergence, so lower values are better.

## **3.4 Attacks on Large Vision-Language Models**

Liu et al. classify LVLM attacks into four groups. Adversarial attacks perturb images or text to cause incorrect or attacker-chosen outputs and differ by white-box, gray-box, and black-box access. Jailbreak attacks bypass safety alignment through adversarial or typographic prompts and may induce harmful behavior. Prompt injection attacks insert instructions through one or more modalities to redirect the model. Data poisoning and backdoor attacks modify training data or embed triggers so that later inference is compromised.

**Table 4.** Attack families, resources, and evaluation in the LVLM survey.

| **Attack family** | **Objective** | **Representative forms** | **Common evaluation** |
| --- | --- | --- | --- |
| Adversarial | Cause incorrect or targeted outputs | FGSM, PGD, transfer attacks, black-box query attacks | Attack success rate, similarity, semantic deviation |
| Jailbreak | Bypass safety restrictions | Adversarial perturbation, typographic images, prompt perturbation | Attack success rate, unsafe response rate, human or LLM judgment |
| Prompt injection | Redirect instruction following | Unimodal and multimodal instruction injection | Task success, leakage, rule-based or model-based judgment |
| Poisoning and backdoor | Compromise training or trigger later behavior | Data poisoning, visual triggers, physical triggers | Attack success rate, trigger specificity, stealth |

The survey notes that attack success rate is widely used but is not calculated uniformly across studies. Other evaluations include exact match, BLEU-4, METEOR, CIDEr, SPICE, SSIM, CLIP embedding similarity, rule-based scores, model-based semantic judgment, human evaluation, and LLM-as-a-judge. This heterogeneity is similar to the evaluation problem in knowledge editing: a single metric cannot describe whether an intervention is technically successful, safe, and narrowly scoped.

## **3.5 Synthesis and Project Gap**

The reviewed work points to one central gap. Intrinsic knowledge editing can achieve high edit success, but the same update may damage unrelated facts, fail to transfer to related questions, or reduce generation quality. External and parameter-efficient methods reduce some risks, but introduce retrieval, context, or capacity costs. Published results also focus mainly on Llama2-7b-chat. Small language models are attractive for coursework, reproducibility, and deployment, yet their editing behavior is less well characterized. The project therefore targets the locality and portability trade-off in a controlled small-model setting.

# **4. Experimental Results from Reviewed Works**

## **4.1 General LLM Evaluation**

Zhao et al. evaluate closed- and open-source models across language generation, knowledge utilization, reasoning, safety, and interaction tasks. Their results show that model ranking depends on the task and that prompt design can materially change performance. Carefully designed prompts improved ChatGPT from 29.25 to 31.21 on WikiFact and from 78.47 to 79.30 on GSM8k when the prompt used a code-oriented format. At the same time, supervised models still led on some tasks: the reported supervised HumanEval result was 48.20 versus 79.88 for ChatGPT, while supervised Spider was 84.10 versus 70.10 for ChatGPT.

**Table 5.** Selected zero-shot results from Zhao et al. Percent values are reported by the survey.

| **Model** | **HumanEval** | **GSM8k** | **MATH** | **Observation** |
| --- | --- | --- | --- | --- |
| ChatGPT | 79.88 | 78.47 | 33.78 | Strong general task solver |
| Claude 2 | 78.04 | 82.87 | 32.24 | Higher GSM8k than ChatGPT |
| Davinci003 | 67.07 | 57.16 | 17.66 | Below ChatGPT in this comparison |
| LLaMA 2-Chat 7B | 11.59 | 9.63 | 2.22 | Large gap in reasoning and code |

The broader result is not that one model dominates everywhere. Closed-source models lead on many general benchmarks, but supervised task-specific systems remain competitive or better in selected structured tasks. For a course project, this supports a benchmark-based evaluation with fixed prompts and metrics rather than a single aggregate score.

## **4.2 Knowledge Editing Benchmark and Main Results**

KnowEdit contains six datasets covering insertion, modification, and erasure. The benchmark mixes factual triples, question answering, hallucination correction, counterfactuals, sentiment control, and privacy-oriented erasure. The main editing comparison uses Llama2-7b-chat and eight published methods.

**Table 6.** KnowEdit datasets and their task types.

| **Dataset** | **Task** | **Knowledge type** | **Train** | **Test** |
| --- | --- | --- | --- | --- |
| WikiData\_recent | Insertion | New fact | 570 | 1,266 |
| ZsRE | Modification | Question answering | 10,000 | 1,230 |
| WikiBio | Modification | Hallucination correction | 592 | 1,392 |
| WikiData\_counterfact | Modification | Counterfactual fact | 1,455 | 885 |
| ConvSent | Modification | Sentiment | 14,390 | 800 |
| Sanitation | Erasure | Unwanted information | 80 | 80 |

Table 7 reports representative edit success and locality values from the KnowEdit results. For the first five rows, each cell is edit success / locality, with higher values better for both metrics. For ConvSent, locality is KL divergence, so lower is better. For Sanitation, locality is accuracy on the retain set.

**Table 7.** Representative results on KnowEdit. Cells show edit success / locality.

| **Dataset** | **SERAC** | **MEND** | **ROME** | **MEMIT** | **FT-M** |
| --- | --- | --- | --- | --- | --- |
| WikiData\_recent | 98.68 / 100.00 | 95.75 / 94.76 | 97.18 / 54.77 | 97.05 / 52.15 | 100.00 / 64.33 |
| ZsRE | 99.67 / 30.23 | 96.74 / 92.79 | 96.77 / 53.67 | 95.37 / 48.32 | 99.98 / 89.78 |
| WikiBio | 99.69 / 69.79 | 93.66 / 69.51 | 96.08 / 62.74 | 94.40 / 61.51 | 100.00 / 93.38 |
| WikiData\_counterfact | 99.99 / 98.96 | 80.03 / 94.38 | 98.57 / 51.97 | 98.05 / 46.62 | 100.00 / 76.76 |
| ConvSent (lower KL better) | 62.75 / 0.26 | 50.76 / 3.42 | 45.79 / 0.00 | 44.75 / 0.00 | 46.10 / 0.00 |
| Sanitation | 0.00 / 100.00 | 0.00 / 5.29 | 85.00 / 50.31 | 48.75 / 67.47 | 75.00 / 47.07 |

Several patterns are clear. First, no single family wins on every metric. AdaLoRA reaches 100.00 edit success on most insertion and modification datasets, but its locality varies from 56.42 on WikiData\_recent to 81.28 on WikiBio. ROME and MEMIT are strong single-fact editors, yet their locality on WikiData\_recent is only 54.77 and 52.15, and it falls to 51.97 and 46.62 on WikiData\_counterfact. MEND is more stable: on ZsRE it records 96.74 edit success and 92.79 locality, but it fails to erase Sanitation knowledge.

Second, external editing preserves parameters but changes the cost profile. SERAC reaches 99.67 edit success and 30.23 locality on ZsRE, while achieving 100.00 locality on WikiData\_recent and 98.96 on WikiData\_counterfact. This variance makes retrieval and counterfactual-model quality central to the method. Third, fine-tuning a selected layer with the improved FT-M objective is a strong general baseline, but it still scores only 47.07 locality on Sanitation and does not solve portability. Across the reported methods, portability remained a weakness: on WikiData\_recent, SERAC, MEND, ROME, MEMIT, and FT-M scored 63.52, 55.88, 55.25, 56.37, and 65.44 respectively.

The paper's mechanistic analysis explains the trade-off. Factual knowledge can be located in middle feed-forward layers through causal tracing, but knowledge is distributed. A targeted update can therefore affect neighboring relations and general ability. ROME and MEMIT produce large changes with weak locality, whereas MEND and external methods are more conservative. AlphaEdit's null-space idea is relevant because it constrains the update away from directions that encode preserved knowledge.

## **4.3 Discipline-Specific and Multimodal Findings**

The discipline survey reports application-level evidence rather than a single shared benchmark. It documents strong results in selected tasks, including tool-using chemistry agents that improve accuracy over a general model, but the evaluation setups differ by domain and dataset. Its main empirical conclusion is that domain performance depends on data access, task formulation, and the combination of internal and external methods. The main unresolved issue is the absence of standardized disciplinary benchmarks.

The LVLM attack survey likewise cannot provide one comparable score because attack goals and metrics differ. Its contribution is a structured account of which attack families are effective in each access setting and which evaluation methods are used. It reports that attack success rate is common but method-dependent, that transferability remains difficult, and that imperceptibility, interpretability, and robustness against adaptive defenses are open problems.

# **5. Project Idea and Preliminary Strategy**

## **5.1 Project Title and Research Questions**

Project title: Locality Aware Knowledge Editing for Small Language Models: A Reproducible Study of ROME and MEMIT on KnowEdit.

* RQ1: Can ROME and MEMIT be reproduced on a small open model with the KnowEdit evaluation protocol and comparable trends to the published Llama2-7b-chat results?
* RQ2: How do single edits, sequential edits, and batched edits affect edit success, portability, locality, fluency, runtime, and memory?
* RQ3: Does a locality-constrained update with adaptive layer selection improve the locality and portability balance relative to standard ROME and MEMIT?

## **5.2 Base Models and Data**

The primary model will be TinyLlama-1.1B-Chat because it can be edited and evaluated repeatedly on limited hardware and remains architecturally close to Llama. If the reference implementation does not transfer cleanly, I will use a quantized Llama-2-7B-chat checkpoint or a smaller evaluation subset to preserve comparability with the source paper. The main datasets will be ZsRE for question-answer modification and WikiData\_counterfact for counterfactual edits. WikiBio will be added if memory and time allow because it tests hallucination correction and has a strong locality signal. The Sanitation subset will be used only for a small erasure case study.

## **5.3 Preliminary Methodology**

The project will use EasyEdit as the implementation and evaluation framework, with custom instrumentation for memory, runtime, and edit interactions. The first stage will reproduce the baseline methods: no edit, FT-L, FT-M, MEND, SERAC, ROME, MEMIT, and AdaLoRA where available. The second stage will diagnose failures by tracking changed answers on the locality set, paraphrase behavior, reverse relations, and fluency after each batch. The third stage will implement one focused improvement.

The proposed method is a locality-constrained adaptive edit. For each requested edit, causal tracing will first identify candidate feed-forward layers. A conflict score will then compare the requested edit with retained facts using entity, relation, and key-vector similarity. ROME or MEMIT will compute the base update, but the update will be projected away from high-influence directions in the covariance of retained knowledge. A weighting term will reduce the edit magnitude when the conflict score is high. The project will compare three variants: standard ROME or MEMIT, the same method with null-space projection, and the projected method with adaptive layer or rank selection. This contribution is an engineering improvement and controlled study, not a claim of a new model architecture.

## **5.4 Evaluation and Ablations**

Evaluation will follow KnowEdit's four dimensions. Edit success measures reliability and generalization. Portability measures alias, composition, and logical generalization. Locality measures preservation of in-distribution and out-of-distribution knowledge. Fluency measures weighted bigram and trigram entropy. I will add runtime per edit and peak GPU memory because these determine whether the method is practical for small models.

The ablation study will vary the number of sequential edits from 1 to 10, 100, and 500; the edited layer or layer set; the projection strength; the rank of the update; and the batch size. For each setting, I will report mean and standard deviation across at least three edit orders. Error analysis will classify failures as failed target edits, locality damage, paraphrases that were not updated, reverse-relation failures, and repetition or fluency loss.

## **5.5 Expected Contribution and Risk Control**

The expected contribution is a reproducible, low-resource recipe that explains when locality constraints help and when they merely reduce edit strength. The main risks are model-tool incompatibility, high runtime, unstable multi-edit behavior, and differences between TinyLlama and Llama2-7b-chat. These will be controlled by starting with a small fixed subset, logging every edit, freezing prompts and answer matching, and separating reproduction results from improvement results. If the null-space variant is too slow, a simpler weighted residual penalty will be tested as a fallback.

# **6. Tentative Schedule**

The schedule leaves one buffer week for reruns and presentation preparation. Each week ends with a saved experiment log and a short summary of decisions.

**Table 8.** Six-week project schedule and expected outputs.

| **Period** | **Tasks** | **Expected output** |
| --- | --- | --- |
| Week 1 6-12 Oct | Finalize topic, complete the review report, install EasyEdit, prepare KnowEdit subsets, verify TinyLlama inference. | Task 1 report; runnable environment; data manifest. |
| Week 2 13-19 Oct | Reproduce zero-edit, FT-L, FT-M, MEND, SERAC, ROME, and MEMIT on a fixed subset; verify prompts and metrics. | Baseline tables; reproduction notes; failure log. |
| Week 3 20-26 Oct | Analyze edit versus locality failures; implement null-space projection and conflict weighting. | First method prototype; diagnostic plots; updated evaluation harness. |
| Week 4 27 Oct-2 Nov | Run layer, rank, projection-strength, and sequential-edit ablations; compare with ROME and MEMIT. | Ablation results; runtime and memory measurements. |
| Week 5 3-9 Nov | Run final experiments on the selected setting; perform error analysis and robustness checks. | Final result tables; failure taxonomy; reproducibility package. |
| Week 6 10-16 Nov | Write the final report, create figures, prepare the presentation, and rehearse. | Final report and presentation slides. |
| Buffer 17-20 Nov | Correct presentation issues, rerun missing experiments, and finalize submission files. | Submission-ready project package. |

# **7. Conclusion**

The four reviewed papers show that LLM capability is built through a layered pipeline, extended to disciplines through training or external knowledge, and increasingly managed through targeted knowledge editing. The strongest evidence for a course project comes from KnowEdit: it defines the task, supplies a shared benchmark, and demonstrates that current methods trade edit success against locality, portability, and fluency. The proposed project will reproduce ROME and MEMIT on a small model and test a constrained, adaptive update aimed at improving that trade-off. The outcome will be a reproducible evaluation, a clear account of failure modes, and evidence about whether locality-aware editing is practical for small language models.

# **References**

[1] Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. (2020). Language Models are Few-Shot Learners. NeurIPS.

[2] Cohen, R., Biran, E., Yoran, O., Globerson, A., and Geva, M. (2023). Evaluating the Ripple Effects of Knowledge Editing in Language Models. arXiv:2307.12976.

[3] Fang, J., Jiang, H., Wang, K., Ma, Y., Wang, X., He, X., and Chua, T.-S. (2024). AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models. arXiv:2410.02355.

[4] Hartvigsen, T., Sankaranarayanan, S., Palangi, H., Kim, Y., and Ghassemi, M. (2022). Aging with GRACE: Lifelong Model Editing with Discrete Key-Value Adaptors. arXiv:2211.11031.

[5] Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B., de Laroussilhe, Q., Gesmundo, A., Attariyan, M., and Gelly, S. (2019). Parameter-Efficient Transfer Learning for NLP. ICML.

[6] Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685.

[7] Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., and Yih, W.-t. (2020). Dense Passage Retrieval for Open-Domain Question Answering. EMNLP.

[8] Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS.

[9] Liu, D., Yang, M., Qu, X., Zhou, P., Cheng, Y., and Hu, W. (2024). A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends. arXiv:2407.07403.

[10] Meng, K., Bau, D., Andonian, A., and Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. NeurIPS.

[11] Meng, K., Sharma, A. S., Andonian, A. J., Belinkov, Y., and Bau, D. (2023). Mass-Editing Memory in a Transformer. ICLR.

[12] Mitchell, E., Lin, C., Bosselut, A., Finn, C., and Manning, C. D. (2022). Fast Model Editing at Scale. ICLR.

[13] Mitchell, E., Lin, C., Bosselut, A., Manning, C. D., and Finn, C. (2022). Memory-Based Model Editing at Scale. ICML.

[14] Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., et al. (2023). Llama 2: Open Foundation and Fine-Tuned Chat Models. arXiv:2307.09288.

[15] Wang, P., Zhang, N., Xie, X., Yao, Y., Tian, B., Wang, M., et al. (2023). EasyEdit: An Easy-to-Use Knowledge Editing Framework for Large Language Models. arXiv:2308.07269.

[16] Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., and Zhou, D. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS.

[17] Xiang, L., Zhao, Y., Zhang, Y., and Zong, C. (2025). A Survey of Large Language Models in Discipline-specific Research: Challenges, Methods and Opportunities. Studies in Informatics and Control, 34(1), 5-24.

[18] Zhang, N., Yao, Y., Tian, B., Wang, P., Deng, S., Wang, M., et al. (2024). A Comprehensive Study of Knowledge Editing for Large Language Models. arXiv:2401.01286.

[19] Zhao, W. X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y., et al. (2023). A Survey of Large Language Models. arXiv:2303.18223.