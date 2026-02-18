# Эмбеддинги трассы/пути для агентов в гоночных играх

## Краткое описание

Представление трассы, пути или локации в виде эмбеддинга (векторного представления) — это подход к кодированию пространственной информации в компактную форму для подачи в модель обучения с подкреплением. Вместо обработки миллионов 3D-точек или сырых пикселей, агент получает сжатое латентное представление среды.

## Основная концепция

### Проблема традиционных подходов

Традиционные методы представления трассы в гоночных играх (включая Trackmania) используют:

| Подход | Размерность данных | Проблемы |
|--------|-------------------|----------|
| **3D-координаты** | `(x, y, z)` + ориентация | Требует точного позиционирования, не масштабируется |
| **LIDAR-лучи** | `(4, 19)` история | Локальная информация, нет глобального контекста |
| **Изображения (CNN)** | `84×84×4` кадра | Высокая размерность, требует значительных вычислений |
| **Полная 3D-геометрия** | Тысячи вершин/граней | Чрезмерно подробно для принятия решений |

### Решение через эмбеддинги

**Ключевая идея:** Сжать информацию о трассе/пути в компактный вектор фиксированной размерности (например, 64-512 измерений), который сохраняет семантически важную информацию для навигации.

```
Традиционный подход:
3D-точки трассы → [1000000+ координат] → Модель → Действие

Эмбеддинг подход:
3D-точки трассы → Encoder → [128-dim вектор] → Модель → Действие
```

## Методы создания эмбеддингов трассы

### 1. Трек-агностическое представление (Track-Agnostic Embedding)

**Подход:** Создание универсального представления трассы, которое не зависит от конкретной геометрии.

**Метод:**
```python
class TrackAgnosticEmbedding:
    def __init__(self, embedding_dim=128):
        self.encoder = TrackEncoder()  # CNN или Graph Neural Network
        self.embedding_dim = embedding_dim
    
    def encode_track(self, track_data):
        """
        Кодирование трассы в латентное пространство
        
        Args:
            track_data: представление трассы (изображение, граф, точки)
        
        Returns:
            track_embedding: вектор размерности embedding_dim
        """
        # 1. Извлечение ключевых характеристик
        features = self.extract_track_features(track_data)
        
        # 2. Кодирование в латентный вектор
        embedding = self.encoder(features)
        
        return embedding
```

**Преимущества:**
- Одна модель может работать на разных трассах
- Переносимость между играми
- Компактное представление

**Недостатки:**
- Требует обучения на разнообразных трассах
- Может терять детали специфичных трасс

### 2. Графовое представление трассы (Graph-based Track Embedding)

**Подход:** Представление трассы как графа, где узлы — ключевые точки, рёбра — соединяющие их сегменты.

**Структура графа:**
```python
class TrackGraph:
    nodes: List[TrackNode]      # Ключевые точки (повороты, прыжки, чекпоинты)
    edges: List[TrackEdge]      # Сегменты между точками
    
class TrackNode:
    position: Vector3           # 3D координаты
    node_type: str              # 'turn', 'jump', 'straight', 'checkpoint'
    difficulty: float           # Сложность участка
    optimal_speed: float        # Оптимальная скорость
    
class TrackEdge:
    from_node: int              # Индекс начального узла
    to_node: int                # Индекс конечного узла
    length: float               # Длина сегмента
    curvature: float            # Кривизна
    elevation_change: float     # Изменение высоты
```

**Кодирование через Graph Neural Network (GNN):**
```python
import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv

class TrackGraphEncoder(nn.Module):
    def __init__(self, node_features=16, edge_features=8, embedding_dim=128):
        super().__init__()
        self.node_encoder = nn.Linear(node_features, 64)
        self.edge_encoder = nn.Linear(edge_features, 64)
        
        # Graph Convolutional Layers
        self.gcn1 = GCNConv(64, 128)
        self.gcn2 = GCNConv(128, 256)
        
        # Global pooling to fixed-size embedding
        self.global_pool = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, embedding_dim)
        )
    
    def forward(self, graph):
        # Кодирование признаков узлов и рёбер
        node_embeddings = self.node_encoder(graph.node_features)
        edge_embeddings = self.edge_encoder(graph.edge_features)
        
        # Graph convolutions
        x = self.gcn1(node_embeddings, graph.edge_index)
        x = torch.relu(x)
        x = self.gcn2(x, graph.edge_index)
        x = torch.relu(x)
        
        # Global pooling (суммирование по всем узлам)
        track_embedding = self.global_pool(x.mean(dim=0))
        
        return track_embedding  # [embedding_dim]
```

**Преимущества:**
- Сохраняет топологическую структуру трассы
- Эффективно для 3D-трасс с прыжками
- Масштабируется на трассы разной длины

### 3. Иерархическое представление (Hierarchical Track Embedding)

**Подход:** Создание многоуровневого представления трассы — от глобальной структуры до локальных деталей.

**Уровни иерархии:**
```
Уровень 0: Глобальная структура (вся трасса)
    ↓
Уровень 1: Секции трассы (прямые, повороты, зоны прыжков)
    ↓
Уровень 2: Локальные особенности (конкретные повороты, препятствия)
    ↓
Уровень 3: Детальная геометрия (поверхность, бордюры)
```

**Архитектура:**
```python
class HierarchicalTrackEncoder(nn.Module):
    def __init__(self, embedding_dims=[256, 128, 64]):
        super().__init__()
        self.global_encoder = GlobalTrackEncoder()  # Уровень 0
        self.section_encoder = SectionEncoder()     # Уровень 1
        self.local_encoder = LocalFeatureEncoder()  # Уровень 2
        
        # Fusion layers для объединения уровней
        self.fusion = nn.Sequential(
            nn.Linear(sum(embedding_dims), 256),
            nn.ReLU(),
            nn.Linear(256, embedding_dims[-1])
        )
    
    def forward(self, track_data):
        # Кодирование на каждом уровне
        global_emb = self.global_encoder(track_data.global_structure)
        section_embs = self.section_encoder(track_data.sections)  # [N_sections, 128]
        local_embs = self.local_encoder(track_data.local_features)  # [N_features, 64]
        
        # Объединение иерархических эмбеддингов
        section_pooled = section_embs.mean(dim=0)  # [128]
        local_pooled = local_embs.mean(dim=0)      # [64]
        
        combined = torch.cat([global_emb, section_pooled, local_pooled], dim=-1)
        track_embedding = self.fusion(combined)
        
        return track_embedding
```

### 4. VAE-подход (Variational Autoencoder для траекторий)

**Подход:** Использование вариационных автоэнкодеров для обучения латентного пространства траекторий.

**Метод SeCTAR (Self-Consistent Trajectory Autoencoder):**

```python
class TrajectoryVAE(nn.Module):
    def __init__(self, trajectory_length=100, state_dim=10, latent_dim=32):
        super().__init__()
        self.latent_dim = latent_dim
        
        # Encoder: траектория → латентное распределение
        self.encoder = nn.Sequential(
            nn.LSTM(state_dim, 128, batch_first=True),
            nn.Linear(128, 64),
            nn.ReLU()
        )
        
        self.mu_head = nn.Linear(64, latent_dim)      # Среднее распределения
        self.logvar_head = nn.Linear(64, latent_dim)  # Логарифм дисперсии
        
        # Decoder: латентный вектор → траектория
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.LSTM(64, 128, batch_first=True),
            nn.Linear(128, state_dim)
        )
    
    def encode(self, trajectory):
        """Кодирование траектории в латентное распределение"""
        h, _ = self.encoder(trajectory)
        mu = self.mu_head(h[:, -1, :])
        logvar = self.logvar_head(h[:, -1, :])
        return mu, logvar
    
    def reparameterize(self, mu, logvar):
        """Reparameterization trick для сэмплирования"""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z, initial_state):
        """Декодирование латентного вектора в траекторию"""
        h = self.decoder[0](z)
        h = self.decoder[1](h)
        h = h.unsqueeze(1).repeat(1, trajectory_length, 1)
        output, _ = self.decoder[2](h)
        trajectory = self.decoder[3](output)
        return trajectory
    
    def forward(self, trajectory, initial_state):
        mu, logvar = self.encode(trajectory)
        z = self.reparameterize(mu, logvar)
        reconstructed = self.decode(z, initial_state)
        return reconstructed, mu, logvar
```

**Функция потерь:**
```python
def vae_loss(reconstructed, original, mu, logvar, beta=1.0):
    # Reconstruction loss (MSE)
    recon_loss = nn.functional.mse_loss(reconstructed, original)
    
    # KL-divergence loss (регуляризация латентного пространства)
    kl_loss = -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp())
    
    return recon_loss + beta * kl_loss
```

**Применение в RL:**
- Латентный вектор `z` используется как компактное представление траектории
- Политика обучается условно на `z`: `π(action | state, z)`
- Планирование происходит в латентном пространстве

### 5. Позиционные эмбеддинги для пространственных данных

**Подход:** Адаптация позиционных эмбеддингов (как в Transformers) для 3D-координат.

**Point Rotary Positional Embedding (Point-ROPE):**
```python
import torch
import numpy as np

class PointROPE(nn.Module):
    def __init__(self, dim=128, max_coord=1000):
        super().__init__()
        self.dim = dim
        assert dim % 6 == 0, "dim must be divisible by 6"
        self.head_dim = dim // 6
        
        # Частоты для каждой оси (x, y, z)
        inv_freq = 1.0 / (10000 ** (torch.arange(0, self.head_dim, 2).float() / self.head_dim))
        self.register_buffer('inv_freq', inv_freq)
    
    def forward(self, positions):
        """
        Args:
            positions: [N, 3] - координаты (x, y, z)
        
        Returns:
            embeddings: [N, dim] - позиционные эмбеддинги
        """
        # Разделение координат на оси
        x, y, z = positions[:, 0:1], positions[:, 1:2], positions[:, 2:3]
        
        # Применение RoPE к каждой оси
        emb_x = self.apply_rope(x, self.inv_freq)  # [N, head_dim]
        emb_y = self.apply_rope(y, self.inv_freq)
        emb_z = self.apply_rope(z, self.inv_freq)
        
        # Конкатенация эмбеддингов всех осей
        embeddings = torch.cat([emb_x, emb_y, emb_z], dim=-1)  # [N, dim]
        
        return embeddings
    
    def apply_rope(self, coord, inv_freq):
        """Применение rotary embedding к одной координате"""
        sinusoid_input = coord * inv_freq  # [N, head_dim//2]
        sinusoid_input = sinusoid_input.repeat_interleave(2, dim=-1)
        
        sin = torch.sin(sinusoid_input)
        cos = torch.cos(sinusoid_input)
        
        # Rotary transformation
        embeddings = torch.cat([cos, sin], dim=-1)
        return embeddings
```

**Применение:**
- Кодирование абсолютных 3D-позиций на трассе
- Сохранение относительных пространственных отношений
- Интеграция с Transformer-архитектурами

## Архитектура модели с эмбеддингом трассы

### Общая структура

```python
class RLAgentWithTrackEmbedding(nn.Module):
    def __init__(self, track_embedding_dim=128, state_dim=20, action_dim=6):
        super().__init__()
        
        # Предобученный эмбеддинг трассы (замороженный или обучаемый)
        self.track_encoder = TrackGraphEncoder(embedding_dim=track_embedding_dim)
        
        # Кодировщик состояния агента
        self.state_encoder = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128)
        )
        
        # Fusion: объединение эмбеддинга трассы и состояния
        self.fusion = nn.Sequential(
            nn.Linear(track_embedding_dim + 128, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU()
        )
        
        # Голова политики
        self.policy_head = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Sigmoid()  # Для бинарных действий
        )
    
    def forward(self, state, track_data):
        # Кодирование трассы
        track_embedding = self.track_encoder(track_data)  # [128]
        
        # Кодирование состояния
        state_embedding = self.state_encoder(state)  # [128]
        
        # Объединение
        combined = torch.cat([track_embedding, state_embedding], dim=-1)
        features = self.fusion(combined)
        
        # Предсказание действия
        action = self.policy_head(features)
        
        return action
```

### Обучение с предобучением эмбеддинга

```python
# Этап 1: Предобучение эмбеддинга трассы
def pretrain_track_encoder(encoder, track_dataset, epochs=100):
    """
    Предобучение на задаче реконструкции или контрастивном обучении
    """
    optimizer = torch.optim.Adam(encoder.parameters(), lr=1e-3)
    
    for epoch in range(epochs):
        for track_data in track_dataset:
            # Задача: реконструкция трассы из эмбеддинга
            embedding = encoder(track_data)
            reconstructed = encoder.decode(embedding)
            
            loss = reconstruction_loss(reconstructed, track_data)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    return encoder

# Этап 2: Обучение RL с замороженным эмбеддингом
def train_rl_with_embedding(agent, env, track_encoder, episodes=10000):
    # Замораживаем эмбеддинг трассы
    track_encoder.eval()
    for param in track_encoder.parameters():
        param.requires_grad = False
    
    # Обучение RL (например, PPO)
    for episode in range(episodes):
        state = env.reset()
        track_data = env.get_track_data()
        
        # Получение эмбеддинга трассы
        with torch.no_grad():
            track_embedding = track_encoder(track_data)
        
        # RL цикл
        for t in range(max_steps):
            action = agent(state, track_embedding)
            next_state, reward, done, info = env.step(action)
            
            # Сохранение опыта и обновление политики
            agent.store_transition(state, action, reward, next_state, done, track_embedding)
            
            state = next_state
            if done:
                break
        
        # Обновление политики
        agent.update()
```

## Применение к Trackmania

### Специфика Trackmania

1. **3D-трассы с прыжками:** Трассы имеют вертикальную составляющую, требуют 3D-представления
2. **Высокая скорость:** Решения принимаются быстро, нужно компактное представление
3. **Разнообразие поверхностей:** Асфальт, грунт, трамплины — разная физика
4. **Shortcuts и альтернативные пути:**Multiple возможные траектории

### Рекомендуемый подход для Trackmania

**Гибридная архитектура:**

```python
class TrackmaniaTrackEmbedding(nn.Module):
    def __init__(self, embedding_dim=128):
        super().__init__()
        
        # 1. Графовое представление для глобальной структуры
        self.graph_encoder = TrackGraphEncoder(
            node_features=12,  # позиция, тип, сложность, ...
            edge_features=8,   # длина, кривизна, высота, ...
            embedding_dim=64
        )
        
        # 2. CNN для локальной геометрии (изображение мини-карты)
        self.local_cnn = nn.Sequential(
            nn.Conv2d(1, 16, 3, 1),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, 2),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(32*14*14, 64)
        )
        
        # 3. Fusion для объединения
        self.fusion = nn.Sequential(
            nn.Linear(64 + 64, embedding_dim),
            nn.ReLU(),
            nn.Linear(embedding_dim, embedding_dim)
        )
    
    def forward(self, track_graph, minimap_image):
        # Глобальное представление (граф)
        graph_emb = self.graph_encoder(track_graph)  # [64]
        
        # Локальное представление (CNN)
        local_emb = self.local_cnn(minimap_image)  # [64]
        
        # Объединение
        combined = torch.cat([graph_emb, local_emb], dim=-1)
        track_embedding = self.fusion(combined)  # [128]
        
        return track_embedding
```

**Входные данные для эмбеддинга:**
```python
track_data = {
    # Граф трассы
    'graph': {
        'nodes': [
            {'pos': (x,y,z), 'type': 'turn', 'angle': 90, 'difficulty': 0.8},
            {'pos': (x,y,z), 'type': 'jump', 'height': 5.0, 'length': 20.0},
            # ...
        ],
        'edges': [
            {'from': 0, 'to': 1, 'length': 50, 'curvature': 0.3},
            # ...
        ]
    },
    
    # Мини-карта (вид сверху)
    'minimap': np.array([...]),  # [128, 128] grayscale
    
    # Чекпоинты
    'checkpoints': [(x1,y1,z1), (x2,y2,z2), ...],
    
    # Зоны прыжков
    'jump_zones': [
        {'entry': (x,y,z), 'exit': (x,y,z), 'min_speed': 50},
        # ...
    ]
}
```

### Преимущества для Trackmania

| Аспект | Традиционный подход | С эмбеддингом |
|--------|-------------------|---------------|
| **Размерность входа** | `(4, 19)` LIDAR + `(3,)` координаты | `(128,)` эмбеддинг |
| **Глобальный контекст** | ❌ Нет | ✅ Есть |
| **3D-прыжки** | ⚠️ Частично | ✅ Полная поддержка |
| **Переносимость** | ❌ Модель для каждой трассы | ✅ Одна модель для всех |
| **Скорость инференса** | Средняя | Высокая |
| **Обучение** | Медленная сходимость | Быстрая сходимость |

## Потенциальные проблемы и ограничения

### 1. Потеря информации при сжатии

**Проблема:** Эмбеддинг фиксированной размерности может не сохранить все детали трассы.

**Решение:**
- Использовать иерархические эмбеддинги
- Добавить механизм внимания для динамического фокуса на важных участках
- Контрастивное обучение для сохранения важной информации

### 2. Обучение эмбеддинга

**Проблема:** Требуются большие размеченные данные для обучения.

**Решение:**
- Self-supervised обучение (реконструкция, контрастивные задачи)
- Transfer learning с предобученных моделей
- Data augmentation (вариации трасс)

### 3. Обобщение на новые трассы

**Проблема:** Модель может не работать на трассах, не виденных при обучении.

**Решение:**
- Обучение на разнообразных трассах
- Регуляризация латентного пространства (VAE)
- Meta-learning для быстрой адаптации

### 4. Вычислительная стоимость кодирования

**Проблема:** Кодирование трассы может быть медленным.

**Решение:**
- Предварительное вычисление эмбеддингов (offline)
- Лёгкие архитектуры encoder
- Кэширование эмбеддингов для известных трасс

## Связанные работы и исследования

### Trajectory Embeddings

**SeCTAR (Self-Consistent Trajectory Autoencoder):**
- Иерархическое RL с эмбеддингами траекторий
- VAE-подход для кодирования траекторий в латентное пространство
- Планирование в латентном пространстве без дополнительного RL

**Применение:**
- Imitation learning из демонстраций
- Classification и regression на траекториях
- Генерация новых траекторий из латентного пространства

### Graph-based Spatial Representations

**Multi-agent graph embedding:**
- Построение пространственных графов agent–obstacle–target
- GNN для кодирования отношений
- Применение в навигации и планировании пути

### Track-Agnostic RL

**Подход:**
- Универсальное представление трассы через латентные векторы
- Одна модель для всех трасс
- Extension DRL для гоночных игр

## Практические рекомендации

### Когда использовать эмбеддинги трассы

✅ **Рекомендуется:**
- Множество разных трасс (нужна переносимость)
- 3D-трассы с прыжками и сложной геометрией
- Ограничения по вычислениям в runtime
- Нужен глобальный контекст для планирования

❌ **Не рекомендуется:**
- Одна фиксированная трасса (проще выучить напрямую)
- Простые 2D-трассы без вертикальности
- Достаточно вычислительных ресурсов для обработки сырых данных
- Требуется максимальная точность (эмбеддинги теряют детали)

### Выбор размерности эмбеддинга

| Сложность трассы | Рекомендуемая размерность |
|-----------------|--------------------------|
| Простые 2D | 32-64 |
| Стандартные 3D | 64-128 |
| Сложные с прыжками | 128-256 |
| Очень сложные (multiple пути) | 256-512 |

### Стратегия обучения

1. **Предобучение encoder:**
   - Self-supervised на неразмеченных трассах
   - Задача: реконструкция или contrastive learning
   - 100-1000 эпох

2. **Заморозка и RL обучение:**
   - Заморозить encoder (не обновлять градиенты)
   - Обучать только политику
   - Быстрая сходимость

3. **Fine-tuning (опционально):**
   - Разморозить encoder
   - Обучать end-to-end с малым learning rate
   - Улучшение производительности

## Связи с другими темами

- [[track_representation_rl.md]] - Традиционные методы представления трассы в Trackmania: checkpoint-система, LIDAR, координаты
- [[replay_learning_trackmania.md]] - Обучение на реплеях Trackmania: архитектура, сбор данных
- [[../../algorithms/specialized/graph_neural_networks/index.md]] - Graph Neural Networks для кодирования структур
- [[../../algorithms/neural_networks/autoencoders.md]] - Автоэнкодеры и VAE для сжатия данных
- [[../../algorithms/classical_ml/reinforcement_learning/index.md]] - Обучение с подкреплением
- [[../../ai/imitation_learning/behavioral_cloning.md]] - Поведенческое клонирование
- [[../../algorithms/neural_networks/transformers/index.md]] - Transformers и positional embeddings

## Источники

1. Yeh, J., et al. (2018). Self-Consistent Trajectory Autoencoder: Hierarchical Reinforcement Learning with Trajectory Embeddings. ICML 2018. URL: https://arxiv.org/abs/1806.02813
2. AAMAS 2025. On Learning Informative Trajectory Embeddings for Imitation, Classification and Regression. URL: https://www.ifaamas.org/Proceedings/aamas2025/
3. Schwarting, W., et al. (2021). Learning to Race Using Visual Control Policies in Latent Space. Conference on Robot Learning 2021. URL: https://proceedings.mlr.press/v155/schwarting21a/
4. Enhancing generalization in autonomous driving through track-agnostic reinforcement learning. Neural Computing and Applications, 2025. URL: https://dl.acm.org/doi/10.1007/s00521-025-11597-5
5. Survey on Graph-Based Reinforcement Learning for Networked Multi-Agent Systems. Technologies, 2025. URL: https://www.mdpi.com/2673-4052/6/4/65
6. Neinders, B. (2023). Improving Trackmania Reinforcement Learning Performance. University of Twente. URL: http://essay.utwente.nl/96153/1/Neinders_BA_EEMCS.pdf
7. Su, J., et al. (2021). RoFormer: Enhanced Transformer with Rotary Position Embedding. arXiv:2104.09864. URL: https://arxiv.org/abs/2104.09864

```metadata
category: applications
subcategory: gaming_ai
tags: track_embedding, path_representation, reinforcement_learning, racing_games, trackmania, latent_space, graph_neural_networks, trajectory_encoding, vae, spatial_representation
```
