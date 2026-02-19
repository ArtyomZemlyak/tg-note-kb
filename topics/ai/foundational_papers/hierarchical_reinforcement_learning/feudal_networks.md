# FeUdal Networks for Hierarchical Reinforcement Learning

## Обзор

**FeUdal Networks (FuN)** — новаторская архитектура для иерархического reinforcement learning, предложенная исследователями из DeepMind (Alexander Sasha Vezhnevets, Simon Osindero, Tom Schaul, Nicolas Heess, Max Jaderberg, David Silver, Koray Kavukcuoglu) в 2017 году.

**Ключевое новшество:** FuN decouples end-to-end learning across multiple levels hierarchy, allowing использовать different resolutions of time. Архитектура employs **Manager module** и **Worker module**, где Manager operates на lower temporal resolution и sets abstract goals, которые Worker enacts через primitive actions.

## Мотивация

### Проблемы Deep Reinforcement Learning

1. **Long-term Credit Assignment** — особенно в environments со sparse reward signals (например, Montezuma's Revenge)
2. **Non-Markovian Environments** — требуют memory для storing relevant experience
3. **Action Repeat Heuristic** — стандартный подход на ATARI benchmark использует action repeat (каждое action = 4 consecutive actions), что указывает на limitations temporal abstraction

### Вдохновение от Feudal Reinforcement Learning

Работа основана на **Feudal Reinforcement Learning (FRL)** предложенной Dayan & Hinton (1993):

**Key Insights FRL:**
- Goals генерируются в top-down fashion
- Goal setting decoupled от goal achievement
- Higher levels reasoning на lower temporal resolution naturally structures behavior в temporally extended sub-policies

## Архитектура FeUdal Networks

### Модульная Структура

```
Environment Observation (x_t)
         ↓
  Perceptual Module (f_percept)
         ↓
  Shared Representation (z_t)
         ↙       ↘
    Manager      Worker
    (f_Mrnn)     (f_Wrnn)
       ↓           ↓
    Goal (g_t)   Actions (a_t)
```

### Manager Module

**Функции:**
- Internally computes latent state representation `s_t`
- Outputs goal vector `g_t` на lower temporal resolution
- Operates с horizon `c` (typically c = 10 steps)

**Архитектура:**
```
h_t^M = f_Mrnn(h_{t-1}^M, z_t)  # Dilated LSTM
s_t = f_Mspace(h_t^M)            # State space representation
g_t = Manager Policy(s_t)        # Goal output
```

**Dilated LSTM:** Novel RNN architecture для Manager:
- Composed of `r` separate groups of sub-states ('cores')
- At each time step only corresponding part обновляется
- Allows preserve memories для long periods
- Processes every input experience
- Updates output at every step

```
dLSTM: ĥ_{t%r}^t, g_t = LSTM(s_t, ĥ_{t%r}^{t-1}; θ_LSTM)
```

### Worker Module

**Функции:**
- Generates primitive actions на every tick environment
- Conditioned на:
  - External observation `x_t`
  - Own state `h_t^W`
  - Goals от Manager `g_t`

**Архитектура:**
```
h_t^W = f_Wrnn(h_{t-1}^W, z_t, g_t)  # Standard LSTM
U_t = Worker Policy(h_t^W)            # Action embeddings
w_t = φ(Σ_{i=0}^{c-1} g_{t-i})        # Goal embedding (pooled)
π_t = softmax(U_t · w_t)              # Final policy
```

### Goal Embedding Mechanism

**Key Design:** Goals модулируют policy через multiplicative interaction в low-dimensional goal-embedding space `R^k` (k << d).

**Process:**
1. Last `c` goals pooled by summation: `G_t = Σ_{i=0}^{c-1} g_{t-i}`
2. Linear projection без biases: `w_t = φ(G_t) ∈ R^k`
3. Matrix-vector product: `π_t ∝ U_t · w_t`

**Важно:** Поскольку φ не имеет biases, она никогда не produz constant non-zero vector — это ensures что goal от Manager всегда влияет на final policy.

## Обучение

### Transition Policy Gradient (Manager)

**Novel Update Rule:** Manager trains через approximate transition policy gradient, который exploits semantic meaning goals.

**Intuition:** Manager learns to select latent goals, которые maximise extrinsic reward, без gradients от Worker.

**Update Formula:**
```
∇_θ J ≈ E[A_t^M · ∇_θ d_cos(s_{t+c} - s_t, g_t)]
```

где:
- `A_t^M = R_t - V_t^M(x_t, θ)` — Manager's advantage function
- `d_cos(α, β) = α^T β / (|α| |β|)` — cosine similarity
- `c` — horizon Manager (temporal resolution)

**Key Property:** `g_t` acquires semantic meaning как advantageous direction в latent state space на horizon `c`.

### Intrinsic Reward (Worker)

**Worker Motivation:** Worker trains via intrinsic reward для following goals.

**Intrinsic Reward:**
```
R_t^I = d_cos(s_{t+c} - s_t, g_t)
```

**Total Reward для Worker:**
```
R_total = R_t + α · R_t^I
```

где `α` — hyperparameter, регулирующий influence intrinsic reward.

**Важно:** FuN использует **directional goals** (направления в state space) вместо **absolute goals** (конкретные target states).

**Преимущества Directional Goals:**
- More feasible для Worker reliably cause directional shifts
- Degree of invariance к goals
- Structural generalization — same directional sub-goal может invoke sub-policy valid в large part of state space
- Examples: "evade enemy", "swim up for air"

### Worker Policy Training

Worker trains через Advantage Actor-Critic (A3C):

```
∇_θ J = E[∇_θ log π(a_t|s_t) · A_t^W]
```

где:
```
A_t^W = (R_t + αR_t^I) - V_t^W(x_t; θ)
```

### Discount Factors

Manager и Worker могут иметь different discount factors `γ`:
- **Worker:** Может быть более greedy (focus на immediate rewards)
- **Manager:** Considers long-term perspective

## Архитектурные Детали

### Perceptual Module

**CNN Architecture:**
```
Layer 1: 16 filters 8x8, stride 4 → ReLU
Layer 2: 32 filters 4x4, stride 2 → ReLU
FC Layer: 256 hidden units → ReLU
```

### State Space Module

```
f_Mspace: Fully connected (256 units) → ReLU
```

### Goal Embedding Dimension

```
k = 16 (dimensionality embedding vectors w)
```

### Recurrent Networks

| Module | Architecture | Hidden Units |
|--------|-------------|--------------|
| **Manager** | Dilated LSTM (r=10) | 256 |
| **Worker** | Standard LSTM | 256 |

### Exploration

```
With probability ε: emit random goal ~ N(0, σ²)
```

## Эксперименты

### Montezuma's Revenge

**Challenge:** Infamously hard ATARI game с lethal traps и sparse rewards.

**Results:**
- FuN significantly outperforms LSTM baseline
- Learns semantically meaningful sub-goals
- Sub-goals correspond to interpretably useful waypoints

**Visualization:** Analysis learnt sub-goals shows tall bars (consistent goals) correspond to:
- Key locations в first room
- Ladder positions
- Treasure locations

### Sea Quest

**Task:** Multi-objective game с oxygen management и enemy avoidance.

**Sub-policies Discovered:**
1. Navigate left area
2. Navigate right area
3. **Swim up for oxygen** (critical survival behavior)
4. Enemy engagement zones

**Finding:** FuN automatically discovers reusable temporal abstractions без explicit regularizers.

### ATARI Suite Comparison

**Baselines:**
- LSTM с different discount factors (γ = 0.95, 0.99)
- Different BPTT lengths (K = 40, 400)

**Results:** FuN outperforms LSTM на games requiring:
- Long-term credit assignment
- Memory
- Temporal abstraction

### DeepMind Lab Memory Tasks

**Tasks:** Visual memorization в 3D environment.

**Findings:**
- FuN dramatically improves memorization
- Emergence of sub-policies associated с different goals
- Better generalization к unseen scenarios

## Ablation Study

### Critical Components

| Component | Impact |
|-----------|--------|
| **Transition Policy Gradient** | Crucial для best performance |
| **Directional Goals** | Significantly better than absolute goals |
| **Dilated LSTM** | Enables long-term memory |
| **Intrinsic Reward** | Necessary для goal following |

### Comparison с Option-Critic

**Key Differences:**
| Aspect | Option-Critic | FeUdal Networks |
|--------|--------------|-----------------|
| **Goal Representation** | Latent options | Explicit directional goals |
| **Training** | End-to-end policy gradient | Decoupled Manager/Worker |
| **Sub-goal Diversity** | Requires regularizers | Emerges naturally |
| **Temporal Resolution** | Fixed option duration | Flexible horizon c |

**Results:** FuN achieves significantly better scores на ATARI benchmarks.

## Связь с Другими Работами

### Options Framework

**Options Framework** (Sutton et al., 1999; Precup, 2000) — popular formulation для hierarchical RL:
- Bottom level: option (sub-policy с termination condition)
- Top level: policy-over-options

**Problems с End-to-End Learning Options:**
- Tend to degenerate к trivial solutions:
  1. Only one active option solves whole task
  2. Policy-over-options changes options at every step (micro-managing)
- Requires regularizers для multiple options extended length

**FuN Advantage:** Sub-goals emerge как directions в latent state space — naturally diverse без regularizers.

### Auxiliary Losses and Rewards

**Related Approaches:**
- **Count-based exploration bonuses** (Bellemare et al., 2016a) — pseudo-count rewards для Montezuma's Revenge
- **UNREAL** (Jaderberg et al., 2016) — unsupervised auxiliary tasks

**Orthogonality:** Benefits от auxiliary losses orthogonal к FuN — можно комбинировать для greater effect.

## Применение к Intelligent AI Delegation

### Manager-Worker Pattern в Делегировании

FeUdal Networks provides template для learning-based delegation:

| FuN Concept | Intelligent Delegation |
|-------------|----------------------|
| **Manager** | Delegator (sets abstract goals) |
| **Worker** | Delegatee (executes primitive actions) |
| **Goals** | Task specifications |
| **Intrinsic Reward** | Alignment incentives |
| **Transition Policy Gradient** | Learning to delegate effectively |

### Key Insights для Делегирования

1. **Decoupled Learning:** Manager (delegator) learns от environment rewards, не от Worker gradients
2. **Directional Goals:** Abstract directions более effective чем absolute specifications
3. **Temporal Abstraction:** Lower temporal resolution для delegator enables long-term planning
4. **Emergent Sub-policies:** Reusable behaviors emerge без explicit regularizers

### Connection к Chain-of-Agents

**Similarities:**
- Thinking Agent (CoA) ≈ Manager (FuN)
- Tool Agents (CoA) ≈ Worker (FuN)

**Differences:**
- FuN operates в action space RL
- CoA operates в token space LLM

**Potential Integration:** CoA could internalize FuN-style hierarchical delegation protocols.

## Ограничения и Вызовы

### Hyperparameter Sensitivity

- Intrinsic reward weight `α` требует careful tuning
- Horizon `c` affects temporal abstraction level
- Dilated LSTM radius `r` impacts memory capacity

### Scalability

- Two-level hierarchy может быть insufficient для very complex tasks
- Deeper hierarchies require additional design considerations
- Communication overhead между levels

### Goal Representation

- Latent state space dimensionality requires tuning
- Directional goals могут быть insufficient для некоторых tasks
- Absolute goals могут потребоваться для precise targeting

## Будущие Направления

1. **Deeper Hierarchies** — более двух levels (Manager → Manager → Worker)
2. **Communication Protocols** — explicit communication между levels
3. **Multi-Manager Architectures** — parallel managers для different aspects
4. **Integration с LLMs** — FuN-style hierarchy для LLM agent control
5. **Human-in-the-Loop** — human as Manager или overseer

## Источники

1. Vezhnevets, A. S., Osindero, S., Schaul, T., Heess, N., Jaderberg, M., Silver, D., & Kavukcuoglu, K. (2017). **FeUdal Networks for Hierarchical Reinforcement Learning**. arXiv preprint arXiv:1703.01161. DeepMind. URL: https://arxiv.org/abs/1703.01161
2. **Proceedings of the 34th International Conference on Machine Learning (ICML 2017)**. URL: https://proceedings.mlr.press/v70/vezhnevets17a.html
3. **GitHub: FeUdal Networks Implementation**. URL: https://github.com/davidhershey/feudal_networks

## Дополнительные Материалы

- **Dayan, P., & Hinton, G. E. (1993). Feudal Reinforcement Learning**. NIPS 1992.
- **Options Framework**: Sutton, R. S., Precup, D., & Singh, S. (1999). Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning.
- **DeepMind Lab**: Beattie, C., et al. (2016). DeepMind Lab. arXiv:1612.03801.

## См. Также

- [[applications/agents/intelligent_delegation_framework.md]] — фреймворк для ИИ-делегирования с Manager-Worker паттернами
- [[applications/agents/chain_of_agents.md]] — end-to-end agent foundation models с hierarchical organization
- [[reinforcement_learning/hierarchical_rl/index.md]] — иерархическое reinforcement learning
- [[ai/foundational_papers/recurrent_neural_networks/understanding_lstm.md]] — LSTM архитектуры
- [[applications/agents/google_research_scaling_agent_systems.md]] — масштабирование агентных систем
