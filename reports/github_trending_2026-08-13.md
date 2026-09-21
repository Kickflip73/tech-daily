# GitHub Trending 数据 - 2026-08-13

> 数据采集时间：2026-08-13 08:08 GMT+8  
> 来源：https://github.com/trending（全语言）及 https://github.com/trending?l=python

---

## 全语言热门

### 1. cathrynlavery/diagram-design（⭐+2,855，总⭐10,272）
- **链接**：https://github.com/cathrynlavery/diagram-design
- **语言**：HTML | **协议**：MIT
- **描述**：29 editorial diagram types for Claude Code. Self-contained HTML + SVG. No shadows, no Mermaid-slop.
- **今日新增**：+2,855
- **技术亮点**：为 Claude Code 设计的 29 种专业图表类型，全部基于 HTML + SVG 自包含输出，无需 Figma 或 Mermaid。支持品牌色自动匹配、静态/动态两种模式。
- **详细解读素材**：
  - 面向 AI 编码助手的可视化技能包（Claude Code / Codex / Pi 插件）
  - 27+ 种图表类型：架构图、流程图、时序图、状态机、ER 模型、甘特图、雷达图等
  - 语义系统模式（semantic system patterns）将行为描述与布局分离
  - 可将 draw.io / Mermaid 源文件重绘为指定格式和尺寸
  - 目标密度 4/10，强调删除而非堆砌

---

### 2. stablyai/orca（⭐+1,235，总⭐43,839）
- **链接**：https://github.com/stablyai/orca
- **语言**：TypeScript | **协议**：MIT
- **描述**：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.
- **今日新增**：+1,235
- **技术亮点**：多 Agent 并行编排 IDE（ADE = Agent Development Environment），支持在同一工作区运行 Claude Code、Codex、Cursor、Pi 等 20+ 编码 Agent，各 Agent 拥有独立 git worktree。
- **详细解读素材**：
  - **核心架构**：Electron + React UI，基于 Ghostty 类终端（WebGL 渲染），支持无限分屏
  - **Parallel Worktrees**：一个 Prompt 可分发到 5 个 Agent，各自在独立 git worktree 中执行，可比较结果并合并最优解
  - **Design Mode**：内置 Chromium 窗口，点击任意 UI 元素即可将其 HTML/CSS/截图直接送入 Agent Prompt
  - **Mobile Companion**：iOS/Android App，可远程监控和指挥 Agent 执行
  - **支持 Agent 列表**：Claude Code、Codex、Grok、Cursor、GitHub Copilot、OpenCode、MiMo、Hermes、Devin、Goose、Cline 等 20+
  - **Orca CLI**：`orca worktree create/snapshot/click/fill` 等命令，Agent 也能驱动 Orca
  - SSH Worktrees 支持远程服务器上运行 Agent，自带自动重连和端口转发

---

### 3. msitarzewski/agency-agents（⭐+1,873，总⭐144,550）
- **链接**：https://github.com/msitarzewski/agency-agents
- **语言**：Shell | **协议**：MIT
- **描述**：A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **今日新增**：+1,873
- **技术亮点**：超大规模 AI Agent 人格库，包含 100+ 个专业领域 Agent 模板，覆盖工程、安全、营销、产品、金融等 20+ 部门。
- **详细解读素材**：
  - **规模**：23,418 forks，是目前最大的开源 Agent 人格集合
  - **多工具支持**：一键安装到 Claude Code、Cursor、Codex、GitHub Copilot、OpenClaw、Aider、Windsurf、Kimi、Hermes 等 15+ 工具
  - **部门覆盖**：Engineering（前端/后端/DevOps/AI/安全）、Marketing、Sales、Product、Finance、Healthcare、Game Dev、GIS 等
  - **Agent 示例**：Frontend Developer、Backend Architect、AI Engineer、DevOps Automator、SRE、Solidity Smart Contract Engineer、Prompt Engineer、Multi-Agent Systems Architect
  - 提供原生桌面 App（macOS/Linux/Windows）一键浏览和安装
  - 每个 Agent 包含身份定义、核心使命、技术交付物、成功指标和沟通风格

---

### 4. paperclipai/paperclip（⭐+571，总⭐77,715）
- **链接**：https://github.com/paperclipai/paperclip
- **语言**：TypeScript | **协议**：MIT
- **描述**：The open-source app everyone uses to manage agents at work
- **今日新增**：+571
- **技术亮点**：AI Agent 企业级编排平台，类比"如果 OpenClaw 是员工，Paperclip 就是公司"。提供组织架构、预算控制、审批流程、目标对齐等企业级治理能力。
- **详细解读素材**：
  - **四大支柱**：Agentic Task Manager、Org Chart for Agents、Agent Employee Training、Agentic OS
  - **Bring Your Own Agent**：支持 Claude Code、Codex、OpenClaw、Cursor、Bash、HTTP/webhook 等任意 Agent
  - **Goal Alignment**：每个任务可追溯回公司使命，Agent 知道做什么以及为什么做
  - **Heartbeats**：Agent 按 schedule 唤醒、检查工作并执行，支持层级委托
  - **Cost Control**：每个 Agent 月度预算上限，超支自动停止
  - **Multi-Company**：一次部署，多家公司，数据完全隔离
  - **Ticket System**：每次对话可追溯，每个决策可解释，完整 tool-call tracing
  - **Governance**：审批雇佣、覆盖策略、随时暂停/终止任意 Agent

---

### 5. semantica-agi/semantica（⭐+845，总⭐5,698）
- **链接**：https://github.com/semantica-agi/semantica
- **语言**：Python | **协议**：MIT
- **描述**：Graph-Native Infrastructure for Context and Accountable AI Systems
- **今日新增**：+845
- **技术亮点**：面向高监管领域的确定性 AI 决策基础设施，自称为"开源版 Palantir for AI Agents"。核心特色：无需 LLM 即可构建知识图谱、因果推理和完整审计追踪。
- **详细解读素材**：
  - **Context Graphs**：结构化、可查询的 Agent 知识图谱，存储 Agent 知道、决定和推理的一切
  - **Decision Intelligence**：每个 AI 决策是一等公民对象，可追溯、可搜索先例、因果关联
  - **确定性推理**：前向链（Forward Chaining）、Rete 网络、Datalog、SPARQL — 完全可解释
  - **完整审计**：W3C PROV-O 来源追溯，支持导出 JSON/CSV/RDF 供监管提交
  - **冲突检测**：冲突事实被标记而非静默覆盖，支持语义去重
  - **Polyglot Graph Storage**：RDF（Oxigraph/Blazegraph/Jena）+ LPG（Neo4j/FalkorDB/AGE/Neptune）
  - **企业数据平台连接器**：Databricks（Unity Catalog + Delta Lake）和 Snowflake 原生集成
  - **MCP Server**：提供完整的 MCP 服务器实现

---

### 6. NVIDIA-NeMo/Switchyard（⭐+421，总⭐813）
- **链接**：https://github.com/NVIDIA-NeMo/Switchyard
- **语言**：Rust | **协议**：Apache 2.0
- **描述**：Rust proxy and library for LLM traffic. Routes requests across providers, translates between OpenAI and Anthropic APIs.
- **今日新增**：+421
- **技术亮点**：NVIDIA 出品的 LLM 流量路由代理，用 Rust 编写。核心解决多模型后端统一接入问题，让编码 Agent 用原生 API 说话，后端可切换 vLLM/NIM/Ollama/任何 OpenAI 兼容端点。
- **详细解读素材**：
  - **协议转换**：OpenAI Chat ↔ Anthropic Messages ↔ OpenAI Responses 格式互转
  - **路由策略**：随机路由、LLM-as-classifier 路由、信号驱动 stage-router、自定义算法
  - **Launcher Path**：`switchyard launch claude/codex/openclaw --model switchyard`
  - **Server Path**：独立 Rust 代理服务器，支持 TOML 配置路由规则
  - **Library Path**：`switchyard-libsy` 可嵌入现有代理/网关/Agent 运行时
  - **Prometheus Metrics**：请求、错误、延迟、token、路由开销全覆盖
  - **状态**：pre-alpha，API 和算法在 v1.0 前可能大幅变化

---

### 7. cactus-compute/needle（⭐+315，总⭐4,210）
- **链接**：https://github.com/cactus-compute/needle
- **语言**：Python | **协议**：MIT
- **描述**：14MB foundation model for tiny devices; phones, wearables, smart home, and robots.
- **今日新增**：+315
- **技术亮点**：仅 45M 参数、14MB 单二进制文件、28MB RAM 运行的端侧工具调用模型。基于 Simple Attention Network 和 CQ2-bit 量化，在 Function Calling 基准上与 5x~70x 更大的模型竞争。
- **详细解读素材**：
  - **核心架构**：Hadamard MLP 替代 FFN、GQA Attention、Engram KV Memory、多通道 Hyper-Connections
  - **工具调用**：通过 `@needle.tool` 装饰器声明工具，模型自动选择调用并填充参数
  - **Confidence Gating**：每个响应携带校准置信度分数，可设阈值自动升级或降级处理
  - **Tool Retrieval**：大规模工具目录下，内置检索头每轮只渲染 Top-5 相关工具
  - **Bounded Memory**：256-token 滑动窗口 + 工具固定为 KV Sinks，无论对话多长内存稳定在 ~28MB
  - **Fine-tuning**：支持 LoRA 在冻结基座上微调，导出为单 .cact 文件
  - **Playground**：`needle playground` 启动浏览器交互界面

---

### 8. embabel/embabel-agent（⭐+40，总⭐4,219）
- **链接**：https://github.com/embabel/embabel-agent
- **语言**：Kotlin | **协议**：Apache 2.0
- **描述**：Agent framework for the JVM. Pronounced Em-BAY-bel /ɛmˈbeɪbəl/
- **今日新增**：+40
- **技术亮点**：由 Spring 框架作者打造的企业级 JVM Agent 框架。核心特色：基于 OODA 循环的动态规划（非 LLM 算法），强类型领域模型驱动，支持 LLM 与代码的无缝混合。
- **详细解读素材**：
  - **核心概念**：Actions（Agent 步骤）、Goals（目标）、Conditions（条件评估）、Domain Model（领域对象）、Plan（动态规划序列）
  - **动态规划**：超越有限状态机，使用非 LLM AI 算法自动组合已知步骤完成新任务
  - **强类型**：Prompt 和代码通过领域模型干净交互，享受完整 IDE 重构支持，告别魔法 Map
  - **Spring 集成**：Spring 注入和管理 Agent，支持 @Autowired Agent
  - **多平台抽象**：本地开发和生产部署代码不变，潜在提供更高 QoS
  - **LLM 混合**：可为不同任务选择不同模型，本地小模型处理点任务以节省成本和保护隐私
  - **模块化架构**：embabel-agent-api / -common / -code / -mcp / -a2a / -anthropic / -openai / -rag / -shell 等 15+ 子模块

---

### 9. hugohe3/ppt-master（⭐+476，总⭐45,542）
- **链接**：https://github.com/hugohe3/ppt-master
- **语言**：Python | **协议**：MIT
- **描述**：AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates.
- **今日新增**：+476
- **技术亮点**：将文档或主题转换为真正原生可编辑的 PowerPoint，支持原生形状、过渡动画、数据图表、音频旁白，以及自定义 .pptx 模板。

---

### 10. infiniflow/ragflow（⭐+139，总⭐87,536）
- **链接**：https://github.com/infiniflow/ragflow
- **语言**：Go | **协议**：Apache 2.0
- **描述**：RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **今日新增**：+139
- **技术亮点**：开源 RAG + Agent 融合引擎，支持多数据源同步（Confluence/S3/Notion/Discord/Google Drive）、Memory 记忆、MCP 工具调用、代码执行组件。87k+ stars，国内团队出品。

---

### 11. shiyu-coder/Kronos（⭐+266，总⭐36,934）
- **链接**：https://github.com/shiyu-coder/Kronos
- **语言**：Python | **协议**：未标注
- **描述**：Kronos: A Foundation Model for the Language of Financial Markets
- **今日新增**：+266
- **技术亮点**：金融市场语言的基础模型，用于金融时序数据理解和预测。

---

### 12. macro-inc/macro（⭐+227，总⭐1,768）
- **链接**：https://github.com/macro-inc/macro
- **语言**：Rust | **协议**：AGPL-3.0
- **描述**：Macro is a unified workspace for teams: email, chat, docs, tasks, agents, calls, and CRM — @-linked together with shared AI memory.
- **今日新增**：+227
- **技术亮点**：SolidJS + Rust 构建的团队统一工作空间，将邮件、消息、文档、任务、Agent、通话、CRM 融为一体。双向图存储所有跨引用关系。核心设计哲学：公司应该是"可计算的"。
- **详细解读素材**：
  - **Block 架构**：Email / Messages / Tasks / Docs（CRDT 实时协作）/ Canvas（2D 画板）/ Agents / Calls / File Storage / PR / CRM
  - **统一 AI Memory**：Agent 可跨所有模块检索和操作用户数据
  - **键盘优先**：Superhuman 风格的快捷键，统一 inbox 管理所有通知
  - **多账号邮箱**：支持多 Google 账号统一 triage
  - **CRM**：客户和联系人对象，自定义属性，邮件同步，自动丰富

---

### 13. localsend/localsend（⭐+213，总⭐87,801）
- **链接**：https://github.com/localsend/localsend
- **语言**：Dart | **协议**：MIT
- **描述**：An open-source cross-platform alternative to AirDrop
- **今日新增**：+213
- **技术亮点**：跨平台文件传输工具，AirDrop 的开源替代方案，支持局域网内设备间快速安全传输。

---

### 14. Lightricks/LTX-2（⭐+65，总⭐8,702）
- **链接**：https://github.com/Lightricks/LTX-2
- **语言**：Python | **协议**：未标注
- **描述**：Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model.
- **今日新增**：+65
- **技术亮点**：LTX-2 音视频生成模型的官方推理和 LoRA 训练包，Lightricks 出品。

---

### 15. smicallef/spiderfoot（⭐+74，总⭐20,341）
- **链接**：https://github.com/smicallef/spiderfoot
- **语言**：Python | **协议**：未标注
- **描述**：SpiderFoot automates OSINT for threat intelligence and mapping your attack surface.
- **今日新增**：+74
- **技术亮点**：自动化开源情报（OSINT）收集工具，用于威胁情报和攻击面映射，安全领域经典项目。

---

## Python 专项热门

### 1. semantica-agi/semantica（⭐+845，总⭐5,698）
- **链接**：https://github.com/semantica-agi/semantica
- **语言**：Python | **协议**：MIT
- **描述**：Graph-Native Infrastructure for Context and Accountable AI Systems
- **今日新增**：+845
- **技术亮点**：见全语言部分 #5

---

### 2. shiyu-coder/Kronos（⭐+266，总⭐36,934）
- **链接**：https://github.com/shiyu-coder/Kronos
- **语言**：Python | **协议**：未标注
- **描述**：Kronos: A Foundation Model for the Language of Financial Markets
- **今日新增**：+266

---

### 3. NanmiCoder/MediaCrawler（⭐+215，总⭐61,956）
- **链接**：https://github.com/NanmiCoder/MediaCrawler
- **语言**：Python | **协议**：未标注
- **描述**：小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫
- **今日新增**：+215
- **技术亮点**：国内主流社交平台爬虫合集，覆盖小红书、抖音、快手、B站、微博、贴吧、知乎。

---

### 4. hugohe3/ppt-master（⭐+476，总⭐45,542）
- **链接**：https://github.com/hugohe3/ppt-master
- **语言**：Python | **协议**：MIT
- **描述**：AI turns documents or topics into real, native PowerPoint decks
- **今日新增**：+476

---

### 5. cactus-compute/needle（⭐+315，总⭐4,210）
- **链接**：https://github.com/cactus-compute/needle
- **语言**：Python | **协议**：MIT
- **描述**：14MB foundation model for tiny devices
- **今日新增**：+315

---

### 6. Lightricks/LTX-2（⭐+65，总⭐8,702）
- **链接**：https://github.com/Lightricks/LTX-2
- **语言**：Python | **协议**：未标注
- **描述**：Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model
- **今日新增**：+65

---

### 7. smicallef/spiderfoot（⭐+74，总⭐20,341）
- **链接**：https://github.com/smicallef/spiderfoot
- **语言**：Python | **协议**：未标注
- **描述**：SpiderFoot automates OSINT for threat intelligence and mapping your attack surface
- **今日新增**：+74

---

### 8. sherlock-project/sherlock（⭐+235，总⭐89,352）
- **链接**：https://github.com/sherlock-project/sherlock
- **语言**：Python | **协议**：MIT
- **描述**：Hunt down social media accounts by username across social networks
- **今日新增**：+235
- **技术亮点**：通过用户名在全网社交网络中追踪账号，OSINT 安全工具。

---

### 9. 3b1b/manim（⭐+506，总⭐90,575）
- **链接**：https://github.com/3b1b/manim
- **语言**：Python | **协议**：未标注
- **描述**：Animation engine for explanatory math videos
- **今日新增**：+506
- **技术亮点**：3Blue1Brown 的数学动画引擎，用于生成解释性数学视频，经典项目持续热门。

---

### 10. anthropics/skills（⭐+569，总⭐168,523）
- **链接**：https://github.com/anthropics/skills
- **语言**：Python | **协议**：未标注
- **描述**：Public repository for Agent Skills
- **今日新增**：+569
- **技术亮点**：Anthropic 官方 Agent Skills 仓库，展示 Claude Skills 系统的全部能力。包含 docx/pdf/pptx/xlsx 等文档处理技能的源码参考（source-available）。

---

### 11. ZhuLinsen/daily_stock_analysis（⭐+559，总⭐62,569）
- **链接**：https://github.com/ZhuLinsen/daily_stock_analysis
- **语言**：Python | **协议**：未标注
- **描述**：LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **今日新增**：+559
- **技术亮点**：LLM-powered 股票分析系统，支持多市场、实时新闻、自动推送，零成本定时运行。

---

### 12. anthropics/claude-code（⭐+150，总⭐141,231）
- **链接**：https://github.com/anthropics/claude-code
- **语言**：Python | **协议**：未标注
- **描述**：Claude Code is an agentic coding tool that lives in your terminal
- **今日新增**：+150
- **技术亮点**：Anthropic 官方终端编码 Agent，141k+ stars。支持自然语言命令执行代码、解释复杂代码、处理 git 工作流。

---

### 13. HKUDS/DeepTutor（⭐+651，总⭐35,169）
- **链接**：https://github.com/HKUDS/DeepTutor
- **语言**：Python | **协议**：Apache 2.0
- **描述**：DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/
- **今日新增**：+651
- **技术亮点**：终身个性化 AI 辅导系统，香港大学数据科学团队出品。支持三层记忆（L1/L2/L3）、Agentic Deep Research、LlamaIndex RAG、多 IM 渠道（Mattermost/Matrix/Discord 等）、MCP 工具调用。
- **详细解读素材**：
  - **三层记忆**：L1 短期对话上下文、L2 中期知识积累、L3 长期个人学习档案
  - **Partner 系统**：可接入 Claude Code / Codex 等外部 Agent 作为"辅导伙伴"
  - **Knowledge Center**：GraphRAG / PageIndex / LightRAG / Linked-KB / Obsidian 集成
  - **多模态**：支持 PDF/DOCX 中的图像提取和理解
  - **Sandbox 安全**：TutorBot 工具沙箱锁定，每用户资源隔离
  - **发布节奏极快**：v1.5.11（8/10），几乎每周多个版本

---

### 14. omnigent-ai/omnigent（⭐+173，总⭐8,726）
- **链接**：https://github.com/omnigent-ai/omnigent
- **语言**：Python | **协议**：Apache 2.0
- **描述**：Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents
- **今日新增**：+173
- **技术亮点**：开源 AI Agent 元编排框架（meta-harness），统一管理 Claude Code、Codex、Cursor、Pi 及自定义 Agent，支持策略执行、沙箱隔离、跨设备实时协作。
- **详细解读素材**：
  - **跨设备会话同步**：终端 → 浏览器 → 手机，消息/子 Agent/终端/文件全同步
  - **Supervise Multiple Agents**：同一会话中混合多种 Agent，可让一个 Agent 审查另一个 Agent 的工作
  - **任意模型**：支持自有 API Key、Claude/ChatGPT 订阅、任意兼容网关
  - **云沙箱**：Modal / Daytona / Blaxel / E2B / CoreWeave / K8s / Databricks 等
  - **Governance**：审批策略、支出上限、工具权限限制，可作用到全服务器/单 Agent/单聊天
  - **桌面 App**：原生 macOS App 可用

---

### 15. calesthio/OpenMontage（⭐+650，总⭐47,779）
- **链接**：https://github.com/calesthio/OpenMontage
- **语言**：Python | **协议**：AGPL-3.0
- **描述**：World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files.
- **今日新增**：+650
- **技术亮点**：全球首个开源 Agentic 视频制作系统。12 条制作管线、100+ 工具、700+ Agent 技能和制作知识文件。可将 AI 编码助手转变为完整视频制作工作室。
- **详细解读素材**：
  - **制作管线**：概念 → 剧本 → 场景规划 → 资产生成 → 剪辑 → 合成
  - **两种视频路径**：
    - 图像动画路径：FLUX 生成图像 + Remotion 动画引擎（Ken Burns/粒子效果/视差）
    - 真实视频路径：从免费素材库检索真实运动片段，剪辑合成完整作品
  - **Backlot 实时看板**：本地故事板自动随管线进度填充，场景级审批门控
  - **参考视频驱动**：粘贴 YouTube/Short/Reel/TikTok 链接，AI 分析节奏、场景、关键帧后生成差异化概念
  - **成本透明**：每个示例标注总成本（$0.02 ~ $1.33）
  - **支持编码助手**：Claude Code、Cursor、Copilot、Windsurf、Codex

---

## 主题分类汇总

### 🔥 AI Agent / 编排（今日最热主题）
| 项目 | 今日新增 | 总星数 | 核心定位 |
|------|---------|--------|---------|
| agency-agents | +1,873 | 144,550 | 100+ Agent 人格模板库 |
| orca | +1,235 | 43,839 | 多 Agent 并行 IDE |
| semantica | +845 | 5,698 | 确定性 AI 决策基础设施 |
| paperclip | +571 | 77,715 | 企业级 Agent 编排平台 |
| diagram-design | +2,855 | 10,272 | AI 图表生成技能 |
| OpenMontage | +650 | 47,779 | Agentic 视频制作系统 |
| DeepTutor | +651 | 35,169 | 终身 AI 辅导系统 |
| omnigent | +173 | 8,726 | Agent 元编排框架 |
| Switchyard | +421 | 813 | LLM 流量路由代理 |

### ⚙️ DevTools / 开发工具
| 项目 | 今日新增 | 总星数 | 核心定位 |
|------|---------|--------|---------|
| claude-code | +150 | 141,231 | Anthropic 终端编码 Agent |
| skills | +569 | 168,523 | Agent Skills 官方仓库 |
| macro | +227 | 1,768 | 统一工作空间（Rust） |

### 🧠 大模型推理优化 / 端侧
| 项目 | 今日新增 | 总星数 | 核心定位 |
|------|---------|--------|---------|
| needle | +315 | 4,210 | 14MB 端侧工具调用模型 |
| unsloth | +592 | 70,645 | 本地 LLM 训练与运行 UI |

### 🔒 安全 / OSINT
| 项目 | 今日新增 | 总星数 | 核心定位 |
|------|---------|--------|---------|
| spiderfoot | +74 | 20,341 | 自动化 OSINT 工具 |
| sherlock | +235 | 89,352 | 社交账号追踪 |

### 📊 数据处理 / RAG
| 项目 | 今日新增 | 总星数 | 核心定位 |
|------|---------|--------|---------|
| ragflow | +139 | 87,536 | RAG + Agent 引擎 |
| MediaCrawler | +215 | 61,956 | 多平台爬虫合集 |
| ppt-master | +476 | 45,542 | AI 生成原生 PPT |

---

## 今日关键趋势

1. **Agent 编排基础设施爆发**：今日 Top 10 中 7 个与 AI Agent 编排/管理/沙箱相关，显示行业正从"单 Agent 工具"进入"多 Agent 企业级编排"阶段
2. **确定性 AI 受关注**：Semantica 强调无需 LLM 的确定性推理和审计追踪，回应监管合规需求
3. **端侧小模型崛起**：Needle 14MB 模型挑战大模型 Function Calling，端侧 Agent 成为可能
4. **Rust 在基础设施层渗透**：Switchyard、Macro 等关键基础设施项目选用 Rust
5. **中国项目表现强劲**：MediaCrawler、DeepTutor、RAGFlow、ZhuLinsen/daily_stock_analysis 等多个中文项目上榜
