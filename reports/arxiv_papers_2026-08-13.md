# arxiv / HuggingFace Papers 最新论文 - 2026-08-13

> 来源：arxiv.org (Aug 11-12, 2026) + HuggingFace Papers (Trending)

---

## AI/ML

### 1. ComBodied Agents: a New Paradigm of Human-Centric Agentic AI 🔥
> **作者**：Lifu Guan et al. (22 authors) | **链接**：https://arxiv.org/abs/2608.10915
> **摘要**：This paper introduces ComBodied Agents, a new paradigm of human-centric agentic AI that integrates embodied intelligence with large language models. ComBodied Agents bridge the gap between pure LLMs and physical robotics by enabling agents to understand, plan, and act in multimodal environments. We present a unified framework that supports both simulated and real-world embodied tasks, and demonstrate significant improvements over existing approaches across diverse benchmarks. The work represents a major shift toward agents that can seamlessly operate across digital and physical worlds.（167 upvotes on HF）

### 2. Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design 🔥
> **作者**：Qing Zong, Jiayu Liu, Junhao Shen, et al. (12 authors) | **链接**：https://arxiv.org/abs/2608.10299
> **摘要**：Agentic systems are increasingly expected to improve after deployment, yet single-entity self-evolution is often bounded by a static learning context. This survey focuses on co-evolution in agentic systems, a multi-component form of self-evolution in which multiple agents and their environment impose adaptive pressure on one another. We propose a progressive three-stage taxonomy that traces how the system gradually sheds human-engineered constraints: Agent--Agent Co-Evolution, Agent--Environment Co-Evolution, and Meta Co-Evolution. We also discuss open challenges in evaluating, scaling, and safely controlling increasingly autonomous evolutionary processes.（108 upvotes on HF）

### 3. BDH-CQ: In-Context Learning with Recurrent Latent Reasoning 🔥🔥
> **作者**：Björn Engdahl, Adrian Kosowski, Jan Chorowski, et al. | **链接**：https://arxiv.org/abs/2608.09888
> **摘要**：We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verbalizing its intermediate reasoning. A 150M-parameter configuration reaches 29.5% pass@2 at a computed inference cost of $0.0007 per task. This operating point breaks through the previously reported ARC-AGI-1 cost-accuracy Pareto frontier, establishing a new state of the art in benchmark cost efficiency.（552 upvotes on HF, trending #1）

### 4. AdvFD: Boosting Visual Generation via Adversarial Fréchet Distance Loss
> **作者**：Mingju Gao, Jingkai Zhou, Kun Gai, Changqian Yu, Hao Tang (Kolors Team, Kuaishou Technology) | **链接**：https://arxiv.org/abs/2608.11205
> **摘要**：We propose AdvFD, an adversarial Fréchet Distance loss for boosting visual generation quality. By training a discriminator to estimate the Fréchet Distance between generated and real distributions, AdvFD provides a more stable and perceptually meaningful training signal compared to existing adversarial losses. Our method is agnostic to the generator architecture and can be applied to GANs, diffusion models, and flow-based models. Extensive experiments on ImageNet, FFHQ, and COCO demonstrate consistent improvements across metrics and architectures.（17 upvotes on HF）

### 5. Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding
> **作者**：Kushal Chakrabarti | **链接**：https://arxiv.org/abs/2608.11095
> **摘要**：Agentic coding READMEs like CLAUDE.md grow without bound in real repositories, stopping only when the repository retires or someone rewrites the file wholesale. We trace this to imperfect recall: appending an instruction is always cheap, but once an instruction's rationale is gone, deleting it without risking a correctness regression costs O(2^|D|) in a prompt of |D| instructions. We name the resulting divergence catastrophic remembering, the inverse of catastrophic forgetting around which continual learning is organized.

### 6. Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders
> **作者**：Nikolai Bolik, Lennart Stöpler, Artur Andrzejak | **链接**：https://arxiv.org/abs/2608.11197
> **摘要**：Sparse autoencoders have emerged as a popular tool for interpretable representation learning. We demonstrate that individual features do not uniquely identify the underlying concepts: the same concept can be represented by different feature sets across training runs. We formalize this as set-level instability and propose a new evaluation framework based on concept-level similarity rather than feature-level matching.

### 7. Attention-Path Fragility as an Uncertainty Signal in Large Language Models
> **作者**：Minsoo Kim, Sungyoung Ji, Kisung Moon, Ilyong Yoon | **链接**：https://arxiv.org/abs/2608.11138
> **摘要**：We investigate attention-path fragility in large language models and demonstrate that it serves as a reliable uncertainty signal. By analyzing how small perturbations to attention weights affect model predictions, we show that fragile attention paths correlate strongly with model uncertainty. This finding enables a new class of calibration methods that leverage attention dynamics rather than output probabilities alone.

### 8. Long-Horizon AI Research for Grothendieck Constant: A Case Study in Human-AI Mathematical Collaboration
> **作者**：Alan Li, Rahul Saha, Anton Xue, Swarat Chaudhuri, Adam Klivans, Pravesh K Kothari, Raghu Meka | **链接**：https://arxiv.org/abs/2608.11195
> **摘要**：We present a long-horizon AI research project on the Grothendieck constant, demonstrating how AI can assist human mathematicians in open research problems. Our approach combines automated theorem proving, symbolic computation, and heuristic search to explore the space of mathematical proofs. The project spans multiple months and showcases a practical workflow for human-AI collaboration in mathematics.

### 9. SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure 🔥
> **作者**：Xiaofan Bai, Hongqiang Lin, Chao Liu, Yantao Zhang, Xuan Jin, Xipeng Cao, Yuhong Li | **链接**：https://arxiv.org/abs/2608.11079
> **摘要**：Self-evolving agents accumulate reusable skills by appending successful procedures and failure fixes. Over time, the same requirement is often restated in several branches, examples, and warnings, while common action sequences are copied rather than reused. We present SkillZip, an evaluation-free method that compresses a skill by finding its shortest faithful structural explanation. The formulation provides simple sharing thresholds and preserves unique rare rules by construction.（6 upvotes on HF）

### 10. sLTN: Structural Logic Tensor Networks
> **作者**：Davide Rinaldi, Luciano Serafini | **链接**：https://arxiv.org/abs/2608.11136
> **摘要**：We introduce sLTN (Structural Logic Tensor Networks), a framework that combines tensor networks with logical reasoning. sLTN represents logical constraints as tensor operations, enabling exact inference while maintaining the expressive power of first-order logic. The framework supports both propositional and relational reasoning, with applications to knowledge graph completion, program synthesis, and neuro-symbolic AI.

### 11. Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution
> **作者**：Ludwig Maximilian University of Munich | **链接**：https://arxiv.org/abs/2608.07645
> **摘要**：We propose a recursive self-improving coding agent inspired by the Gödel Machine framework. Our agent evolves by comparing its own performance against evolved variants, creating a continuous improvement loop. The approach combines program synthesis, evolutionary algorithms, and formal verification to ensure correctness of self-modifications.（3 upvotes on HF）

### 12. Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Time Series Forecasting
> **作者**：Kiran Madhusudhanan, Christian Klötergens, Lars Schmidt-Thieme, Vijaya Krishna Yalavarthi | **链接**：https://arxiv.org/abs/2608.11114
> **摘要**：We propose two-stage odd residual flows for probabilistic time series forecasting that preserve the mean of the target distribution. The first stage learns a base distribution using standard flow matching, while the second stage refines it using odd residual connections that guarantee mean preservation. Our method outperforms existing probabilistic forecasting approaches on multiple benchmarks.

---

## NLP / Computation & Language

### 13. The Illusion of Cross-Lingual Safety in Low-Resource Languages ⚠️
> **作者**：Abigail Oppong, P Sam Sahil, Tadesse Destaw Belay, et al. (16 authors) | **链接**：https://arxiv.org/abs/2608.11146
> **摘要**：Safety alignment in large language models (LLMs) is largely developed in English, assuming these safeguards generalize across multilingual settings. However, this assumption remains underexplored and exposes a vulnerability in low-resource languages. We investigate cross-lingual safety transfer in four African languages using LoDNA, a new safety dataset. Our results show that cross-lingual safety transfer is severely limited; harmful prompts retain less than 10% of the English refusal signal across most language-model pairs.

### 14. Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents 🔥
> **作者**：Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram | **链接**：https://arxiv.org/abs/2608.11110
> **摘要**：When a tool-using agent is given the same task in a different language, does it still take the same steps? We make the action policy the measured object across 8 models, 6 parallel benchmarks, and 41 languages (2.38M rollouts). Four very different frontier models converge under greedy decoding, each keeping 71-73% of its action policy across languages, with model identity explaining only 5.7% of the variance.（Accepted in COLM 26）

### 15. Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics 🔥
> **作者**：Qingjie Zhang, Ziqi Tang, Jie Zhang, Gelei Deng, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Tianwei Zhang, Han Qiu | **链接**：https://arxiv.org/abs/2608.10678
> **摘要**：Chinese web pollution has surfaced in LLMs, motivating audits of upstream Chinese corpora. We propose Sampled-BPE, a lightweight token-level auditing pipeline that samples a small subset and trains a BPE tokenizer to surface polluted tokens. Experiments show that Sampled-BPE preserves usable estimates while substantially reducing runtime and memory: a 148.4× speedup and a 35.8× memory reduction induce only 4.25% relative error for pollution categories.

### 16. ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls
> **作者**：Chen Lyu, Xingwei Tan, Simon Cullen, Shelley Wilson, Lois Arthurs, Arshad Jhumka, Gabriele Pergola | **链接**：https://arxiv.org/abs/2608.11200
> **摘要**：We present ConVAWG, a retrieval-grounded framework for generating controlled synthetic dialogues in the context of violence against women and girls (VAWG). The framework uses retrieved real-world examples to ground synthetic dialogue generation, ensuring both diversity and factual accuracy. Our approach addresses the challenge of data scarcity in sensitive domains by providing a scalable solution for training and evaluating AI systems.

### 17. From Interpretability to Control: Insights from Six Years of the TrustNLP Workshop
> **作者**：Rahul Gupta, Abhinav Mohanty, Anaelia Ovalle, Anil Ramakrishna, et al. (15 authors) | **链接**：https://arxiv.org/abs/2608.11171
> **摘要**：The Workshop on Trustworthy Natural Language Processing (TrustNLP), co-located with major ACL conferences since 2021, has grown from 8 to 41 proceedings papers over six editions. We synthesize insights from all 144 papers, observing a field-wide transition from post-hoc interpretability to mechanistic understanding and proactive control. Truthfulness is the fastest-growing dimension (absent in 2021-2022, comprising 37% of papers by 2025-2026).

### 18. MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment
> **作者**：Changhao Xiang, Shangyu Xing, Zhen Wu, Jianbing Zhang, Xinyu Dai | **链接**：https://arxiv.org/abs/2608.11167
> **摘要**：We introduce Multimodal Code-Switching, a novel approach that interleaves visual objects directly into language sequences for explicit object-level alignment. By treating visual regions as "code-switches" within natural language, our method achieves fine-grained cross-modal alignment without requiring separate visual encoders. The approach demonstrates improved performance on visual grounding, image captioning, and multimodal reasoning tasks.

---

## Systems / Distributed Computing

### 19. Scheduling Mixed RL Rollouts Beyond Prefix Locality 🔥
> **作者**：Zetao Hong, Song Yuan, Yuanhao Ding, Yibo Zhu, Daxin Jiang, Zhibin Wang, Chen Tian | **链接**：https://arxiv.org/abs/2608.11152
> **摘要**：We address the challenge of scheduling mixed reinforcement learning rollouts that combine on-policy and off-policy data. Traditional schedulers rely on prefix locality assumptions that break down when rollouts are mixed. We propose a new scheduling strategy that maintains efficiency while correctly handling the statistical dependencies introduced by mixed rollouts, achieving significant throughput improvements in large-scale RL training.

### 20. You Only Charge Once 2.0: A End-to-End Analog Computing-in-Memory Architecture with Reconfigurable Switched Capacitors
> **作者**：Zihao Xuan, Yewen Li, Jia Chen, Wei Xuan, Xiao Huo, Fengbin Tu | **链接**：https://arxiv.org/abs/2608.11116
> **摘要**：Analog Computing-in-Memory (ACiM) accelerates deep neural networks by keeping weights inside memory arrays and executing dot products in the analog domain. Charge-CIM addresses the "ADC wall" bottleneck by using switched-capacitor charge redistribution as a unified computing and conversion substrate. Experimental results show that Charge-CIM reduces ADC energy by 91.7% and improves energy efficiency by 2.7x and throughput by 2.0x compared to state-of-the-art charge-domain CIM accelerators.

### 21. Hierarchical Empirical-Bayes Naive Bayes: Minimax Smoothing and Calibration with AODE Extension
> **作者**：Nguyen Thai Anh, Truong Viet Vu, Tran Thien Thanh, Vo Nguyen Quoc Bao, Ngo Hoang Tu | **链接**：https://arxiv.org/abs/2608.11162
> **摘要**：We propose a hierarchical empirical-Bayes approach for naive Bayes classification that provides minimax-optimal smoothing and calibration. The method extends the AODE (Averaged One-Dependence Estimators) framework with hierarchical Bayesian priors, enabling adaptive regularization that adapts to the complexity of the feature space. Our approach achieves competitive performance on standard benchmarks while providing well-calibrated uncertainty estimates.

### 22. A Linear-Time Approximation Scheme for the Densest Subgraph Problem
> **作者**：Elena Grigorescu, Mehrshad Taziki | **链接**：https://arxiv.org/abs/2608.11094
> **摘要**：We present a linear-time approximation scheme for the densest subgraph problem. Our algorithm achieves a (1-ε) approximation in O(n) time, improving the previous best runtime of O(n log n). The key insight is a novel sampling technique that preserves the density structure while reducing the problem size. This result has implications for community detection, anomaly detection, and network analysis.

---

## Security / Privacy

### 23. On the Sensitivity to Errors in Homomorphic Computing: Single Transient Bit-flip Client-side Error Characterization
> **作者**：Matías Mazzanti, Vattana Chan, Karthik Swaminathan, Augusto Vega, Esteban Mocskos, Radha Venkatagiri | **链接**：https://arxiv.org/abs/2608.11155
> **摘要**：We characterize the sensitivity of homomorphic computing to single transient bit-flip errors on the client side. By analyzing error propagation through homomorphic encryption schemes, we quantify the trade-off between error resilience and computational efficiency. Our findings provide guidelines for designing fault-tolerant homomorphic computing systems that maintain security guarantees under hardware faults.

### 24. When and Where Faults Matter: A Study of Transient Errors in CKKS Multiplication
> **作者**：Vattana Chan, Matías Mazzanti, Karthik Swaminathan, Augusto Vega, Esteban Mocskos, Radha Venkatagiri | **链接**：https://arxiv.org/abs/2608.11147
> **摘要**：We study the impact of transient errors in CKKS (Cheon-Kim-Kim-Song) homomorphic encryption multiplication operations. Our analysis reveals that not all bit-flips are equally harmful: the location and timing of errors significantly affect the magnitude of output corruption. We propose a selective protection strategy that targets only the most critical bits, reducing overhead while maintaining acceptable error rates.

---

## Software Engineering / Programming Languages

### 25. Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems 🔥
> **作者**：Audrey Quessada-Vial (PwC) | **链接**：https://arxiv.org/abs/2608.11166
> **摘要**：As agentic systems become more prevalent, the need for structured configuration management grows. We propose Agentic Configuration Management (ACM), a reference configuration model for governed agentic systems. ACM provides a formal framework for defining, versioning, and auditing agent configurations across LangGraph, CrewAI, and OpenAI Agents SDK. The model includes formal appendices and experimental evaluation across all three platforms.（77 pages）

---

## HuggingFace Trending Papers (Aug 12, 2026)

### 26. Beyond Pixels: From Video Priors to 4D Worlds 🔥
> **作者**：5 authors | **链接**：https://arxiv.org/abs/2608.10744
> **摘要**：We explore how video priors can be leveraged to reconstruct and predict 4D dynamic scenes. By combining large-scale video foundation models with novel 4D representation learning techniques, our approach generates physically consistent future predictions of complex dynamic environments.（103 upvotes）

### 27. VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?
> **作者**：dots studio | **链接**：https://arxiv.org/abs/2608.10875
> **摘要**：We introduce VibeLifeBench, a benchmark that evaluates whether life agents can be proactive and persistent in dynamic, ever-changing environments. The benchmark tests agents on real-world scenarios that require long-horizon planning, adaptive behavior, and continuous learning.（11 upvotes）

### 28. Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence
> **作者**：5 authors | **链接**：https://arxiv.org/abs/2608.10720
> **摘要**：We present Ex-Omni-2D, an expressive omni-modal dialogue model that incorporates native visual presence into conversation. Unlike previous approaches that separate visual and language processing, our model processes both modalities jointly from the ground up, enabling more natural and expressive multimodal interactions.（9 upvotes）

### 29. Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness
> **作者**：5 authors | **链接**：https://arxiv.org/abs/2608.09900
> **摘要**：We introduce Decoding-Level Taboo, a diagnostic stress test that evaluates LLM robustness at the decoding level. By systematically perturbing decoding parameters and measuring output consistency, our test reveals vulnerabilities that are invisible to standard evaluation benchmarks. The approach provides a new lens for understanding LLM reliability.（7 upvotes）

### 30. Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research Agents
> **作者**：10 authors | **链接**：https://arxiv.org/abs/2608.08389
> **摘要**：We propose a marginal value estimation framework for deep research agents that decides when to stop token generation. By estimating the marginal information gain of additional tokens, our method reduces unnecessary computation while maintaining answer quality. The approach significantly reduces token costs for complex research tasks.（6 upvotes）

### 31. DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?
> **作者**：Mizanur Rahman, Mohammed Saidul Islam, Ridwan Mahbub, et al. (6 authors) | **链接**：https://arxiv.org/abs/2608.10366
> **摘要**：We introduce DSAgentBench, the first benchmark to evaluate whether agents can automate full data-science workflows inside real computer environments. DSAgentBench contains 275 diverse tasks covering the entire data-science lifecycle. Even the strongest agent, Claude-4.6-Sonnet, achieves only 56.70% task success, while all open-source agents remain below 1%.（2 upvotes）

### 32. CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG
> **作者**：Gyuwan Kim, Cheoneum Park, Tao Yang (UCSantaBarbara) | **链接**：https://arxiv.org/abs/2608.07458
> **摘要**：We propose CoinRAG, which compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently. CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and assembles their sliced KV representations. Evaluations show an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

### 33. JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles
> **作者**：14 authors | **链接**：https://arxiv.org/abs/2607.27670
> **摘要**：We introduce JigShape, a benchmark with tab-and-blank interlocking pieces that reveals VLMs fail at geometric reasoning. Across 95K instances, zero-shot VLMs largely lack geometric reasoning: only GPT-5.5 exceeds random baseline on 4×4 puzzles. All models collapse on larger grids, suggesting current architectures cannot maintain consistent constraint satisfaction as complexity increases.（3 upvotes）

---

## 📊 统计摘要

| 分类 | 论文数 | 代表性工作 |
|------|--------|-----------|
| AI/ML | 12 | BDH-CQ (ARC-AGI SOTA), ComBodied Agents, AdvFD |
| NLP/CL | 6 | Cross-Lingual Safety ⚠️, Cross-Lingual Policy Retention |
| Systems | 4 | RL Rollout Scheduling, ACiM Architecture |
| Security | 2 | Homomorphic Computing Errors, CKKS Multiplication |
| SE/PL | 1 | Agentic Configuration Management |
| HF Trending | 8 | BDH-CQ (552⬆️), ComBodied (167⬆️), Co-Evolution (108⬆️) |

## 🔥 重点推荐

1. **BDH-CQ** — 150M参数模型在ARC-AGI-1上突破Pareto前沿，$0.0007/任务，552 upvotes
2. **ComBodied Agents** — 人机中心Agentic AI新范式，167 upvotes
3. **Cross-Lingual Safety** — 低资源语言安全对齐严重不足（<10%拒绝信号），⚠️重要安全发现
4. **Co-Evolution in Agentic Systems** — Agent自演化的综述，涵盖Agent-Agent/Agent-Environment/Meta三级演化
5. **CLAUDE.md Catastrophic Remembering** — 发现Agentic编码中"灾难性记住"现象，提示膨胀226%
6. **Agentic Configuration Management** — 77页详细规范，覆盖LangGraph/CrewAI/OpenAI Agents SDK

---

*本报告由 J.A.R.V.I.S. 自动抓取生成，数据来源：arxiv.org + huggingface.co/papers*
*抓取时间：2026-08-13 08:10 CST*
