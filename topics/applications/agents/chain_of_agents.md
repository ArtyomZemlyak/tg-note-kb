# Chain-of-Agents: End-to-End Agent Foundation Models

## Обзор

![Chain-of-Agents Paradigm Comparison](../../../media/img_1771471872_aqadybhrgxwrmeh_lecompasition_ptoo0sa_selechon_negotiati.jpg)

**Image:** Comparison of TIR and CoA paradigms showing decomposition, selection, and negotiation phases

**Chain-of-Agents (CoA)** — новая парадигма LLM-рассуждений, разработанная OPPO AI Agent Team, которая enables native end-to-end complex problem-solving таким же образом, как мультиагентная система (multi-turn problem solving с multiple tools и multiple agents) внутри одной модели.

**Ключевое новшество:** В отличие от Tool-Integrated Reasoning (TIR), который поддерживает только ReAct-like trajectory (think-action-observation), CoA поддерживает практически любую мультиагентную систему через динамическую активацию role-playing agents и tool agents в end-to-end fashion.

## Проблема Существующих Подходов

### Ограничения Multi-Agent Systems (MAS)

1. **Высокий computational overhead** из-за redundant communication между агентами и sophisticated workflow design
2. **Challenges в generalization** к новым доменам и задачам без substantial reconfiguration (prompt engineering, workflow engineering)
3. **Inability to perform data-centric learning** — performance MAS не может улучшаться через training на agentic tasks
4. **Backbone LLMs не тренированы** для поддержки multi-turn, multi-agent, multi-tool workflows — они prompt engineered для этого

### Ограничения Tool-Integrated Reasoning (TIR)

TIR модели (Search-R1, WebThinker) явно incorporate tool usage в reasoning process, но:
- Поддерживают только ReAct-like trajectory
- Не могут тренировать LLM для поддержки multi-agent systems в end-to-end fashion
- Не используют преимущества collaboration между multiple role-playing agents

## Chain-of-Agents Парадигма

### Архитектура

CoA состоит из двух core компонентов:

#### 1. Role-playing Agents (High-level reasoning и coordination)

| Агент | Функция |
|-------|---------|
| **Thinking Agent** | Orchestrates reasoning pipeline, активирует specialized agents, maintains solution state coherence |
| **Plan Agent** | Decomposes query в structured task sequences ⟨φ_search, φ_crawl, ...⟩ |
| **Reflection Agent** | Conducts self-critique через knowledge fusion и inconsistency resolution |
| **Verification Agent** | Validates reasoning integrity against formal correctness criteria |

#### 2. Tool Agents (Domain-specific execution)

| Агент | Функция |
|-------|---------|
| **Search Agent** | Формулирует optimized queries с source prioritization |
| **Crawl Agent** | Parallel content extraction и technical detail parsing |
| **Code Generate Agent** | Generates and executes code snippets в sandbox environments |

### State Transitions

CoA orchestrates multi-agent collaboration внутри единого decoding (inference) процесса:

```
S_t = Γ(S_{t-1}, φ_t, o_t)
```

где:
- `S_t` — persistent reasoning state
- `φ_t ∈ {φ_think, φ_plan, φ_search, ...}` — activated roles
- `o_t` — observation от executed agent

### Сравнение Парадигм

| Парадигма | Tool Integration | End-to-end Execution | Multi-agent Collaboration | Data-centric Optimization |
|-----------|-----------------|---------------------|--------------------------|--------------------------|
| ReAct | ✓ | ✗ | ✗ | ✗ |
| Multi-Agent System | ✓ | ✗ | ✓ | ✗ |
| Tool-Integrated Reasoning | ✓ | ✓ | ✗ | ✓ |
| **Chain-of-Agents** | ✓ | ✓ | ✓ | ✓ |

**Преимущества CoA:**
- Устраняет need для sophisticated prompt engineering и workflow engineering
- Reduces computational overhead для inter-agent communication
- Supports end-to-end training
- Maintains contextual continuity внутри multi-agent orchestration

## Методология Обучения

### Multi-Agent Knowledge Distillation

Подход leverages agent-level knowledge distillation для transfer capabilities от state-of-the-art multi-agent systems в chain-of-agents trajectories.

**Процесс:**
1. State-of-the-art MAS (например, OAgents) решает task
2. System monitors agent selection process
3. Captures reasoning state перед каждым agent action
4. Records agent output
5. Transforms MAS collaboration procedure в CoA-like trajectory

**Формализация:**
```
Γ = {(S_t, φ_t, o_t)}_{t=1}^T
```
где `S_t` — reasoning state, `φ_t ~ P(φ|S_t)` — activated agent, `o_t` — observation.

### Progressive Quality Filtering

Four-stage filtering для обеспечения high-quality trajectories:

1. **Complexity filtering:** Trajectories с < 5 total agent-tool interactions исключаются
2. **Quality filtering:** "Dirty data" удаляется (incorrect answers, redundant tool inputs, failure to follow instructions)
3. **Reflection enrichment:** Trajectories lacking reflection mechanisms downsampled
4. **Error-correction trajectory upsampling:** Trajectories где double-check agent initially yields low credibility scores но ultimately achieves correct answers — upsampled

**Результирующий корпус характеризуется:**
- Все trajectories necessitate multi-tool collaborative coordination
- Reasoning chains span 5-20 hops (significantly surpassing 2-3 hop range standard benchmarks)
- Enriched high-quality reflective trajectories (особенно с iterative error correction)

### Формат Training Data

```
<think> C_cot </think>
<tools> α_m(α_p) </tools>
<observation> O_t </observation>
<reflection> F_t </reflection>
...
<answer> A_t </answer>
```

где:
- `C_cot` — chain-of-thought rationales
- `α_m` — tool action
- `F_t` — reflection/reasoning over observation
- `O_t` — tool observations

**Training objective:**
```
L = -Σ log P(answer|query, trajectories)
```
с observation masking (O) для efficiency.

### Agentic Reinforcement Learning

После SFT используется agentic RL на verifiable agentic tasks для further improvement capabilities.

**Ключевые аспекты:**
- Tool-aware rollouts на unused QA pairs
- Reward function design для multi-agent collaboration
- Optimization policy для dynamic agent orchestration

## Экспериментальные Результаты

### Web Agent Benchmarks

| Benchmark | AFM (CoA) | Previous SOTA |
|-----------|-----------|---------------|
| **GAIA** | 55.3% | < 50% |
| **BrowseComp** | 11.1% | < 10% |
| **HLE** | 18.0% | < 15% |

### Code Agent Benchmarks

| Benchmark | AFM (CoA) | Previous SOTA |
|-----------|-----------|---------------|
| **LiveCodeBench v5** | 47.9% | < 40% |
| **CodeContests** | 32.7% | < 25% |

### Mathematical Reasoning

| Benchmark | AFM (CoA) | Previous SOTA (TIR) |
|-----------|-----------|---------------------|
| **AIME2025** | 59.8% | 49.3% (ReTool, SimpleTIR) |

**Absolute improvement:** > 10.5% на challenging reasoning benchmarks

### Computational Efficiency

- **Reduction in inference cost:** 84.6% reduction in token consumption compared to traditional MAS
- **Competitive performance** при значительно lower overhead

## Agent Foundation Models (AFM)

Модели, тренированные с CoA paradigm, называются **Agent Foundation Models (AFM)**:

**Характеристики:**
- Native support для multi-agent collaboration внутри single model
- End-to-end оптимизируемые через SFT и RL
- Generalize к unseen agents и tools
- Support agentic test-time scaling

**Open Source:**
- Model weights
- Code для training и evaluation
- Training data

## Связь с Другими Работами

### Intelligent AI Delegation

В отличие от Intelligent Delegation (DeepMind), который фокусируется на **протоколах передачи authority и accountability** между отдельными агентами, CoA фокусируется на **internalization multi-agent collaboration** внутри единой модели.

**Комплементарность:**
- CoA может использоваться для internalization delegation protocols от Intelligent Delegation
- Intelligent Delegation может обеспечивать security и verification для CoA-generated trajectories

### FeUdal Networks

CoA shares similarities с hierarchical RL:
- Thinking Agent ≈ Manager (sets abstract goals)
- Tool Agents ≈ Worker (execute primitive actions)

**Key difference:** CoA operates в token space LLM, а не в action space RL.

### BlockA2A

CoA может benefit от security frameworks типа BlockA2A:
- Decentralized identity для tool agents
- Immutable auditability для agent trajectories
- Smart contract enforcement для verification policies

## Применение

### Deep Research

- Multi-hop information seeking
- Cross-source verification
- Iterative hypothesis refinement

### Vibe Coding

- Dynamic tool selection (search, code, test)
- Self-reflection и error correction
- Multi-file project coordination

### Mathematical Reasoning

- Step-by-step proof construction
- Tool-augmented calculation
- Verification через formal methods

## Ограничения и Вызовы

### Training Data Requirements

- High-quality multi-agent trajectories дороги для генерации
- Progressive filtering reduces dataset size
- Domain-specific adaptation требует additional data

### Generalization

- Generalization к unseen agents требует careful design
- Tool integration может require retraining для new tools

### Computational Costs

- Training AFM требует significant compute
- RL optimization может быть unstable
- Test-time scaling увеличивает inference costs

## Будущие Направления

1. **Automated agent discovery** — dynamic identification оптимальных agent roles для task
2. **Cross-model collaboration** — CoA trajectories across heterogeneous LLM backbones
3. **Human-in-the-loop CoA** — integration human feedback в end-to-end training
4. **Verification-aware CoA** — integration cryptographic verification (zk-SNARKs, TEE)

## Источники

1. **Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL**. OPPO AI Agent Team. arXiv preprint arXiv:2508.13167, 2025. URL: https://arxiv.org/abs/2508.13167
2. **OAgents: Open-Source Multi-Agent System**. URL: https://github.com/OPPO-Mente-Lab/OAgents
3. **Medium: Chain-of-Agents: How OPPO's New AI Distills an Expert Team Into a Single Super-Model**. URL: https://medium.com/towardsdev/chain-of-agents-how-oppos-new-ai-distills-an-expert-team-into-a-single-super-model-c3e5393937a8

## Дополнительные Материалы

- **GAIA Benchmark**: https://huggingface.co/gaia-benchmark
- **LiveCodeBench**: https://livecodebench.github.io/
- **AIME Benchmark**: https://artofproblemsolving.com/aime

## См. Также

- [[applications/agents/intelligent_delegation_framework.md]] — фреймворк для безопасного делегирования между агентами от Google DeepMind
- [[applications/agents/blocka2a_security_framework.md]] — security framework для agent-to-agent interoperability
- [[ai/foundational_papers/hierarchical_reinforcement_learning/feudal_networks.md]] — hierarchical RL с Manager-Worker архитектурой
- [[frameworks_and_libraries/agentic-flow/multi_agent_systems.md]] — координация агентов в Agentic-Flow
- [[ai/multi_token_prediction.md]] — related архитектуры для efficient inference
