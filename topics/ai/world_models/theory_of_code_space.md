# Theory of Code Space: Бенчмарк для проверки понимания архитектуры кода агентами

## Общее описание

**Theory of Code Space (ToCS)** — это бенчмарк для оценки способности AI-агентов по коду konstruировать, поддерживать и обновлять связные архитектурные убеждения во время исследования кодовой базы. Вместо оценки только правильности выходного кода (как в HumanEval или SWE-bench), ToCS измеряет, строит ли агент внутреннюю модель архитектуры системы.

Работа напрямую наследует идеи из **Theory of Space (ToS)** [[./theory_of_space.md]] — бенчмарка для проверки пространственного интеллекта мультимодальных моделей, но переносит эту диагностику в область software engineering.

![Theory of Code Space: оценка понимания архитектуры кода](../../../media/doc_1773635452_ff69366b_arxiv_2603.00601.pdf) <!-- TODO: Broken image path -->

**Ключевая идея:** AI-агенты для работы с кодом excel на изолированных задачах (написание функций, исправление локализованных багов), но struggle со сложным software engineering, требующим понимания взаимосвязей между десятками модулей. ToCS гипотезирует, что эти провалы происходят от неспособности конструировать, поддерживать и обновлять когерентные архитектурные убеждения во время исследования кодовой базы.

## Ключевая проблема: Разрыв между генерацией кода и пониманием архитектуры

### Фундаментальный разрыв

Large language models достигают remarkable scores на бенчмарках генерации кода [Chen et al., 2021, Austin et al., 2021], создавая ожидание deep understanding software architecture. Однако practitioners сообщают о persistent gap: модели, которые с лёгкостью решают HumanEval проблемы, производят incoherent результаты при модификации реальных кодовых баз с десятками взаимозависимых модулей [Jimenez et al., 2024].

### Связь с Theory of Space

Recent work на spatial reasoning предлагает compelling diagnostic framework. Zhang et al. [2026] ввели Theory of Space (TOS) бенчмарк, демонстрирующий, что мультимодальные модели не могут поддерживать когерентные внутренние 'cognitive maps' при активном исследовании частично наблюдаемых сред. Они идентифицировали два core феномена:

1.  **Active-Passive Gap** — модели деградируют, когда должны сами собирать информацию, а не получать её upfront
2.  **Belief Inertia** — модели не могут обновлять spatial beliefs, когда среда меняется

ToCS гипотезирует, что те же latent state maintenance failures объясняют struggles code agents.

## Формализация: Убеждения об архитектуре кода

Авторы формализуют codebase understanding как belief construction over latent architectural state.

### Архитектурное состояние

Пусть **S** обозначает ground-truth архитектуру, включающую:

-   **Typed dependency graph** G = (V, E) с edge types τ ∈ {IMPORTS, CALLS_API, DATA_FLOWS_TO, REGISTRY_WIRES}
-   **Cross-module invariants** I
-   **Exported contracts** C

В момент t агент имеет историю h_t = (o_0:t, a_0:t), и оцениваются три операции на его убеждении B_t(S):

1.  **Construct** — построение B_t из partial observations, gathered through active exploration
2.  **Revise** — обновление B_t → B_t+∆t, когда environment mutates (S → S') и агент встречает evidence изменений
3.  **Exploit** — использование B_t для выполнения downstream engineering task correctly

### Cognitive Map Probing

Поскольку B_t — латентное внутреннее состояние, его измеряют через **probing**: периодический запрос агенту экстернализировать убеждение как structured JSON.

**Every K=3 actions** harness прерывает агента structured prompt, запрашивающим экстернализацию текущего архитектурного убеждения как JSON. Critically, **probing is free** — не consumes action из бюджета B, ensuring measurement не interferes с exploration strategy.

Cognitive map ŜB_t содержит:

1.  **Component beliefs** со статусом (observed/inferred/unknown), purpose, exported symbols с typed signatures, typed dependency edges с per-element confidence
2.  **Invariant beliefs** со structured canonical form (type, src, dst, via, pattern) и evidence pointers
3.  **Uncertainty tracking** — explicit list unexplored regions

Resulting time-series of maps (one every K steps) captures, как understanding развивается, не just final state.

## Environment и Action Space

Агент взаимодействует с кодовой базой через **пять действий** с фиксированной tool semantics:

| Действие | Описание | Cost |
|----------|----------|------|
| **LIST(d)** | Filenames в директории d (no contents, no recursion) | 0 |
| **OPEN(f)** | Full contents файла f | 1 |
| **SEARCH(q)** | Matching filepaths + line numbers (no content snippets) | 1 |
| **INSPECT(f, s)** | Type signature + docstring symbol s (no body) | 1 |
| **DONE()** | Terminate | 0 |

Агент оперирует под **budget B** (default B=20). Critically, SEARCH возвращает только locations, never content — ensuring architectural understanding требует deliberate OPEN decisions.

## Evaluation Modes: Декомпозиция Active-Passive Gap

ToCS декомпозирует Active-Passive Gap через **четыре условия**:

| Mode | Описание |
|------|----------|
| **Active** | Agent chooses actions под бюджетом B |
| **Passive-Full** | Agent receives entire codebase; probed once |
| **Passive-Oracle** | Agent receives B files, selected by oracle (maximum ground-truth connectivity); one file per step, probed every K |
| **Passive-Replay** | Agent receives exact observation trace from prior active run, without decisions |

Это декомпозирует:
- **APG_total** = passive-full − active
- **APG_selection** = passive-oracle − active (cost of choosing which files)
- **APG_decision** = passive-replay − active (cost of deciding what to do with observations)

**Scope note:** v0.1 оценивает Construct operation в Active mode only. Passive conditions и APG decomposition implemented в harness и reserved for future work.

## Architectural Constraint Discovery

Beyond structural mapping, ToCS probes, могут ли агенты discover planted architectural constraints:

| Тип ограничения | Пример |
|-----------------|--------|
| **Forbidden dependency** | 'Module A must not import module C directly' |
| **Interface-only access** | 'Module X must access Y only through interface Z' |
| **Validation chain** | 'Data must pass through validation before reaching module W' |

Каждое constraint имеет **discoverability requirement**: test evidence, structural patterns, или documentation в кодовой базе. Scored via counterfactual multiple-choice probes ('Which change would violate an architectural constraint?').

**Это dimension отсутствует в spatial benchmarks** — в коде architectural decisions encode checkable constraints: forbidden dependency enforces service boundary; validation chain ensures data integrity.

## Процедурная генерация кодовых баз

### Architecture Grammar

v0.1 generator производит **Pipeline architecture** codebases с controlled anti-triviality measures. PipelineTemplate grammar определяет:

-   **Domain pools**: Three domains (data ETL, log processing, text processing), каждый с 8 semantically coherent processing stages. Medium complexity selects 6-8 stages
-   **Module roles**: Infrastructure (models, base class, config, exceptions, registry), stages (processing steps implementing common ABC), adapters (wrapping stages), middleware (cross-cutting decorators), utilities, legacy/distractor modules
-   **Anti-triviality measures**:
    1.  Registry wiring — stages connected via config, not direct imports
    2.  Adapter indirection — ABC interface layer
    3.  Distractor modules — files not in main pipeline
    4.  Neutral naming — mod_a.py, not extract.py
    5.  Hidden invariants — constraints discoverable only by reading function bodies/tests

### Four Edge Types

Каждая сгенерированная кодовая база содержит edges **четырёх типов**, отражающих different methods of discovery:

| Edge Type | ~Процент | Описание | Discovery Method |
|-----------|----------|----------|------------------|
| **IMPORTS** | ~67% | Python import statements | AST parsing |
| **CALLS_API** | ~17% | Runtime function calls between modules | Reading function bodies |
| **REGISTRY_WIRES** | ~9% | Config-driven connections (registry loads stages via importlib based on JSON config) | Reading config + registry logic |
| **DATA_FLOWS_TO** | ~7% | Data dependency (one module's output → another's input) | Understanding orchestration logic |

**Crucially**, roughly **one-third of edges are invisible to import-following**, создавая meaningful gap между syntactic analysis и semantic understanding.

### Generation Statistics

| Metric | Seed 42 | Seed 123 | Seed 999 |
|--------|---------|----------|----------|
| Modules | 27 | 30 | 27 |
| Total edges | 70 | 84 | 70 |
| IMPORTS | 47 (67%) | 56 (67%) | 47 (67%) |
| CALLS_API | 12 (17%) | 15 (18%) | 12 (17%) |
| DATA_FLOWS_TO | 5 (7%) | 6 (7%) | 5 (7%) |
| REGISTRY_WIRES | 6 (9%) | 7 (8%) | 6 (9%) |
| Invariants | 15 | 16 | 15 |
| Sub-packages | 5 | 5 | 5 |

### Invariant Planting

Каждая кодовая база содержит **15-16 planted constraints** across five types:

-   **BOUNDARY** — forbidden dependencies
-   **DATAFLOW** — required processing chains
-   **INTERFACE** — access-only-through-ABC
-   **INVARIANT** — naming/structural conventions
-   **PURPOSE** — design rationales

Каждое constraint имеет structured canonical form (type, src, dst, via, pattern) для machine-comparable scoring и ≥1 evidence source (test file, structural pattern, documentation).

## Метрики

### Dependency F1

Compare predicted edges from cognitive map against ground truth. Edge matches if (source, target, type) all agree. Report precision, recall, F1 separately.

### Invariant F1

Match agent-discovered constraints against planted constraints via **structured form comparison** — exact field matching on (type, src, dst, via), not text similarity. Это eliminates ambiguity в natural-language descriptions.

### Confidence Calibration

**Expected Calibration Error (ECE)** между agent-stated per-edge confidence и actual correctness, binned into 5 confidence intervals.

### Two Efficiency Curves

| Кривая | Описание |
|--------|----------|
| **Action-efficiency** | AUC(F1 vs. total actions) — headline metric |
| **Observation-efficiency** | AUC(F1 vs. OPEN count) — diagnostic, isolating information gain per file opened |

Belief is piecewise-constant между probes; integration is trapezoidal.

### Active-Passive Gap

For each metric m: **APG_m = m_passive − m_active**, decomposed into selection и decision components.

### Belief Revision Score (BRS)

After mutation at time t_m: **BRS = |correctly updated| / |affected elements|**

Decomposed into:
-   **Inertia-proper** — correctly-believed elements not updated after evidence
-   **Impact-discovery** — missing elements newly found
-   **Gullibility** — sham condition (evidence without actual change)

**BRS evaluation implemented but reserved for future work.**

## Эксперименты и результаты

### Methods

**Rule-based baselines:**

| Baseline | Описание |
|----------|----------|
| **Oracle** | Outputs ground-truth graph directly (F1 = 1.0, upper bound) |
| **Config-Aware** | Lists directories, opens config/registry first, parses module references, follows imports BFS |
| **Random** | Opens files uniformly at random until budget exhausted |
| **BFS-Import** | Opens files breadth-first following import chains |

All baselines build cognitive maps from AST-parsed imports and config references.

**LLM agents:**

| Модель | Провайдер | Notes |
|--------|-----------|-------|
| **Claude Sonnet 4.6** | Anthropic | Frontier coding model |
| **GPT-5.3-Codex** | OpenAI | Code-specialized reasoning model (temperature=1) |
| **Gemini 2.5 Flash** | Google | Reasoning-optimized flash model |
| **Gemini 3.1 Pro** | Google | Frontier pro model |
| **Gemini 3 Flash** | Google | Frontier flash model |

All models receive identical prompts: system prompt (partial observability environment + actions), per-turn action prompts (remaining budget + opened files), structured JSON probe prompts (schema + example). Temperature=0 except GPT-5.3-Codex.

### Результаты

| Method | Type | Dep F1 | Precision | Recall | AUC | Inv F1 | Files |
|--------|------|--------|-----------|--------|-----|--------|-------|
| **Oracle** | baseline | 1.000 | 1.000 | 1.000 | — | 0 | — |
| **Config-Aware** | baseline | **0.577** | 0.736 | 0.475 | 0.212 | 0 | 13 |
| **Random** | baseline | 0.538 | **1.000** | 0.368 | 0.142 | 0 | 13 |
| **BFS-Import** | baseline | 0.293 | **1.000** | 0.173 | 0.079 | 0 | 13 |
| **Claude Sonnet 4.6** | LLM | **0.646** | **0.991** | **0.479** | **0.377** | 0 | 12 |
| **GPT-5.3-Codex** | LLM | 0.564 | 0.768 | 0.460 | 0.243 | 0 | 14 |
| **Gemini 2.5 Flash** | LLM | 0.328 | 0.568 | 0.232 | 0.227 | 0 | 13 |
| **Gemini 3.1 Pro** | LLM | 0.262 | 0.894 | 0.156 | 0.135 | 0 | 9 |
| **Gemini 3 Flash** | LLM | 0.129 | 0.713 | 0.071 | 0.120 | 0 | 12 |

**Table 2:** Performance averaged over 3 codebases (seeds 42, 123, 999). Baselines use AST parsing; LLM agents use prompted JSON externalization. Best non-Oracle in **bold**.

### Edge Type Discovery

| Method | IMPORTS (n=150) | CALLS_API (n=39) | DATA_FLOWS (n=16) | REG._WIRES (n=19) |
|--------|-----------------|------------------|-------------------|-------------------|
| **Config-Aware** | 0.58 | 0 | 0 | 1.00 † |
| **Random** | 0.55 | 0 | 0 | 0.00 |
| **BFS-Import** | 0.25 | 0 | 0 | 0.00 |
| **Claude Sonnet 4.6** | 0.55 | **0.15** | 0 | **1.00** |
| **GPT-5.3-Codex** | **0.57** | **0.15** | **0.31** | 0.32 † |
| **Gemini 2.5 Flash** | 0.32 | 0.10 | 0 | 0.00 |
| **Gemini 3.1 Pro** | 0.20 | 0.05 | 0.06 | 0.05 |
| **Gemini 3 Flash** | 0.09 | 0.08 | 0 | 0.00 |

**Table 3:** Edge type recall by method. n = total ground-truth edges. Bold = best non-Oracle recall per type. † = significant over-generation (false positives > true positives).

### Ключевые инсайты

#### 1. Claude Sonnet 4.6 surpasses baselines

Claude Sonnet 4.6 достигает **F1 = 0.646**, surpassing best rule-based strategy (Config-Aware, 0.577) на 7 points — **первый LLM agent to outperform all baselines** на этом бенчмарке. Opens 12 files (vs. 13 for baselines) yet achieves higher recall (0.479 vs. 0.475), с near-perfect precision (0.991: only 1 false positive across all 3 codebases).

Critically, discovers **all 19 ground-truth REGISTRY_WIRES edges** с zero false positives — matching Config-Aware's recall but without its 38 false positives (Config-Aware achieves only 33% precision on this edge type). Это suggests Claude reads both config file и registry loading logic, correctly inferring which modules dynamically wired.

#### 2. LLM agents discover all four edge types

Table 3 reveals most distinctive finding: **LLM agents collectively discover all four edge types**, while baselines find at most two (IMPORTS и REGISTRY_WIRES for Config-Aware).

-   **All five LLMs found CALLS_API edges** — invisible to all rule-based baselines, confirming genuine code comprehension beyond syntactic parsing
-   **GPT-5.3-Codex — единственный метод, обнаруживший DATA_FLOWS_TO edges** (5 of 16, 31% recall, perfect precision), демонстрируя understanding, как data flows через pipeline orchestrator. Эти edges требуют **multi-hop reasoning**: tracing one module's return value through runner into next module's input.

#### 3. GPT-5.3-Codex: strong but variable

GPT-5.3-Codex achieves F1 = 0.564 on average (second-highest), но с **high variance** across codebases: 0.719 on seed 42 vs. 0.392 on seed 999. Discovers broadest range of edge types (all four), including 5 DATA_FLOWS_TO edges с perfect precision. Однако over-generates REGISTRY_WIRES edges (6 correct, 29 false positives), reducing overall precision to 0.768.

High variance may stem from sensitivity to early exploration choices: different initial file sequences trigger different architectural hypotheses, с some runs 'locking in' to more productive exploration path.

#### 4. Belief Externalization Bottleneck

Weaker LLMs (Gemini 3 Flash, F1 = 0.129) score below simple heuristics (Random, F1 = 0.538), revealing **belief externalization fidelity** как non-trivial capability. Faithfully serializing internal understanding into structured JSON — itself a first-order confounder in any belief-probing benchmark.

## Связь с другими бенчмарками

### Code Generation Benchmarks

| Бенчмарк | limitation vs. ToCS |
|----------|---------------------|
| **SWE-bench** [Jimenez et al., 2024] | Evaluates bug-fixing in real GitHub repos, measures patch correctness, **not evolving architectural understanding** |
| **ContextBench** [Li et al., 2026] | Logs agent trajectories, scores context retrieval precision/recall — **measuring what agent looked at, not what agent believes about architecture** |
| **SWE-ContextBench** [Zhu et al., 2026] | Tests cross-task experience reuse |
| **RepoBench** [Liu et al., 2024] | Evaluates repo-level completion |
| **LoCoBench-Agent** [Qiu et al., 2025] | Evaluates long-context interaction, observes 'comprehension-efficiency trade-off' (formalized как Active-Passive Gap в ToCS) |
| **RefactorBench** [Masai et al., 2025] | Targets multi-file refactoring, evaluates output correctness **without probing belief state** |

**None of these benchmarks** require agents to:
- Externalize revisable architectural belief state
- Impose exploration budgets
- Score against typed dependency graphs with planted constraints

### Code Understanding Tools

| Tool | Description |
|------|-------------|
| **CodePlan** [Bairi et al., 2024] | Augments LLMs with static-analysis dependency graphs for change propagation — engineering solution validating premise: agents need architectural maps but cannot build them alone |
| **Aider's RepoMap** [Gauthier, 2024] | Uses tree-sitter parsing + PageRank to construct repository context |
| **Code World Models** [FAIR CodeGen team, 2025] | Trains LLMs on execution traces to improve code reasoning |

**TOCS provides diagnostic benchmark** to test whether such approaches actually improve architectural belief quality.

### Spatial Reasoning

| Benchmark | Relation to ToCS |
|-----------|------------------|
| **Theory of Space** [Zhang et al., 2026] | Demonstrated Active-Passive Gap и Belief Inertia in grid-world environments — ToCS transplants this framework to code |
| **SpatialVLM** [Chen et al., 2024] | Evaluates spatial reasoning |
| **Habitat** [Savva et al., 2019] | Embodied question answering |
| **OpenEQA** [Majumdar et al., 2024] | Evaluates spatial reasoning, does not require constructing revisable belief states |
| **TOM-SWE** [Zhou et al., 2025] | Models user's mental state in SWE agents — complementary to ToCS focus on agent's belief about codebase |

## Практические выводы для исследователей

1.  **Architectural belief — latent variable**, которую current transformers не могут поддерживать стабильно при active exploration
2.  **Нужны архитектуры с явным state tracking** — способность генерировать код не гарантирует умения поддерживать связную архитектурную карту
3.  **Belief externalization fidelity** — non-trivial capability, первый порядок confounder в belief-probing benchmarks
4.  **LLM agents discover semantic edge types**, invisible to rule-based baselines — confirming genuine code comprehension beyond syntactic parsing
5.  **Exploration strategy matters** — high variance у GPT-5.3-Codex показывает sensitivity к early exploration choices

## Будущие направления

-   **Больше архитектурных паттернов**: event-driven, microservices, plugin systems (currently only Pipeline)
-   **Больше языков**: TypeScript, Go (currently only Python)
-   **REVISE фаза**: обновление beliefs после изменений в коде (BRS evaluation implemented, reserved for future work)
-   **Реальные кодовые базы** в дополнение к сгенерированным
-   **Использование документации** для выявления зависимостей и ограничений
-   **Разрешение противоречий** между реальным кодом и документами
-   **Scaffold-augmented evaluation**: static analysis + LLM
-   **Больше моделей**: frontier models (Claude, GPT, Gemini), open-weight models

## TOCS Benchmark Toolkit

**GitHub:** [https://github.com/che-shr-cat/tocs](https://github.com/che-shr-cat/tocs)

### Project Structure

```
tocs/
├── models.py              # Pydantic schemas (CognitiveMap, GroundTruth, EvalResult)
├── generator/             # Procedural codebase generation
├── harness/               # Partial observability environment + probing
├── baselines/             # Rule-based explorers (BFS-Import, Config-Aware, Random, Oracle)
├── metrics/               # Scoring (map accuracy, gap analysis, constraint discovery)
├── evaluation/            # Model adapters (Anthropic, OpenAI) + eval pipeline
├── analysis/              # Figure generation
├── tests/                 # 310 tests
├── paper/                 # LaTeX paper source
├── data/                  # Generated codebases
└── results/               # Evaluation results
```

### Installation & Usage

```bash
# Installation
pip install -e .

# Generate codebase
python -m generator --pattern pipeline --complexity medium --seed 42 \
  --output ./data/my_codebase

# Run evaluation (baseline)
python -m evaluation.run_eval evaluate \
  --model config-aware --codebase ./data/my_codebase --mode active \
  --budget 20 --output ./results/

# Run evaluation (frontier model)
ANTHROPIC_API_KEY=sk-... python -m evaluation.run_eval evaluate \
  --model claude-sonnet-4-5-20250929 --codebase ./data/my_codebase \
  --mode active --budget 15 --probe-interval 3 --output ./results/

# Generate figures
python -m analysis.figures --results ./results/ --output ./paper/figures/

# Run tests
python -m pytest tests/ -v
```

## Связи с другими темами

-   [[./theory_of_space.md|Theory of Space]] — бенчмарк для проверки пространственного интеллекта MLLM, direct predecessor ToCS
-   [[../../applications/agents/code_agents/index.md|Code Agents]] — агенты для работы с кодом, основная target audience ToCS
-   [[../../llm/post_training/index.md|Post-training LLM**]] — techniques для улучшения capabilities, которые можно evaluate через ToCS
-   [[../../interpretability/index.md|Interpretability**]] — understanding internal representations, related to belief construction
-   [[../safety/index.md|AI Safety**]] — understanding model limitations и failure modes
-   [[../../applications/nlp/code_generation/index.md|Code Generation**]] — генерация кода, complementary capability к architectural understanding

## Источники

1.  **Theory of Code Space: Do Code Agents Understand Software Architecture?** — Grigory Sapunov. arXiv:2603.00601, February 2026. [https://arxiv.org/abs/2603.00601](https://arxiv.org/abs/2603.00601)
2.  **TOCS Benchmark Toolkit** — GitHub repository. [https://github.com/che-shr-cat/tocs](https://github.com/che-shr-cat/tocs)
3.  **Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?** — Pingyue Zhang et al. arXiv:2602.07055, 2026. [https://arxiv.org/abs/2602.07055](https://arxiv.org/abs/2602.07055)
4.  **SWE-bench: Can Language Models Resolve Real-world GitHub Issues?** — Carlos E. Jimenez et al. arXiv:2310.06770, 2024. [https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)
5.  **HumanEval Benchmark** — Mark Chen et al. arXiv:2107.03374, 2021. [https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374)

## Дополнительные материалы

-   **ContextBench** — бенчмарк для evaluation context retrieval в agent trajectories
-   **RepoBench** — бенчмарк для repo-level code completion
-   **LoCoBench-Agent** — бенчмарк для long-context agent interaction
-   **RefactorBench** — бенчмарк для multi-file refactoring evaluation
-   **CodePlan** — tool для augmentation LLMs со static-analysis dependency graphs
-   **Aider's RepoMap** — tool для repository context construction через tree-sitter + PageRank

```metadata
category: ai
subcategory: world_models
tags: бенчмарки, code agents, architectural understanding, Theory of Code Space, ToCS, cognitive maps, belief construction, code comprehension, active exploration, partial observability
```
