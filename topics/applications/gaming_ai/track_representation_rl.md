# Представление трассы в Trackmania для обучения с подкреплением (RL)

## Краткое описание

Представление трассы в Trackmania для RL-агентов включает несколько подходов к кодированию состояния среды: от систем контрольных точек (checkpoint) до LIDAR-подобных измерений и обработки изображений. Выбор представления зависит от доступных API, требуемой точности и вычислительных ресурсов.

## Пространство состояний (State Space)

### Основные компоненты состояния

Состояние RL-агента в Trackmania обычно включает следующие компоненты:

| Компонент | Формат | Описание |
|-----------|--------|----------|
| **Скорость** | `(1,)` | Норма вектора скорости (скаляр) |
| **Позиция** | `(3,)` | Координаты (x, y, z) в мировом пространстве |
| **Ориентация** | `(3,)` | Углы Эйлера: yaw, pitch, roll |
| **LIDAR** | `(4, 19)` | История из 4 измерений по 19 лучей |
| **Действия** | `(2,)` | История последних 2 действий |

### Пространство наблюдений (Observation Space)

**Стандартное представление tmrl:**
```python
observation = {
    'speed': (1,),      # норма скорости
    'lidar': (4, 19),   # история LIDAR измерений
    'action_hist': (3,), # история действий
}
```

**Полное состояние (при использовании TMInterface):**
```python
state = {
    'position': (x, y, z),       # 3D координаты
    'orientation': (yaw, pitch, roll),
    'velocity': norm(velocity),  # норма скорости
    'speed': scalar_speed,
    'car_status': {...},         # состояние машины
}
```

## Представление трассы

### 1. Checkpoint-система (наиболее распространённая)

**Принцип работы:**
1. Для каждой трассы записывается **демонстрационная траектория** (не обязательно оптимальная)
2. Траектория автоматически делится на **равноотстоящие точки**
3. **Награда** = количество точек, пройденных с предыдущего шага

**Преимущества:**
- Простота реализации
- Не требует явных координат
- Автоматическое определение прогресса
- Устойчивость к разным стилям вождения

**Недостатки:**
- Зависит от качества демонстрации
- Не учитывает оптимальность пути
- Может создавать локальные оптимумы

**Пример реализации:**
```python
class CheckpointReward:
    def __init__(self, demonstration_trajectory, point_spacing=1.0):
        """
        demonstration_trajectory: список точек (x, y, z)
        point_spacing: расстояние между контрольными точками
        """
        self.points = self.equispace_points(
            demonstration_trajectory, 
            point_spacing
        )
        self.current_point_idx = 0
    
    def compute_reward(self, agent_position):
        # Найти ближайшую точку впереди
        progress = self.count_passed_points(agent_position)
        return progress  # награда = количество пройденных точек
```

### 2. LIDAR-подобное представление

**Принцип работы:**
- Изображение с камеры обрабатывается для выделения границ трассы
- От центра машины «испускаются» лучи в разных направлениях
- Для каждого луча вычисляется расстояние до границы трассы

**Техническая реализация:**
```python
def compute_lidar_from_image(image, num_rays=19):
    """
    Вычисление LIDAR-подобных измерений из скриншота
    
    Args:
        image: бинарное изображение трассы (после Canny edge detection)
        num_rays: количество лучей (обычно 19)
    
    Returns:
        lidar_distances: массив расстояний [num_rays]
    """
    # 1. Обработка изображения
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges = cv2.dilate(edges, kernel, iterations=2)
    
    # 2. Raycasting от центра машины
    center = (image.width // 2, image.height // 2)
    angles = np.linspace(0, np.pi, num_rays)  # 19 лучей в поле зрения
    
    distances = []
    for angle in angles:
        distance = cast_ray(edges, center, angle)
        distances.append(distance)
    
    return np.array(distances)
```

**Формат наблюдений:**
```
LIDAR history: (timesteps, num_rays) = (4, 19)
- 4 последних измерения
- 19 лучей в каждом измерении
- Расстояния нормализованы [0, 1]
```

### 3. Представление через изображения (CNN-based)

**Пайплайн обработки:**
1. **Скриншот**: 84×84 или 128×128 пикселей
2. **Предобработка**:
   - Конвертация в grayscale
   - Бинаризация/пороговая обработка
   - Canny edge detection
   - Dilation + Gaussian blur
3. **Stack кадров**: 4 последних кадра для temporal информации

**Архитектура CNN:**
```
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
```

### 4. Координатное представление

**Использование TMInterface/OpenPlanet API:**

```python
# Trackmania Nations Forever (TMInterface)
state = {
    'pos': (x, y, z),           # позиция в мире
    'roll': float,              # крен
    'pitch': float,             # тангаж
    'yaw': float,               # рыскание
    'speed': float,             # скорость
    'gear': int,                # передача
    'engine_rpm': float,        # обороты двигателя
}

# Trackmania 2020 (OpenPlanet API)
state = {
    'position': Vector3(x, y, z),
    'velocity': Vector3(vx, vy, vz),
    'orientation': Quaternion(w, x, y, z),
    'speed': float,
}
```

**Преимущества:**
- Точная информация о состоянии
- Не требует обработки изображений
- Быстрое получение данных

**Недостатки:**
- Требует доступа к API игры
- Меньше переносимости между версиями игры

## Пространство действий (Action Space)

### Бинарное представление

Используется в большинстве подходов с поведенческим клонированием:

```python
action = {
    'W': 0 or 1,    # газ
    'S': 0 or 1,    # тормоз/задний ход
    'A': 0 or 1,    # влево
    'D': 0 or 1,    # вправо
    'Space': 0 or 1, # дрифт/ручник
    'R': 0 or 1,    # сброс машины
}
```

**Размерность:** `(6,)` для 6 кнопок

### Аналоговое представление

Используется в RL с непрерывным управлением:

```python
action = [
    acceleration,   # [-1.0, +1.0]: -1=тормоз, +1=газ
    steering,       # [-1.0, +1.0]: -1=влево, +1=вправо
]
```

**Эмуляция контроллера Xbox 360:**
```python
import vgamepad as vg

gamepad = vg.VGamepad()

def apply_action(action):
    # Газ/тормоз (триггеры)
    if action[0] > 0:
        gamepad.right_trigger(action[0])  # 0..1
    else:
        gamepad.left_trigger(-action[0])  # 0..1
    
    # Руление (левый стик)
    gamepad.left_joystick_float(action[1], 0)  # x, y
    
    gamepad.update()
```

## Функция вознаграждения (Reward Function)

### Комбинированная награда

```python
def compute_reward(state, next_state, action):
    """
    Комбинированная функция вознаграждения для Trackmania
    """
    reward = 0.0
    
    # 1. Прогресс по трассе (основная награда)
    progress_reward = next_state.checkpoint_progress - state.checkpoint_progress
    reward += progress_reward * 1.0
    
    # 2. Штраф за сброс машины
    if action['R'] > 0.5:
        reward -= 1.0
    
    # 3. Штраф за столкновение/переворот
    if state.is_crashed or state.is_upside_down:
        reward -= 0.5
    
    # 4. Бонус за скорость (опционально)
    speed_bonus = next_state.speed * 0.01
    reward += speed_bonus
    
    # 5. Штраф за отклонение от оптимальной траектории
    if hasattr(state, 'distance_to_center'):
        deviation_penalty = -state.distance_to_center * 0.1
        reward += deviation_penalty
    
    return reward
```

### Награда на основе checkpoint-системы

```python
class CheckpointReward:
    def __init__(self, trajectory_points):
        self.points = trajectory_points  # равноотстоящие точки
        self.point_spacing = self.compute_spacing()
    
    def get_reward(self, current_pos, previous_pos):
        # Найти индекс ближайшей точки
        current_idx = self.find_nearest_point_index(current_pos)
        previous_idx = self.find_nearest_point_index(previous_pos)
        
        # Награда = количество пройденных точек
        points_passed = current_idx - previous_idx
        
        # Штраф за движение назад
        if points_passed < 0:
            points_passed *= 2  # удвоенный штраф
        
        return points_passed * self.point_spacing
```

## Временная дискретизация

### Конфигурация timestep

```python
# Стандартные настройки tmrl
TIMESTEP_DURATION = 0.05  # 0.05s = 20Hz
OBS_CAPTURE_OFFSET = 0.04  # захват наблюдения за 0.04s до конца timestep
ACTION_BUFFER_LENGTH = 2   # история из 2 действий
LIDAR_HISTORY_LENGTH = 4   # история из 4 LIDAR измерений
```

### Elastic Time Steps

Для обработки задержек в real-time средах используется подход с эластичными временными шагами:

```python
class ElasticTimeStep:
    def __init__(self, target_timestep=0.05, tolerance=0.01):
        self.target = target_timestep
        self.tolerance = tolerance
    
    def step(self, action):
        # Отправка действия
        self.env.apply_action(action)
        
        # Ожидание с допуском
        elapsed = self.wait_for_timestep()
        
        # Захват наблюдения
        observation = self.env.get_observation()
        
        return observation, elapsed
```

## Технические реализации

### tmrl (Trackmania RL Library)

**Ссылка:** https://pypi.org/project/tmrl/

**Ключевые особенности:**
- Gym-совместимая среда
- Поддержка Trackmania Nations Forever и Trackmania 2020
- Встроенная checkpoint-система
- LIDAR-вычисления из скриншотов

**Пример использования:**
```python
from tmrl import TMEnv

env = TMEnv(
    server_ip='localhost',
    server_port=5000,
    lidar_rays=19,
    lidar_history=4,
    action_history=2,
    timestep=0.05
)

obs = env.reset()
# obs shape: ((1,), (4, 19), (3,), (3,))
# speed, lidar_history, action_hist_1, action_hist_2

for _ in range(1000):
    action = agent.predict(obs)
    obs, reward, done, info = env.step(action)
```

### TMInterface

**Ссылка:** https://donadigo.com/tminterface/

**Для Trackmania Nations Forever:**
- Прямой доступ к состоянию игры
- Получение позиции, ориентации, скорости
- Отправка команд клавиатуры/геймпада

```python
from tminterface.interface import TMInterface
from tminterface.client import BaseClient

class RLClient(BaseClient):
    def __init__(self):
        super().__init__(interface_name='MyRLClient')
        self.state = None
    
    def on_run(self, current_time, current_step):
        # Получение состояния
        self.state = self.interface.get_state()
        position = self.state.dyna.position
        velocity = self.state.dyna.velocity
        speed = np.linalg.norm(velocity)
    
    def on_step(self, current_time, current_step):
        # Применение действия
        action = self.agent.predict(self.state)
        self.interface.set_key_state(action)

client = RLClient()
client.run()
```

### OpenPlanet API

**Для Trackmania 2020:**
- Скриптовый API на AngelScript
- Прямой доступ к физике игры
- Получение полного состояния машины

```angelscript
// OpenPlanet скрипт для получения состояния
void OnStep() {
    CGameCtnChallenge@ challenge = GetChallenge();
    CControlledCar@ car = challenge.GetControlledCar();
    
    // Позиция
    vec3 position = car.EyePosition;
    
    // Скорость
    vec3 velocity = car.Velocity;
    float speed = velocity.length();
    
    // Ориентация
    quat orientation = car.Orientation;
    
    // Отправка в RL-агент
    SendToRLAgent(position, velocity, orientation);
}
```

## Сравнение подходов

| Подход | Точность | Скорость | Переносимость | Сложность |
|--------|----------|----------|---------------|-----------|
| **Checkpoint** | Средняя | Высокая | Высокая | Низкая |
| **LIDAR** | Средняя | Средняя | Высокая | Средняя |
| **Изображения (CNN)** | Высокая | Низкая | Очень высокая | Высокая |
| **Координаты (API)** | Очень высокая | Очень высокая | Низкая | Средняя |

## Рекомендации по выбору

### Для поведенческого клонирования (BC)
- **Рекомендация:** Изображения + история действий
- **Причина:** Максимальное соответствие человеческим демонстрациям

### Для RL с нуля
- **Рекомендация:** Checkpoint + координаты из API
- **Причина:** Быстрая сходимость, стабильные градиенты

### Для production/deployment
- **Рекомендация:** LIDAR + скорость
- **Причина:** Баланс между точностью и производительностью

### Для исследований
- **Рекомендация:** Полное состояние (координаты + ориентация + скорость)
- **Причина:** Максимальный контроль над экспериментом

## Связи с другими темами

- [[replay_learning_trackmania.md]] - Обучение на реплеях Trackmania: архитектура, сбор данных, обучение
- [[../../algorithms/classical_ml/reinforcement_learning/index.md]] - Основы обучения с подкреплением
- [[../../algorithms/classical_ml/reinforcement_learning/ppo_algorithm.md]] - PPO алгоритм для дообучения
- [[../../ai/imitation_learning/index.md]] - Обучение с подражанием
- [[../../ai/imitation_learning/behavioral_cloning.md]] - Поведенческое клонирование
- [[../../algorithms/neural_networks/convolutional/index.md]] - CNN для обработки изображений
- [[../../algorithms/neural_networks/recurrent/index.md]] - RNN/LSTM для временных последовательностей
- [[index.md]] - ИИ для игр: обзор раздела

## Источники

1. TMRL Documentation. Trackmania RL Library. URL: https://pypi.org/project/tmrl/
2. TMInterface Documentation. URL: https://donadigo.com/tminterface/
3. LouisDeOliveira. TMAI: A real-time TrackMania Nations environment for RL. GitHub. URL: https://github.com/LouisDeOliveira/TMAI
4. Trackmania RL Community. Training neural networks for Trackmania. URL: https://blog.tammearu.eu/posts/tm20ai/
5. Neinders, B. (2023). Improving Trackmania Reinforcement Learning Performance. University of Twente. URL: http://essay.utwente.nl/96153/1/Neinders_BA_EEMCS.pdf
6. EA SEED. (2024). OfflineMania: A Benchmark Environment for Offline Reinforcement Learning in Racing Games. CoG 2024.

```metadata
category: applications
subcategory: gaming_ai
tags: trackmania, reinforcement_learning, state_space, observation_space, track_representation, checkpoint_system, lidar, rl_environment, game_ai
```
