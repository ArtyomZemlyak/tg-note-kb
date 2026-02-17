# ИИ для игр: Обучение на реплеях (Gaming AI: Replay Learning)

## Краткое описание

Обучение ИИ для игр на реплеях людей — это подход к созданию игровых ботов и агентов, использующий записи игровых сессий (реплеи) для обучения нейронных сетей через поведенческое клонирование и обучение с подражанием. Этот метод особенно эффективен для гоночных симуляторов (Trackmania), где есть скриншоты с высокой частотой кадров и логи нажатий клавиш.

## Основное описание

Обучение на реплеях представляет собой практическое применение методов imitation learning к видеоиграм. Игровые реплеи содержат богатые демонстрации экспертного поведения, включая:

- **Визуальные наблюдения**: Скриншоты игрового процесса с высокой частотой (60-240 FPS)
- **Действия игрока**: Логи нажатий клавиш, движения мыши, действия контроллера
- **Контекстуальная информация**: Позиция, скорость, состояние игры (если доступно)

### Преимущества подхода

1. **Доступность данных**: Реплеи легко записывать и хранить
2. **Разнообразие**: Множество игроков с разными стилями
3. **Масштабируемость**: Можно собрать тысячи часов геймплея
4. **Безопасность**: Обучение без риска для физического оборудования

## Архитектура системы для Trackmania

### Входные данные

#### Визуальный вход
```
- Скриншоты: 84x84 или 128x128 пикселей
- Частота: 64 FPS (синхронизировано с игрой)
- Формат: Grayscale или RGB
- Stack: 4 последних кадра для temporal информации
```

#### Вход действий (история)
```
- Газ (W): 0 или 1
- Тормоз (S): 0 или 1
- Влево (A): 0 или 1
- Вправо (D): 0 или 1
- Дрифт (Пробел): 0 или 1
- Сброс (R): 0 или 1
- История: последние 10-20 фреймов
```

### Архитектура нейронной сети

#### Вариант 1: CNN + LSTM (рекомендуется)
```
Визуальный поток:
Input: [84x84x4] (stack 4 кадров)
↓
Conv2d(4, 32, kernel=8, stride=4) → ReLU → [20x20x32]
↓
Conv2d(32, 64, kernel=4, stride=2) → ReLU → [9x9x64]
↓
Conv2d(64, 64, kernel=3, stride=1) → ReLU → [7x7x64]
↓
Flatten → [3136]
↓
Fully Connected: 512 units → ReLU
↓
[512-dim visual features]

Поток действий:
Input: [10x6] (10 фреймов истории, 6 кнопок)
↓
LSTM: 256 hidden units
↓
[256-dim action features]

Объединение:
Concat: [512 + 256] = [768]
↓
FC: 256 → ReLU
↓
FC: 128 → ReLU
↓
Output: [6] → Sigmoid (для multi-label classification)
```

#### Вариант 2: ResNet Backbone
```
Визуальный поток:
Input: [128x128x3]
↓
ResNet-18 (без последних слоев)
↓
[512-dim features]
↓
FC: 256 → ReLU

Поток действий:
(аналогично Варианту 1)

Объединение и вывод:
(аналогично Варианту 1)
```

#### Вариант 3: Transformer-based (экспериментальный)
```
Vision Transformer (ViT):
- Patch embedding: 16x16
- Position encoding
- Transformer encoder: 4-6 слоев
- [CLS] token как features

Action Transformer:
- Action embedding
- Temporal encoding
- Transformer encoder: 2-3 слоя

Cross-attention между модальностями
```

## Процесс обучения

### Шаг 1: Сбор данных

```python
# Псевдокод для сбора данных
import pyautogui
import cv2
import time

def collect_replay_data():
    frames = []
    actions = []
    timestamps = []
    
    start_time = time.time()
    
    while recording:
        # Скриншот
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (128, 128))
        frames.append(frame)
        
        # Действия
        action_vector = [
            keyboard.is_pressed('w'),  # газ
            keyboard.is_pressed('s'),  # тормоз
            keyboard.is_pressed('a'),  # влево
            keyboard.is_pressed('d'),  # вправо
            keyboard.is_pressed('space'),  # дрифт
            keyboard.is_pressed('r'),  # сброс
        ]
        actions.append(action_vector)
        timestamps.append(time.time() - start_time)
        
        time.sleep(1/64)  # 64 FPS
    
    return frames, actions, timestamps
```

### Шаг 2: Предобработка данных

```python
import torch
from torch.utils.data import Dataset
import numpy as np

class ReplayDataset(Dataset):
    def __init__(self, replay_files, frame_stack=4, action_history=10):
        self.replay_files = replay_files
        self.frame_stack = frame_stack
        self.action_history = action_history
        
    def __getitem__(self, idx):
        # Загрузка данных
        frames, actions = self.load_replay(self.replay_files[idx])
        
        # Случайный выбор временного шага
        t = np.random.randint(self.frame_stack, len(frames) - self.action_history)
        
        # Stack кадров
        stacked_frames = np.stack([frames[t-i] for i in range(self.frame_stack)], axis=-1)
        stacked_frames = stacked_frames.astype(np.float32) / 255.0  # нормализация
        
        # История действий
        action_seq = np.array([actions[t-i] for i in range(self.action_history)])
        action_seq = action_seq.astype(np.float32)
        
        # Целевое действие (следующий фрейм)
        target_action = np.array(actions[t+1]).astype(np.float32)
        
        return stacked_frames, action_seq, target_action
    
    def __len__(self):
        return len(self.replay_files)
```

### Шаг 3: Обучение модели

```python
import torch
import torch.nn as nn
import torch.optim as optim

class TrackmaniaBC(nn.Module):
    def __init__(self, action_dim=6):
        super().__init__()
        
        # CNN для изображений
        self.cnn = nn.Sequential(
            nn.Conv2d(4, 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64*7*7, 512),
            nn.ReLU(),
        )
        
        # LSTM для истории действий
        self.lstm = nn.LSTM(
            input_size=action_dim,
            hidden_size=256,
            num_layers=2,
            batch_first=True,
            dropout=0.3
        )
        
        # Объединяющие слои
        self.fc = nn.Sequential(
            nn.Linear(512 + 256, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Sigmoid()  # для multi-label
        )
    
    def forward(self, frames, action_history):
        visual_features = self.cnn(frames)
        _, (action_features, _) = self.lstm(action_history)
        action_features = action_features[-1]  # последний слой
        
        combined = torch.cat([visual_features, action_features], dim=1)
        return self.fc(combined)

# Обучение
def train_model(model, dataloader, num_epochs=50):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    
    criterion = nn.BCELoss()  # Binary Cross Entropy
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)
    
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        
        for frames, action_hist, target in dataloader:
            frames = frames.to(device)
            action_hist = action_hist.to(device)
            target = target.to(device)
            
            optimizer.zero_grad()
            output = model(frames, action_hist)
            loss = criterion(output, target)
            loss.backward()
            
            # Gradient clipping
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}')
        scheduler.step(avg_loss)
```

### Шаг 4: Валидация и тестирование

```python
def evaluate_model(model, val_dataloader):
    model.eval()
    correct = 0
    total = 0
    action_accuracy = {i: 0 for i in range(6)}  # для каждой кнопки
    
    with torch.no_grad():
        for frames, action_hist, target in val_dataloader:
            output = model(frames, action_hist)
            predicted = (output > 0.5).int()
            
            # Общая точность
            total += target.numel()
            correct += (predicted == target).sum().item()
            
            # Точность по действиям
            for i in range(6):
                action_accuracy[i] += ((predicted[:, i] == target[:, i]).sum().item())
    
    accuracy = correct / total
    print(f'Validation Accuracy: {accuracy:.4f}')
    for i, acc in enumerate(action_accuracy):
        print(f'Action {i} Accuracy: {acc / total:.4f}')
    
    return accuracy
```

## Интеграция с RL для дообучения

### Подход 1: BC + PPO Fine-tuning

```python
# После обучения BC модели
def fine_tune_with_ppo(bc_model, env, num_steps=1000000):
    # Инициализация PPO с весами из BC
    ppo_agent = PPOAgent(bc_model)
    
    # PPO hyperparameters
    gamma = 0.99
    gae_lambda = 0.95
    clip_epsilon = 0.2
    lr = 3e-4
    
    # Награда в Trackmania
    def compute_reward(state, next_state, action):
        # Прогресс по трассе
        progress_reward = next_state.progress - state.progress
        
        # Штраф за сброс
        reset_penalty = -1.0 if action[5] > 0.5 else 0
        
        # Штраф за столкновение
        crash_penalty = -0.5 if state.is_crashed else 0
        
        # Бонус за скорость
        speed_bonus = next_state.speed * 0.01
        
        return progress_reward + reset_penalty + crash_penalty + speed_bonus
    
    # PPO training loop
    for episode in range(num_episodes):
        # Сбор траекторий
        trajectories = collect_trajectories(ppo_agent, env)
        
        # Вычисление advantages
        advantages = compute_gae(trajectories, gamma, gae_lambda)
        
        # PPO update
        ppo_agent.update(trajectories, advantages, clip_epsilon, lr)
    
    return ppo_agent
```

### Подход 2: Комбинированная функция потерь

```python
class CombinedLoss(nn.Module):
    def __init__(self, bc_weight=0.5, rl_weight=0.5):
        super().__init__()
        self.bc_weight = bc_weight
        self.rl_weight = rl_weight
        self.bc_loss = nn.BCELoss()
    
    def forward(self, policy_output, expert_actions, rl_advantages):
        # BC loss: кросс-энтропия с действиями эксперта
        bc_loss = self.bc_loss(policy_output, expert_actions)
        
        # RL loss: policy gradient с advantages
        rl_loss = -(policy_output * rl_advantages).mean()
        
        # Комбинированная потеря
        total_loss = self.bc_weight * bc_loss + self.rl_weight * rl_loss
        
        return total_loss
```

## Практические рекомендации

### Сбор данных

1. **Качество реплеев**:
   - Записывайте только чистые заезды без сбросов
   - Используйте реплеи сильных игроков (top 10%)
   - Избегайте поврежденных/прерванных записей

2. **Разнообразие**:
   - Разные типы трасс (скоростные, технические, смешанные)
   - Разные погодные условия (если применимо)
   - Разные стили вождения

3. **Объем данных**:
   - Минимум: 10 часов чистого геймплея
   - Рекомендуется: 50-100 часов
   - Идеально: 500+ часов для robust модели

### Обучение

1. **Hyperparameters**:
   ```
   Learning rate: 1e-4 (Adam)
   Batch size: 64-256
   Gradient clipping: 1.0
   Dropout: 0.3
   Weight decay: 1e-5
   ```

2. **Regularization**:
   - Data augmentation (random crops, brightness)
   - Dropout в fully-connected слоях
   - Early stopping по validation loss

3. **Monitoring**:
   - Training/validation loss curves
   - Per-action accuracy
   - Visual inspection of predictions

### Deployment

1. **Оптимизация**:
   - Quantization (FP32 → FP16 → INT8)
   - Pruning незначительных весов
   - Knowledge distillation в меньшую модель

2. **Inference**:
   ```python
   def predict_action(model, frames_stack, action_history):
       model.eval()
       with torch.no_grad():
           output = model(frames_stack, action_history)
           # Threshold для бинарных действий
           actions = (output > 0.5).int()
       return actions
   ```

3. **Latency**:
   - Целевая задержка: <16ms (для 60 FPS)
   - Используйте GPU inference или оптимизированный CPU
   - Batch prediction для multiple environments

## Связи с другими темами

- [[behavioral_cloning.md]] - Поведенческое клонирование как основа подхода
- [[imitation_learning_methods.md]] - Методы обучения с подражанием
- [[../../algorithms/classical_ml/reinforcement_learning/index.md]] - Обучение с подкреплением
- [[../../algorithms/classical_ml/reinforcement_learning/ppo_algorithm.md]] - PPO для дообучения
- [[../../algorithms/neural_networks/convolutional/index.md]] - CNN для обработки изображений
- [[../../algorithms/neural_networks/recurrent/index.md]] - LSTM для временных последовательностей
- [[../../applications/computer_vision/image_classification/index.md]] - Классификация изображений

## Источники

1. Bruce, J., et al. (2024). Genie: Generative Interactive Environments. arXiv preprint arXiv:2402.15391.
2. Blog: Trackmania 2020 AI - Training neural networks for racing games. URL: https://blog.tammearu.eu/posts/tm20ai/
3. Reddit: AI that can drive in Trackmania. URL: https://www.reddit.com/r/MachineLearning/comments/ia93ao/p_i_made_an_ai_that_can_drive_in_a_real_racing/
4. Neinders, B. (2023). Improving Trackmania Reinforcement Learning Performance. University of Twente. URL: http://essay.utwente.nl/96153/1/Neinders_BA_EEMCS.pdf
5. CSDN Blog: Trackmania RL Tutorial. URL: https://blog.csdn.net/gitblog_00952/article/details/142162471
6. YouTube: Training an unbeatable AI in Trackmania. URL: https://www.youtube.com/watch?v=Dw3BZ6O_8LY

```metadata
category: applications
subcategory: gaming_ai
tags: trackmania, gaming_ai, replay_learning, behavioral_cloning, imitation_learning, neural_networks, racing_simulator, bot_training
```
