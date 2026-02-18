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

### 5. 3D-представление трассы (для поддержки прыжков и воздушных маневров)

**Ключевая проблема:** В Trackmania трассы трёхмерные, и лучшие реплеи часто содержат прыжки с одного сегмента трассы на другой (cut-ы, shortcuts через воздух). Традиционные 2D-представления (LIDAR из изображения, checkpoint-система на плоскости) не обеспечивают информацию, необходимую для обучения таким маневрам.

**Компоненты 3D-представления:**

```python
class Track3DRepresentation:
    def __init__(self):
        # 1. Полная 3D-геометрия трассы
        self.track_mesh = TrackMesh()  # вершины, грани, нормали
        
        # 2. 3D-чекпоинты (объёмные, а не плоские)
        self.checkpoints_3d = []  # [(x, y, z, radius), ...]
        
        # 3. Граф связности сегментов
        self.segment_graph = SegmentGraph()
        
        # 4. Воздушные коридоры (для прыжков)
        self.air_corridors = []  # [(start_pos, end_pos, min_speed), ...]
        
    def get_state(self, car_position, car_velocity):
        return {
            # Позиция и ориентация
            'position_3d': car_position,  # (x, y, z)
            'velocity_3d': car_velocity,  # (vx, vy, vz)
            'orientation': car_orientation,  # (yaw, pitch, roll)
            
            # Относительное положение на трассе
            'distance_to_surface': self.distance_to_track_surface(car_position),
            'nearest_segment': self.find_nearest_segment_3d(car_position),
            'reachable_segments': self.find_reachable_segments(car_position, car_velocity),
            
            # Информация для прыжков
            'airborne': not self.is_on_surface(car_position),
            'jump_trajectory': self.compute_jump_trajectory(car_position, car_velocity),
            'landing_zone': self.predict_landing_point(car_position, car_velocity),
            
            # 3D-чекпоинты
            'next_checkpoint_3d': self.get_next_checkpoint_3d(car_position),
            'checkpoint_direction_3d': self.get_checkpoint_direction_vector(car_position),
        }
```

**Детальные компоненты:**

#### 5.1. 3D-геометрия трассы (Track Mesh)

```python
class TrackMesh:
    def __init__(self):
        # Вершины трассы (включая высоту)
        self.vertices: List[Tuple[float, float, float]] = []
        
        # Грани (треугольники)
        self.faces: List[Tuple[int, int, int]] = []
        
        # Нормали граней (для определения "верх" поверхности)
        self.normals: List[Tuple[float, float, float]] = []
        
        # Типы поверхностей (асфальт, грунт, трамплин)
        self.surface_types: List[int] = []
    
    def raycast_to_surface(self, origin: Vector3, direction: Vector3) -> Optional[HitInfo]:
        """Пуск луча для определения расстояния до поверхности трассы"""
        # Используется для определения airborne-состояния
        pass
    
    def get_elevation_map(self, resolution: float) -> np.ndarray:
        """
        Создание карты высот трассы
        
        Returns:
            elevation_map: (H, W) - высота в каждой точке XY-плоскости
            passable_mask: (H, W) - можно ли проехать
        """
        pass
```

**Применение:**
- Определение состояния "в воздухе" vs "на земле"
- Вычисление оптимальных точек для прыжка
- Предсказание точки приземления

#### 5.2. 3D-чекпоинты (объёмные)

В отличие от традиционных 2D-чекпоинтов (плоские точки на поверхности), 3D-чекпоинты представляют собой объёмные области:

```python
class Checkpoint3D:
    def __init__(self, position: Vector3, radius: float, is_airborne: bool = False):
        self.position = position  # (x, y, z)
        self.radius = radius  # радиус сферы
        self.is_airborne = is_airborne  # чекпоинт в воздухе (для прыжков)
        
    def is_passed(self, car_position: Vector3) -> bool:
        """Проверка прохождения чекпоинта (сфера, а не точка)"""
        distance = np.linalg.norm(car_position - self.position)
        return distance <= self.radius
```

**Типы 3D-чекпоинтов:**
1. **Наземные**: На поверхности трассы (стандартные)
2. **Воздушные**: В воздухе (для прыжков, shortcuts)
3. **Ворота**: Плоские области в 3D-пространстве (для прыжков между сегментами)

#### 5.3. Граф связности сегментов

```python
class SegmentGraph:
    def __init__(self):
        # Узлы = сегменты трассы
        self.segments: List[TrackSegment] = []
        
        # Рёбра = возможные переходы между сегментами
        # Включая воздушные переходы (прыжки)
        self.edges: List[SegmentEdge] = []
    
    def add_jump_edge(self, from_segment: int, to_segment: int, 
                      jump_info: JumpInfo):
        """
        Добавление ребра прыжка между сегментами
        
        Args:
            from_segment: индекс сегмента старта
            to_segment: индекс сегмента приземления
            jump_info: информация о прыжке
        """
        edge = SegmentEdge(
            from_seg=from_segment,
            to_seg=to_segment,
            edge_type='jump',
            required_speed=jump_info.min_speed,
            takeoff_position=jump_info.takeoff_point,
            landing_position=jump_info.landing_point,
            trajectory=jump_info.trajectory,
            success_probability=jump_info.success_rate,
        )
        self.edges.append(edge)
    
    def find_shortest_path_with_jumps(self, start: Vector3, goal: Vector3) -> List[int]:
        """
        Поиск оптимального пути с учётом прыжков
        
        Returns:
            sequence сегментов + прыжков
        """
        # A* или Dijkstra на графе с jump edges
        pass
```

**JumpInfo структура:**
```python
@dataclass
class JumpInfo:
    takeoff_point: Vector3      # точка отрыва
    landing_point: Vector3      # точка приземления
    min_speed: float            # минимальная скорость для прыжка
    optimal_speed: float        # оптимальная скорость
    trajectory: List[Vector3]   # дискретизированная траектория
    flight_time: float          # время полёта
    success_rate: float         # вероятность успеха (из реплеев)
    time_saved: float           # экономия времени vs обычный путь
```

#### 5.4. Воздушные коридоры (Air Corridors)

Для поддержки обучения прыжкам между сегментами вводятся "воздушные коридоры" — объёмные области, через которые должен пролететь автомобиль:

```python
class AirCorridor:
    def __init__(self, entry: Vector3, exit: Vector3, 
                 corridor_radius: float, min_speed: float):
        self.entry = entry          # входная точка
        self.exit = exit            # выходная точка
        self.radius = corridor_radius  # радиус коридора
        self.min_speed = min_speed     # минимальная скорость
        
    def is_in_corridor(self, position: Vector3) -> bool:
        """Проверка нахождения в воздушном коридоре"""
        # Расстояние до центральной линии коридора
        line_segment = LineSegment(self.entry, self.exit)
        distance = line_segment.distance_to_point(position)
        return distance <= self.radius
    
    def get_direction_vector(self, position: Vector3) -> Vector3:
        """Вектор направления к выходу из коридора"""
        return normalize(self.exit - position)
```

**Применение:**
- Награда за нахождение в коридоре во время прыжка
- Штраф за отклонение от коридора
- Обучение точным прыжкам через corridor-based reward

#### 5.5. Наблюдения для 3D-представления

**Полное пространство наблюдений с 3D-информацией:**

```python
observation_3d = {
    # Основное состояние машины
    'position': (3,),          # (x, y, z)
    'velocity': (3,),          # (vx, vy, vz)
    'orientation': (3,),       # (yaw, pitch, roll)
    'angular_velocity': (3,),  # (wx, wy, wz)
    'speed': (1,),             # скаляр скорости
    
    # Состояние относительно трассы
    'on_surface': (1,),        # бинарно: на земле или в воздухе
    'surface_distance': (1,),  # расстояние до поверхности
    'surface_normal': (3,),    # нормаль поверхности под машиной
    
    # 3D-чекпоинты
    'next_checkpoint_rel': (3,),  # относительный вектор к чекпоинту
    'checkpoint_distance': (1,),  # расстояние до чекпоинта
    
    # Воздушные коридоры (если активен прыжок)
    'in_air_corridor': (1,),      # бинарно
    'corridor_direction': (3,),   # вектор к выходу
    'corridor_deviation': (1,),   # отклонение от центра
    
    # Граф сегментов
    'current_segment': (1,),      # индекс текущего сегмента
    'reachable_segments': (N,),   # one-hot достижимых сегментов
    'jump_opportunity': (1,),     # вероятность успешного прыжка
    
    # LIDAR (дополнительно, для избежания столкновений)
    'lidar_3d': (4, 19),          # 3D LIDAR (с высотой)
    
    # Визуальные признаки (опционально)
    'visual_features': (512,),    # из CNN
}
```

**Размерность:** ~600-700 скаляров (в зависимости от количества сегментов)

#### 5.6. Функция вознаграждения для 3D-обучения

```python
def compute_reward_3d(state, next_state, action, jump_info=None):
    """
    Комбинированная награда с поддержкой 3D-маневров
    """
    reward = 0.0
    
    # 1. Прогресс по 3D-треку (основная награда)
    progress = next_state.checkpoint_progress - state.checkpoint_progress
    reward += progress * 1.0
    
    # 2. Награда/штраф за прыжки
    if state.airborne:
        if jump_info and jump_info.is_valid_jump():
            # Награда за нахождение в воздушном коридоре
            corridor_reward = 1.0 - jump_info.corridor_deviation
            reward += corridor_reward * 0.5
            
            # Бонус за успешный прыжок (в момент приземления)
            if next_state.just_landed and jump_info.successful:
                reward += jump_info.time_saved * 2.0  # бонус за экономию времени
        else:
            # Штраф за неконтролируемый полёт
            reward -= 0.2
    
    # 3. Штраф за приземление не на ту поверхность
    if next_state.just_landed:
        if not next_state.landed_on_valid_surface:
            reward -= 5.0  # серьёзный штраф за падение
    
    # 4. Штраф за столкновение/переворот
    if state.is_crashed or state.is_upside_down:
        reward -= 0.5
    
    # 5. Бонус за использование shortcuts через прыжки
    if action['jump'] and jump_info and jump_info.is_shortcut:
        reward += jump_info.time_saved * 3.0
    
    return reward
```

**Преимущества 3D-представления:**
- Поддержка обучения сложным воздушным маневрам
- Возможность находить и использовать shortcuts через прыжки
- Более точное моделирование физики полёта
- Устойчивость к разным траекториям (включая воздушные)

**Недостатки:**
- Значительно большая сложность реализации
- Требует доступа к полной 3D-геометрии трассы
- Выше вычислительные затраты
- Сложнее сбор данных для обучения (нужны 3D-координаты из реплеев)

**Рекомендации по использованию:**
- Для **исследовательских задач** с фокусом на сложные маневры — использовать полное 3D-представление
- Для **production** — гибридный подход: 2D-представление + упрощённая 3D-информация (только для прыжков)
- Для **быстрого прототипирования** — начать с checkpoint + координаты, затем добавить 3D-компоненты

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

| Подход | Точность | Скорость | Переносимость | Сложность | Поддержка прыжков |
|--------|----------|----------|---------------|-----------|-------------------|
| **Checkpoint** | Средняя | Высокая | Высокая | Низкая | ❌ Нет |
| **LIDAR** | Средняя | Средняя | Высокая | Средняя | ❌ Нет |
| **Изображения (CNN)** | Высокая | Низкая | Очень высокая | Высокая | ⚠️ Косвенная |
| **Координаты (API)** | Очень высокая | Очень высокая | Низкая | Средняя | ⚠️ Частичная |
| **3D-представление** | Очень высокая | Средняя | Низкая | Очень высокая | ✅ Полная |

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

### Для обучения прыжкам и воздушным маневрам
- **Рекомендация:** Полное 3D-представление с воздушными коридорами
- **Причина:** Единственный подход, явно поддерживающий 3D-маневры между сегментами

### Гибридный подход (рекомендуется для большинства задач)
- **Базовый уровень:** Checkpoint + координаты + LIDAR
- **Для прыжков:** Добавить упрощённое 3D-представление (только 3D-чекпоинты + граф сегментов)
- **Компромисс:** Использовать 3D-информацию только в моментах, когда автомобиль в воздухе

## Связи с другими темами

- [[replay_learning_trackmania.md]] - Обучение на реплеях Trackmania: архитектура, сбор данных, обучение
- [[track_embedding_representations.md]] - Эмбеддинги трассы/пути для агентов: кодирование трассы в латентное пространство, графовые представления, VAE для траекторий — альтернативный подход к представлению трассы через компактные векторные представления
- [[../../algorithms/classical_ml/reinforcement_learning/index.md]] - Основы обучения с подкреплением
- [[../../algorithms/classical_ml/reinforcement_learning/ppo_algorithm.md]] - PPO алгоритм для дообучения
- [[../../ai/imitation_learning/index.md]] - Обучение с подражанием
- [[../../ai/imitation_learning/behavioral_cloning.md]] - Поведенческое клонирование
- [[../../algorithms/neural_networks/convolutional/index.md]] - CNN для обработки изображений
- [[../../algorithms/neural_networks/recurrent/index.md]] - RNN/LSTM для временных последовательностей
- [[../../algorithms/specialized/graph_neural_networks/index.md]] - Graph Neural Networks для кодирования структур трассы
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
tags: trackmania, reinforcement_learning, state_space, observation_space, track_representation, checkpoint_system, lidar, rl_environment, game_ai, 3d_representation, jump_maneuvers, air_corridors, track_geometry
```
