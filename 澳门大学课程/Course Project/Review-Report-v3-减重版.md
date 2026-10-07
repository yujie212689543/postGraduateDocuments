# Sequential Knowledge Editing in GPT-2 XL: A Comparative Study of ROME, MEMIT, and AlphaEdit on KnowEdit

**Review Report — Task 1**

**Group 36 | CISC7021 Applied Natural Language Processing | October 2026**

**Members:** CAI XIAOCHENG (MC651373); KE GUANYU (MC664433); GU YUJIE (MC664973)

*Revised review and project proposal*

---

## Abstract

Knowledge editing aims to update selected factual associations in a language model while preserving behavior that should remain unchanged. A successful update to one prompt, however, does not establish that related questions will be answered correctly or that earlier edits will survive subsequent updates. This report reviews ROME, MEMIT, AlphaEdit, and KnowEdit to motivate a controlled study of sequential editing. The method discussion follows the progression from targeted single-fact updates to multi-fact editing and preservation constraints. We propose to reproduce AlphaEdit as the main method and compare it with ROME, MEMIT, and an unedited baseline on GPT-2 XL, using a fixed subset of KnowEdit's ZsRE dataset. The main experiment will track edit success, locality, portability, and retention of earlier edits as updates accumulate. Edit order, runtime, and peak GPU memory will provide additional evidence about robustness and feasibility. The expected contribution is a reproducible empirical comparison and failure analysis; no new editing algorithm or experimental outcome is claimed. A pilot will establish implementation compatibility and resource requirements before the formal protocol is frozen.

## 1. Introduction and Scope

Language models can retain factual associations that are incorrect or become outdated. Updating the entire model for a small set of changes is costly and can affect behavior beyond the intended facts. Knowledge editing addresses this problem through targeted changes. For a requested association such as a subject, relation, and replacement object, an editor should produce the new answer while limiting unintended effects [1–4].

This requirement becomes harder when edits accumulate. The latest target may be answered correctly even though earlier updates have been forgotten. Unrelated answers may change, and questions that depend on the new fact may still receive outdated answers. These are different failure modes: locality concerns behavior outside the intended edit, retention concerns previously introduced updates, and portability concerns related knowledge that should change consistently.

Our project therefore focuses on a common sequential-editing protocol rather than a broad comparison of model families or application domains. We will use GPT-2 XL as the planned base model, AlphaEdit as the main reproduction target, ROME and MEMIT as comparison methods, and KnowEdit as the evaluation framework. The scope is limited to one factual-editing dataset and a manageable number of updates. Hardware feasibility and the final sample size will be confirmed through a pilot.

## 2. Literature Selection and Roles

### 2.1 Core Literature

The four core papers serve complementary roles in the project. The method papers provide the algorithms to implement and critique; KnowEdit provides a broader evaluation perspective. Table 1 identifies their roles without treating inclusion in this review as evidence that every group member has completed an independent close reading.

**Table 1. Core papers and their roles in the project.**

| Paper | Main focus | Role in this review |
|---|---|---|
| Meng et al., ROME [1] | Targeted editing of an individual factual association | Establishes the single-fact baseline |
| Meng et al., MEMIT [2] | Editing many factual associations | Extends the comparison to scalable parameter editing |
| Fang et al., AlphaEdit [3] | Preservation during knowledge updates | Main method to reproduce and evaluate |
| Zhang et al., KnowEdit [4] | Knowledge-editing tasks and evaluation | Supplies the dataset and metric framework |

### 2.2 Supporting Literature

The general LLM survey [9] provides background on the wider choices of training, adaptation, prompting, and evaluation. These topics explain where editing fits but do not require separate application surveys or general-model leaderboards in this project.

Two sequential-editing studies are particularly relevant. Gupta et al. [5] report gradual and catastrophic forgetting in their evaluated ROME and MEMIT settings. Their later work, Rebuilding ROME [6], links disabling edits to irregularities in the original ROME implementation and introduces r-ROME. Together, these papers motivate both retention measurements and implementation checks. They do not justify predicting that every ROME implementation must collapse after a fixed number of edits.

EasyEdit [7] provides the planned implementation framework, and the GPT-2 technical report [8] documents the model family. Code versions and configurations will be recorded separately from paper citations because software changes can affect the observed results.

## 3. Critical Review of the Methods

### 3.1 ROME: Targeted Single-Fact Editing

ROME treats a feed-forward module as an associative memory and applies a rank-one update to a selected weight matrix. Its causal-tracing experiments identify computations involved in factual retrieval, and its CounterFact evaluation examines whether edited associations generalize across prompts while preserving neighboring facts [1]. This connects an interpretable account of retrieval with a concrete parameter update.

The evidence supports targeted editing under the studied models and prompts; it does not establish that every fact occupies an isolated location or that a long sequence of updates will preserve all earlier changes. In our study, ROME will provide a single-fact baseline applied repeatedly. We will fix the implementation and layer configuration, then measure accumulated effects rather than assume that isolated-edit performance transfers to a sequence.

### 3.2 MEMIT: Scaling to Multiple Facts

MEMIT extends the associative-memory approach by distributing updates across several feed-forward layers. Its experiments demonstrate simultaneous editing of thousands of associations, addressing the limited scale of single-fact methods [2]. The central contribution is a method for accommodating many requested updates within a shared model.

Simultaneous batch editing and repeated sequential editing remain different experimental settings. A method that computes one update from many requests has information unavailable to an editor receiving one request at a time. Our main comparison will therefore use one request per step for every method. This tests a common sequential use case, but it does not reproduce MEMIT's principal large-batch experiment or measure its maximum batch-editing capacity.

### 3.3 AlphaEdit: Preserving Existing Knowledge

AlphaEdit projects parameter changes into a null space associated with preserved knowledge, aiming to reduce interference during editing. Its evaluation includes GPT-2 XL, GPT-J, and LLaMA3, with additional KnowEdit experiments in the appendix [3]. This makes it a suitable primary reproduction target rather than merely an inspiration for an independently claimed projection method.

The preservation argument depends on the represented knowledge and the mathematical setting of the update. It should not be interpreted as a guarantee that every natural-language answer remains correct. We will evaluate the complete method under our shared protocol. Without a controlled component ablation, differences between AlphaEdit and the baselines cannot be attributed solely to projection.

### 3.4 KnowEdit and Evaluation Coverage

KnowEdit examines insertion, modification, and erasure, with evaluation covering edit success, portability, locality, and fluency [4]. Its broader perspective matters because changing a target answer can leave related questions inconsistent. The version used here, arXiv:2401.01286v5, already includes AlphaEdit in its discussion; we also cite the original method paper directly.

These dimensions need explicit operational definitions. A token-level score, complete-answer accuracy, and agreement with the original model measure different properties. Similarly, preserving an originally incorrect output is evidence of invariance, not correctness. Our metric implementation and reporting will keep these distinctions visible.

**Table 2. Method comparison and implications for this project.**

| Method | Update mechanism | Main contribution | Question in the proposed study |
|---|---|---|---|
| ROME [1] | Rank-one change in a selected feed-forward layer | Targeted single-fact editing | How does repeated use affect earlier updates? |
| MEMIT [2] | Updates distributed across several layers | Multi-fact editing at greater scale | How does it perform when requests arrive individually? |
| AlphaEdit [3] | Update constrained by preserved-knowledge structure | Reduced interference during editing | How well does preservation coexist with new target and related-answer performance? |

### 3.5 Project Focus

Existing studies establish strong editing methods, but their reported outcomes depend on model, data, implementation, and evaluation protocol. We will conduct a controlled comparison on a fixed KnowEdit subset, focusing on how target performance, locality, portability, and earlier-edit retention change as edits accumulate. This is a defined empirical question, not a claim that GPT-2 XL or preservation-aware editing has been unexplored.

## 4. Published Evidence and Its Limits

### 4.1 KnowEdit Datasets

Table 3 preserves the dataset overview from the reviewed KnowEdit version [4]. It describes the benchmark, not the number of examples we will run. Our formal study will use only the ZsRE subset; the remaining datasets provide context for the published comparison.

**Table 3. KnowEdit datasets and reported split sizes [4].**

| Dataset | Task | Knowledge type | Train | Test |
|---|---|---|---|---|
| WikiData_recent | Insertion | New facts | 570 | 1,266 |
| ZsRE | Modification | Question answering | 10,000 | 1,230 |
| WikiBio | Modification | Hallucination correction | 592 | 1,392 |
| WikiData_counterfact | Modification | Counterfactual facts | 1,455 | 885 |
| ConvSent | Modification | Sentiment | 14,390 | 800 |
| Sanitation | Erasure | Unwanted information | 80 | 80 |

### 4.2 Reported Editing Results

Table 4 reproduces the draft's selected results from KnowEdit v5, Table 4, for Llama2-7b-chat [4]. It includes five of the eight evaluated methods. These are literature results, not results from our proposed GPT-2 XL experiments.

**Table 4. Published KnowEdit results on Llama2-7b-chat. Each cell reports edit success / locality [4, Table 4].**

| Dataset | SERAC | MEND | ROME | MEMIT | FT-M |
|---|---|---|---|---|---|
| WikiData_recent | 98.68 / 100.00 | 95.75 / 94.76 | 97.18 / 54.77 | 97.05 / 52.15 | 100.00 / 64.33 |
| ZsRE | 99.67 / 30.23 | 96.74 / 92.79 | 96.77 / 53.67 | 95.37 / 48.32 | 99.98 / 89.78 |
| WikiBio | 99.69 / 69.79 | 93.66 / 69.51 | 96.08 / 62.74 | 94.40 / 61.51 | 100.00 / 93.38 |
| WikiData_counterfact | 99.99 / 98.96 | 80.03 / 94.38 | 98.57 / 51.97 | 98.05 / 46.62 | 100.00 / 76.76 |
| ConvSent | 62.75 / 0.26 | 50.76 / 3.42 | 45.79 / 0.00 | 44.75 / 0.00 | 46.10 / 0.00 |
| Sanitation | 0.00 / 100.00 | 0.00 / 5.29 | 85.00 / 50.31 | 48.75 / 67.47 | 75.00 / 47.07 |

For the first four rows, larger reported values are better for both measures. ConvSent locality is KL divergence, for which lower is better. Sanitation locality measures retain-set accuracy. These quantities should not be pooled into a single cross-dataset average without accounting for their different meanings.

The selected results illustrate why target success alone is insufficient. For example, ROME and MEMIT achieve high edit success on WikiData_counterfact while their reported locality scores are considerably lower. SERAC's locality also differs substantially between ZsRE and WikiData_recent. These observations support measuring several outcomes on each dataset, rather than declaring a universal winner from one score.

### 4.3 What the Literature Does Not Establish

The table does not predict how the methods will behave on GPT-2 XL after 100 sequential edits. Matching a model name is also insufficient for numerical reproduction: data, prompts, metrics, edit counts, batching, and code must match. In particular, the original CounterFact dataset used in method papers must not be conflated with KnowEdit's WikiData_counterfact subset.

Our work will reproduce method implementations in a specified evaluation setting. Published results will motivate the design and support qualitative discussion, rather than serve as numerical pass thresholds. Implementation problems, prompt mismatches, and numerical instability will be investigated before a failure is attributed to the underlying method or model capacity.

## 5. Project Design and Preliminary Strategy

### 5.1 Research Questions

**RQ1:** How do ROME, MEMIT, and AlphaEdit compare in edit success, locality, and portability on a fixed KnowEdit subset using GPT-2 XL?

**RQ2:** How do these outcomes, including retention of previously edited facts, change as sequential edits accumulate?

**RQ3:** How sensitive are the results to edit order, and what runtime and peak GPU memory does each method require?

### 5.2 Model, Data, and Pilot

GPT-2 XL [8] will be the single planned base model. We will use EasyEdit [7] and inspect the available method configurations before running a pilot. Configuration availability is not proof that all methods fit the group's hardware or run correctly. We will record the checkpoint, tokenizer, precision, device, software versions, and hyperparameters.

The pilot will use approximately 20–50 examples from the selected dataset to check data fields, subject identification, prompt construction, answer matching, state management, runtime, and memory. Pilot examples will be disjoint from the formal evaluation subset. We will inspect locality and portability annotations before choosing the formal sample; missing annotations will be recorded rather than silently discarded.

The initial formal target is 100 edit requests from the ZsRE subset. A fixed selection procedure will produce a manifest of sample IDs and annotation coverage. We will screen for duplicate or contradictory requested edits and conflicts between locality probes and the intended updates. Any necessary exclusions will be documented before results are examined and applied consistently across methods. The pilot will determine whether the target scale is feasible; any revision to scope will be recorded before formal runs.

**Compute.** The editing experiments will be executed on free Kaggle T4 GPUs (16 GB each, with a weekly per-account quota), and a single local 12 GB GPU will be used for verification runs, debugging, and analysis. Because peak memory, rather than runtime, is the binding constraint on the available hardware, the protocol is fixed before formal runs and measured peak memory is reported for each method. The availability of an official configuration is not treated as evidence that a method fits the available memory.

### 5.3 Sequential Editing Protocol

The comparison will include the unedited model, ROME, MEMIT, and AlphaEdit. Each editing method will receive one request per step, with the changed model carried into the next step. Checkpoints will be evaluated before editing and after 1, 10, and 100 accumulated requests.

Each independent method–dataset–order run will begin from the same original checkpoint. We will restore both model weights and method-specific state between independent runs, while preserving the state required by each algorithm within a sequence. Statistics or caches may be reused only when they are valid for the same model and configuration; edit-dependent history must not leak between runs. This distinction prevents an intended sequential experiment from becoming a collection of independent single-edit tests.

We will use two fixed permutations of the same 100 requests, shared by all methods. At the final checkpoint, every order will contain the same edited fact set, enabling a matched assessment of order sensitivity. Earlier prefixes can contain different facts; differences at the 1- and 10-edit checkpoints will therefore not be interpreted entirely as order effects. The unedited baseline will be evaluated on the corresponding probes using the same settings.

### 5.4 Metrics and Aggregation

**Edit success.** We will record the score of each request immediately after its edit. At each checkpoint, we will also evaluate all requests introduced so far. The most recent request's score and the mean over accumulated targets will be reported separately, so a successful final update cannot conceal earlier failures.

**Earlier-edit retention.** For each earlier request, its checkpoint score will be compared with its immediate post-edit score. We will report the mean score change for previous requests and, when a binary complete-answer criterion is available, the proportion of initially successful edits that remain successful. The denominator will be shown; if no earlier edit initially succeeded, conditional retention will be N/A. At checkpoint 1, earlier-edit retention is also N/A. This separates forgetting from an edit that never succeeded.

**Locality.** A fixed set of probes for behavior that should remain unchanged will be evaluated against the original, unedited model. The same reference will be used throughout the sequence, rather than only comparing consecutive checkpoints. Where labels are available, original and edited answer correctness will be shown separately from output preservation.

**Portability.** Available alias, compositional, and logical probes will be evaluated by subtype. We will report annotation coverage, effective probe counts, and valid request counts. Missing annotations will be N/A, not zero. For each subtype, we will first average valid probes within a request, then average across eligible requests; the aggregation rule will be fixed before formal evaluation. Results will remain separate by dataset and subtype rather than be hidden in an unsupported overall score.

**Metric implementation.** We will inspect the exact evaluation functions in the pinned code. Every score will identify whether it uses teacher-forced tokens, free generation, token agreement, or complete-answer matching. Token-level accuracy will not be described as full-answer correctness. Prompt templates, tokenization, matching rules, and generation settings will be fixed across methods. The no-edit measurements will establish how much of each score was already present before intervention.

**Resources and auxiliary checks.** Setup costs, including statistics and projection preparation, will be timed separately from editing and evaluation. We will record per-edit runtime, total run time, and peak GPU memory with a consistent measurement procedure. Available paraphrases will support a supplementary generalization check, and a fixed small set of generated examples will help identify repetition or incoherence. If n-gram entropy is used, it will be labeled as a diversity proxy rather than evidence of correctness or coherence.

At the final checkpoint, we will present per-order results and their mean and standard deviation. This variation describes the two selected orders, not all sources of statistical uncertainty. Failed runs, out-of-memory errors, and non-finite updates will be reported with the last completed checkpoint; they will not be silently removed or replaced with favorable examples.

### 5.5 Expected Contribution, Feasibility, and Limits

The intended output is an executable comparison with fixed data manifests, configurations, metric definitions, run logs, and an analysis of failed or inconsistent edits. We will distinguish failed target updates, loss of earlier edits, locality damage, portability failures, and generation degradation. These categories will help explain trade-offs beyond a single ranking.

The main risks are implementation incompatibility, resource limits, and ambiguous measurement. Pilot results will determine the computational budget. Reducing the total number of edits may reduce runtime without lowering the peak memory needed for one update, so it will not be treated as an automatic solution to an out-of-memory error. We will first inspect batching, sequence lengths, precision, and cache behavior; any material protocol change will be documented and applied consistently. A method that cannot be executed within the available compute budget will be reported as such rather than omitted silently.

The main deliverable does not include adaptive layer selection, conflict weighting, a newly claimed projection method, or a broad parameter sweep. If the course specification requires a method modification, we will select one narrowly defined extension after the pilot and evaluate it separately against the frozen baseline protocol. A component-level causal claim would require a corresponding controlled ablation.

## 6. Tentative Schedule

The schedule includes pilot work, protocol and result freezes, and preparation of submission materials before an internal completion target. The Review Report is due on Oct 10, 2026 at 23:55. Implementation and All Materials are due on Nov 17, 2026 at 00:00, slides on Nov 17, 2026 at 14:00, and the Final Report on Nov 17, 2026 at 23:55. The Final Report must use the ACL two-column format. Presentations are scheduled for Nov 17, 2026 and Nov 24, 2026, with four minutes for presentation and one minute for questions.

**Table 5. Proposed schedule and deliverables.**

| Period | Tasks | Expected output | Owner |
|---|---|---|---|
| Oct 7, 2026–Oct 10, 2026 | Finalize the review, confirm citations and authorship, and submit the Review Report by 23:55 on the last day | Submitted Review Report | All |
| Oct 11, 2026–Oct 12, 2026 | Complete core-paper reading, set up the environment, and run initial examples | Runnable examples; initial compatibility notes | Implementation |
| Oct 13, 2026–Oct 19, 2026 | Run the pilot; validate metrics and state restoration; confirm resources and sample size | Frozen protocol, data manifests, versions, and resource estimate | Implementation / Data & Evaluation |
| Oct 20, 2026–Oct 26, 2026 | Run the primary sequential experiments and inspect failures as they occur | Checkpoint results; run logs; initial failure analysis | Implementation / Data & Evaluation |
| Oct 27, 2026–Nov 2, 2026 | Complete the matched order comparisons and any necessary reruns | Per-order tables; retention and locality curves; resource measurements | Implementation / Data & Evaluation |
| Nov 3, 2026–Nov 9, 2026 | Resolve identified gaps, complete error analysis, and freeze results | Final figures, tables, and reproducibility package | Analysis & Writing |
| Nov 10, 2026–Nov 15, 2026 | Write the final report, prepare slides and any required video, and rehearse | Complete submission materials | Analysis & Writing |
| Nov 16, 2026 | Check files, links, authorship, and submission requirements | Internal submission-ready package | All |

The group will finish the submission-ready package by Nov 16, 2026, ahead of the earliest official deadline.

## 7. Conclusion

ROME, MEMIT, AlphaEdit, and KnowEdit provide a focused basis for studying targeted updates and their wider effects. Their combined relevance is that editing quality must be assessed beyond the latest target answer and within a clearly defined experimental protocol. Our proposed study will compare three editing methods on GPT-2 XL using a fixed KnowEdit subset, tracking new-target performance, earlier-edit retention, locality, portability, and resource costs. The project will contribute a reproducible empirical analysis within this scope. The pilot and subsequent experiments will determine the observed trade-offs; this proposal does not presume that any method will dominate.

## References

1. Meng, K., Bau, D., Andonian, A., and Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. NeurIPS.
2. Meng, K., Sharma, A. S., Andonian, A., Belinkov, Y., and Bau, D. (2023). Mass-Editing Memory in a Transformer. ICLR.
3. Fang, J., et al. (2025). AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models. ICLR. Version used: arXiv:2410.02355v3.
4. Zhang, N., et al. (2024). A Comprehensive Study of Knowledge Editing for Large Language Models. Version used: arXiv:2401.01286v5.
5. Gupta, A., Rao, A., and Anumanchipalli, G. (2024). Model Editing at Scale leads to Gradual and Catastrophic Forgetting. Findings of ACL.
6. Gupta, A., Baskaran, S., and Anumanchipalli, G. (2024). Rebuilding ROME: Resolving Model Collapse during Sequential Model Editing. EMNLP.
7. Wang, P., et al. (2023). EasyEdit: An Easy-to-Use Knowledge Editing Framework for Large Language Models. arXiv:2308.07269.
8. Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language Models are Unsupervised Multitask Learners. OpenAI technical report.
9. Zhao, W. X., et al. (2023; revised version consulted). A Survey of Large Language Models. arXiv:2303.18223v16.

**Group Details.** CAI XIAOCHENG (MC651373); KE GUANYU (MC664433); GU YUJIE (MC664973).
