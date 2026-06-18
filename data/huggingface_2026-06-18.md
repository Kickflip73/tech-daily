# HuggingFace 技术热点 — 2026-06-18

> 数据来源：HuggingFace Daily Papers / Models / Spaces
> 抓取时间：2026-06-18 08:08 CST

---

## 🔥 今日热门论文 Top 15（按点赞数排序）

| # | 论文 | 点赞 | 作者 | 机构 | 亮点 |
|---|------|------|------|------|------|
| 1 | **[LoopCoder-v2](https://huggingface.co/papers/2606.18023)** | ⭐113 | Jian Yang 等 (19人) | - | Parallel loop Transformers 在代码生成上实现 SWE-bench Verified 43→64.4，2-loop 效果最佳，3+ loop 反而退化 |
| 2 | **[DreamX-World 1.0](https://huggingface.co/papers/2606.16993)** | ⭐95 | DreamX Team (23人) | AMAP-ML | 通用交互式世界模型，支持长时程可控生成+相机导航，8×RTX 5090 达 16 FPS，整体得分 84.76 超越 HY-WorldPlay 1.5 |
| 3 | **[Ling & Ring 2.6](https://huggingface.co/papers/2606.15079)** | ⭐68 | Ang Li 等 (218人) | inclusionAI | 万亿参数级 Agentic 智能体模型，Ling-2.6 侧重快速响应，Ring-2.6 侧重深度推理，引入 KPop RL 框架 |
| 4 | **[ACE-Ego-0](https://huggingface.co/papers/2606.17200)** | ⭐40 | Hao Li 等 (11人) | CUHK | 统一人眼视角+机器人数据做 VLA 预训练，在 RoboCasa/Real-world bimanual 操作上达到 SOTA |
| 5 | **[ZPPO](https://huggingface.co/papers/2606.18216)** | ⭐40 | Byung-Kwan Lee 等 (11人) | NVIDIA | 受维果茨基近端发展区启发的 RL 蒸馏方法，在 Qwen3.5 0.8B-9B 上全面超越 GRPO，小模型提升最显著 |
| 6 | **[GameCraft-Bench](https://huggingface.co/papers/2606.17861)** | ⭐36 | Tongxu Luo 等 (25人) | CUHK Shenzhen | 140 Godot 游戏生成基准，最强 Agent 仅 41.46% 通过率，揭示端到端游戏生成的巨大挑战 |
| 7 | **[LectūraAgents](https://huggingface.co/papers/2606.16428)** | ⭐31 | Jaward Sesay 等 (6人) | - | 多 Agent 框架模拟教授-学生互动，支持体感教学动作（手写/高亮/划线），个性化学习质量提升显著 |
| 8 | **[TRIAGE](https://huggingface.co/papers/2606.09030)** | ⭐25 | Hyeongwon Jang 等 (6人) | KAIST AI | LLM 医疗风险预测框架，通过辩证推理消除风险极化，AUPRC 提升 3.3%，校准误差降低 81% |
| 9 | **[d-OPSD](https://huggingface.co/papers/2606.18195)** | ⭐24 | Yifu Luo 等 (7人) | Max Planck Institute | 首个针对扩散 LLM 的 OPSD 框架，用"自未来经验"做后缀条件，仅需 RLVR 10% 的优化步数 |
| 10 | **[OPD-Evolver](https://huggingface.co/papers/2606.17628)** | ⭐21 | Guibin Zhang 等 (7人) | NUS | 慢-快协同进化框架，9B 模型挑战 Qwen3.5-397B-A17B，在 ReasoningBank 上领先 11.5% |
| 11 | **[Spectral Forcing](https://huggingface.co/papers/2606.15236)** | ⭐15 | Weichen Fan 等 (4人) | MMLab@NTU | 时间条件 2D-DCT 低通算子，显式分离像素空间扩散模型的信号与噪声，FID+IS 全程提升 |
| 12 | **[MVEB](https://huggingface.co/papers/2606.14958)** | ⭐13 | Adnan El Assadi 等 (16人) | MTEB | 23 任务视频嵌入基准，评估 33 模型，发现不同架构在不同任务各有所长，音频影响取决于数据标注来源 |
| 13 | **[Memento](https://huggingface.co/papers/2606.14667)** | ⭐13 | Xuan Wei 等 (8人) | Baidu | 主体重建引导框架，通过双查询记忆机制保持长视频生成中的人物一致性，视觉质量 SOTA |
| 14 | **[Text-Vision Co-Instructed](https://huggingface.co/papers/2606.16767)** | ⭐12 | Chenxi Xie 等 (4人) | VCLab | 文本+视觉联合指导图像编辑框架 TV-Edit，语义意图+空间约束双管齐下，超越 SOTA |
| 15 | **[SP³](https://huggingface.co/papers/2606.16396)** | ⭐13 | Sean Man 等 (4人) | - | 球面编码器作为生成先验的 Plug-and-Play 图像恢复算法，比 SOTA 零-shot 扩散方法快 3-630 倍 |

---

## 🏆 热门模型 Top 10（按点赞数排序）

| # | 模型 | 作者 | 下载量 | 点赞 | 类型 | 亮点 |
|---|------|------|--------|------|------|------|
| 1 | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | deepseek-ai | 511万+ | ⭐13,394 | 推理模型 | MoE 671B 参数，37B 激活，RL 训练，推理能力顶尖 |
| 2 | [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) | black-forest-labs | 71万+ | ⭐13,231 | 文生图 | 12B rectified flow，图像质量行业标杆 |
| 3 | [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | stabilityai | 108万+ | ⭐7,823 | 文生图 | SDXL 基础版，1024×1024 高清生成 |
| 4 | [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) | meta-llama | 99万+ | ⭐6,578 | 语言模型 | Meta 旗舰开源模型，多语言支持 |
| 5 | [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | hexgrad | 1,356万+ | ⭐6,353 | 语音合成 | 82M 参数 TTS，音质自然，效率极高 |
| 6 | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | meta-llama | 692万+ | ⭐6,103 | 对话模型 | 多语种指令模型，开源生态核心 |
| 7 | [whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | openai | 463万+ | ⭐5,826 | 语音识别 | 117种语言，识别准确率 SOTA |
| 8 | [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) | black-forest-labs | 22万+ | ⭐5,150 | 文生图 | FLUX.1 快速版，12B 参数，生成速度快 |
| 9 | [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 280万+ | ⭐4,924 | 语言模型 | DeepSeek 最新旗舰模型 |
| 10 | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | openai | 316万+ | ⭐4,891 | 语言模型 | OpenAI 开源 120B 巨型模型 |

---

## 🎯 热门 Spaces Top 10（按点赞数排序）

| # | Space | 作者 | 点赞 | 类型 | 亮点 |
|---|-------|------|------|------|------|
| 1 | [deepsite](https://huggingface.co/spaces/enzostvs/deepsite) | enzostvs | ⭐16,617 | Docker | AI 驱动的网站生成 |
| 2 | [open_llm_leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | open-llm-leaderboard | ⭐14,025 | Leaderboard | LLM 排行榜 |
| 3 | [ai-comic-factory](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory) | jbilcke-hf | ⭐11,125 | Docker | AI 漫画工厂 |
| 4 | [Kolors-Virtual-Try-On](https://huggingface.co/spaces/Kwai-Kolors/Kolors-Virtual-Try-On) | Kwai-Kolors | ⭐10,107 | Gradio | 快手虚拟试穿 |
| 5 | [FLUX.1-dev](https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev) | black-forest-labs | ⭐9,469 | Gradio | FLUX.1 在线体验 |
| 6 | [mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard) | mteb | ⭐7,479 | Leaderboard | 文本嵌入排行榜 |
| 7 | [dalle-mini](https://huggingface.co/spaces/dalle-mini/dalle-mini) | dalle-mini | ⭐5,690 | Static | DALL-E mini |
| 8 | [IllusionDiffusion](https://huggingface.co/spaces/AP123/IllusionDiffusion) | AP123 | ⭐5,413 | Gradio | 幻觉扩散生成 |
| 9 | [Wan2.2-Animate](https://huggingface.co/spaces/Wan-AI/Wan2.2-Animate) | Wan-AI | ⭐5,115 | Gradio | 视频动画生成 |
| 10 | [MusicGen](https://huggingface.co/spaces/facebook/MusicGen) | facebook | ⭐5,073 | Gradio | Meta 音乐生成 |

---

## 📊 今日观察

1. **代码生成赛道升温**：LoopCoder-v2 以 113 点赞登顶，2-loop 架构在 SWE-bench 上 43→64.4 的飞跃引发广泛关注
2. **世界模型+视频生成持续火热**：DreamX-World 1.0 (95)、Memento (13) 均聚焦长时程视频/世界生成
3. **Agent 智能体研究爆发**：Ling & Ring 2.6 (68)、ACE-Ego-0 (40)、OPD-Evolver (21) 三篇 Agent 相关论文上榜
4. **蒸馏/训练方法创新**：ZPPO (40)、d-OPSD (24) 展示了新的知识蒸馏范式
5. **医疗+教育 AI 跨界**：TRIAGE (25) 医疗风险预测、LectūraAgents (31) 个性化教学均受关注
6. **DeepSeek 生态持续强势**：R1 (13,394 赞)、V4-Pro (4,924)、Janus-Pro (3,616) 均入榜

---

*数据由 J.A.R.V.I.S. 自动抓取并整理* 🤖
