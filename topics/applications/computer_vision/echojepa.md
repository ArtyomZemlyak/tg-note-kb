# EchoJEPA: Латентная предиктивная foundation-модель для эхокардиографии

## Общее описание

**EchoJEPA (Echo Joint Embedding Predictive Architecture)** - это foundation-модель для эхокардиографии, представленная в работе "EchoJEPA: A Latent Predictive Foundation Model for Echocardiography". Модель обучена на **18 миллионах эхокардиограмм** от **300 000 пациентов**, что представляет собой крупнейший корпус предобучения для этой модальности на текущий момент.

EchoJEPA адаптирует архитектуру V-JEPA2 для ультразвуковой визуализации, используя латентный предиктивный объектив для обучения робастных анатомических представлений, игнорирующих спекл-шум и артефакты acquisitions.

## Проблема и мотивация

### Вызовы эхокардиографии

Foundation-модели для эхокардиографии сталкиваются с уникальными проблемами, обусловленными свойствами сигнала ультразвука:

- **Спекл-шум**: Стохастические спекл-паттерны доминируют в ультразвуковом видео
- **Затухание интенсивности**: Глубинно-зависимое затухание интенсивности
- **Акустические тени**: Артефакты, варьирующиеся между acquisitions и не связанные с анатомией сердца

### Ограничения существующих подходов

Существующие foundation-модели используют различные подходы, но ни один явно не нацелен на представления, инвариантные к шуму:

- **Supervised multitask learning** (PanEcho): Наследует шум аннотаций
- **Contrastive vision-language alignment** (EchoPrime): Выравнивается с языком отчетов, а не с анатомией
- **Masked autoencoding** (EchoFM): Должен точно воспроизводить спекл для минимизации потерь

## Архитектура EchoJEPA

### Латентный предиктивный объектив

EchoJEPA использует архитектуру joint-embedding predictive architecture (JEPA), которая обучает предиктор выводить эмбеддинги маскированных областей из видимого контекста, нацеливаясь на экспоненциальное скользящее среднее (EMA) teacher, а не на сырые пиксели.

**Ключевое преимущество**: Этот подход снижает вес непредсказуемых артефактов (спекл-шум) и усиливает временно когерентные структуры (геометрия камер, движение стенок).

### Основные компоненты

1. **Context Encoder (E_θ)**: Извлекает представления из видимых tubelets
2. **Predictor (P_φ)**: Принимает представления контекста и обучаемый mask token Δ_y, выводит эмбеддинги для маскированных областей
3. **Target Encoder (E_θ̄)**: Создает целевые предсказания, обновляется через EMA

### Функция потерь

Модель минимизирует L₁ расстояние между предсказанными и целевыми эмбеддингами:

```
L = || P_φ(E_θ(x), Δ_y) - sg(E_θ̄(y)) ||₁
```

где sg(·) - оператор stop-gradient, предотвращающий поток градиентов в target encoder.

## Адаптации для эхокардиографии

EchoJEPA адаптирует V-JEPA2 с тремя модификациями, учитывающими свойства сигнала ультразвука:

### 1. Временное разрешение

- **Изменение**: Увеличение частоты дискретизации с 4 fps до **24 fps**
- **Обоснование**: Сердечная динамика разворачивается быстро (некоторые процессы в пределах 50-100 мс), требуя более высокого временного разрешения

### 2. Aspect Ratio Augmentation

- **Изменение**: Сужение диапазона случайного aspect ratio с (0.75, 1.35) до **(0.9, 1.1)**
- **Обоснование**: Эхокардиографические виды следуют стандартизированным протоколам acquisitions с консистентной геометрией; агрессивная аугментация искажает клинически значимые пропорции камер

### 3. Crop Scale Augmentation

- **Изменение**: Корректировка диапазона случайного crop scale с (0.3, 1.0) до **(0.5, 1.0)**
- **Обоснование**: Ультразвуковой сектор имеет веерообразную геометрию; кропы ниже 50% рискуют полностью исключить сердечные структуры

## Модели и обучение

### Конфигурации моделей

| Модель | Backbone | Данные обучения | Видео |
|--------|----------|-----------------|-------|
| EchoJEPA-G | ViT-Giant (1.1B) | Проприетарные | 18.1M |
| EchoJEPA-L | ViT-Large (300M) | MIMIC-IV-Echo | 525K |
| VideoMAE-L | ViT-Large | MIMIC-IV-Echo | 525K |

**EchoJEPA-G**: Флагманская модель с ViT-Giant, предобученная на 18.1M проприетарных эхокардиограмм от различных популяций и производителей сканеров.

**EchoJEPA-L**: Модель с ViT-Large, обученная на публичном датасете MIMIC-IV-Echo (525K видео), доступна для внешней валидации методологии.

### Процесс обучения

Обучение проходит в две фазы:
1. **Предобучение**: Разрешение 224², 280 эпох
2. **Annealing**: Разрешение 336², 80 эпох с уменьшенным learning rate

## Multi-View Probing Framework

EchoJEPA представляет **multi-view probing framework** с factorized video stream embeddings для интеграции информации across views без view-specific компонентов.

### Структура исследования

Эхокардиографическое исследование S = {v₁, ..., v_N} содержит N видео клипов с associated view labels. Для клинической задачи с релевантным подмножеством views V_task выбирается одно видео на view.

### Архитектура

1. **Замороженный энкодер**: Извлекает эмбеддинги из каждого клипа
2. **Factorized embeddings**: E_view ∈ R^(V×D) и E_clip ∈ R^(C×D) - требуют только (V+C)×D параметров
3. **Self-attention блоки**: R-1 блоков с key padding mask для игнорирования missing views
4. **Learnable query**: Cross-attends к выходным токенам для финального представления

### Протокол

Все модели используют идентичные probes с глубиной R=4, 16 attention heads, и MLP ratio 4.

## Оценка робастности

EchoJEPA вводит **physics-informed perturbations**, симулирующие доминирующие режимы деградации в эхокардиографии:

### 1. Depth Attenuation

Симулирует затухание сигнала ультразвука с глубиной ткани (особенно у пациентов с ожирением или плохими акустическими окнами):

```
I'(x, y) = I(x, y) × (1 - α × y/H)
```

где α ∈ {0.3, 0.5, 0.7} контролирует серьезность затухания.

### 2. Acoustic Shadow

Симулирует тени от высокоотражающих структур (ребра, кальцификации):

```
I'(x, y) = I(x, y) × (1 - exp(-(x-x₀)²/2σ²))
```

где x₀ - центр тени, σ ∈ {0.1W, 0.2W, 0.3W} контролирует ширину тени.

## Экспериментальные результаты

### Датасеты

- **Toronto (Internal)**: N=150,000 исследований для probe training и внутренней валидации
- **Chicago (Internal)**: N=60,000 исследований как внешний holdout сайт
- **EchoNet-Dynamic**: 10,030 видео (Stanford) для внешней zero-shot оценки LVEF
- **EchoNet-Pediatric**: 3,316 видео для тестирования генерализации на педиатрические популяции

### Задачи оценки

1. **View Classification**: 12-классная идентификация стандартных видов (Accuracy %)
2. **LVEF Regression**: Фракция выброса левого желудочка из апикальных видов (MAE %)
3. **RVSP Regression**: Систолическое давление в правом желудочке из multi-view интеграции (MAE mmHg)

### Основные результаты

#### LVEF Estimation (MAE, меньше лучше)

| Модель | Toronto | Chicago | Stanford |
|--------|---------|---------|----------|
| EchoPrime | 5.33 | 6.71 | 4.87 |
| PanEcho | 5.43 | 6.52 | 5.10 |
| EchoMAE-L | 8.15 | 9.40 | 8.52 |
| EchoJEPA-L | 5.97 | 7.39 | 5.76 |
| **EchoJEPA-G** | **4.26** | **5.44** | **3.97** |

#### Sample Efficiency (View Classification, Accuracy %)

EchoJEPA демонстрирует выдающуюся sample efficiency:

| Модель | 1% labels | 10% labels | 100% labels |
|--------|-----------|------------|-------------|
| EchoPrime | 21.63 | 32.06 | 42.1 |
| PanEcho | 21.48 | 30.62 | 41.9 |
| EchoMAE-L | 21.86 | 34.47 | 40.4 |
| EchoJEPA-L | 57.55 | 80.06 | 85.5 |
| **EchoJEPA-G** | **78.63** | **84.42** | **87.4** |

**Ключевой результат**: EchoJEPA-G с 1% размеченных данных превосходит все baseline модели, обученные на 100% данных.

#### Robustness к акустическим perturbations

EchoJEPA демонстрирует превосходную робастность:
- **Деградация EchoJEPA**: Только 2% при physics-informed acoustic perturbations
- **Деградация конкурентов**: 17% у лучших baseline моделей
- EchoJEPA деградирует на **86% меньше** чем следующий лучший baseline

#### Zero-shot генерализация на педиатрических пациентов

Zero-shot производительность EchoJEPA на педиатрических пациентах **превосходит полностью fine-tuned baseline модели**, устанавливая латентное предсказание как превосходную парадигму для робастного, генерализуемого медицинского AI.

## Контролируемое сравнение: Латентное vs. Пиксельное предсказание

EchoJEPA-L и EchoMAE-L используют идентичную архитектуру (ViT-L), данные обучения (MIMIC-IV-Echo, 525K видео), аугментации и compute budget. Единственное различие - objective:

| Модель | Objective | LVEF MAE ↓ | View Acc ↑ |
|--------|-----------|------------|------------|
| EchoMAE-L | Reconstruction | 8.15 | 40.4 |
| EchoJEPA-L | Latent Prediction | 5.97 | 85.5 |
| **Улучшение** | | **-26.7%** | **+45.1%** |

Этот результат подтверждает, что латентное предсказание предлагает превосходную производительность над пиксельной реконструкцией для ультразвука.

## Вклад

1. **EchoJEPA**: Первая foundation-scale архитектура JEPA для эхокардиографии, обученная на 18M видео от 300K пациентов
2. **Multi-view probing framework**: Метод с factorized video stream embeddings и attention masking для интеграции информации across views
3. **Unified evaluation protocol**: Стандартизированный benchmark с frozen backbones, идентичными probes и консистентными гиперпараметрами
4. **Robustness benchmarks**: Physics-informed perturbations, выявляющие превосходную робастность EchoJEPA
5. **Public release**: Открытый исходный код EchoJEPA-L и evaluation framework

## Связь с другими архитектурами

EchoJEPA является частью семейства JEPA архитектур:

- **I-JEPA**: Image-based JEPA для статических изображений - первоисточник
- **V-JEPA**: Video JEPA для видеообработки - прямое расширение
- **VL-JEPA**: Vision-Language JEPA для мультимодальных задач
- **LeJEPA**: Theoretically-grounded JEPA с доказуемой оптимальностью

## Применение

### Клинические приложения

- **Автоматическая оценка LVEF**: Стандартизированная оценка функции сердца
- **Оценка RVSP**: Диагностика легочной гипертензии
- **Классификация видов**: Триаж для автоматизированных пайплайнов
- **Педиатрическая эхокардиография**: Zero-shot генерализация на детские популяции

### Исследовательские приложения

- **Сравнительный анализ foundation моделей**: Unified evaluation protocol
- **Изучение робастности**: Physics-informed perturbations для оценки устойчивости
- **Sample efficiency исследования**: Обучение с малым количеством размеченных данных

## Новые концепции и термины

- **EchoJEPA**: Foundation модель для эхокардиографии на основе JEPA архитектуры
- **Латентный предиктивный объектив**: Предсказание эмбеддингов вместо пиксельной реконструкции
- **Multi-view probing framework**: Framework для интеграции информации из multiple echocardiographic views
- **Physics-informed perturbations**: Симулированные деградации на основе физики ультразвука
- **Factorized video stream embeddings**: Эффективное кодирование stream identity с (V+C)×D параметров
- **Sample efficiency**: Способность модели обучаться с малым количеством размеченных данных

## Связи с другими темами

- [[v_jepa.md]] - V-JEPA как предшественник EchoJEPA для видеообработки
- [[i_jepa.md]] - I-JEPA как foundational архитектура для JEPA семейства
- [[vl_jepa_model.md]] - VL-JEPA как мультимодальное расширение JEPA
- [[jepa_models_comprehensive_summary.md]] - Полный обзор JEPA архитектур
- [[self_supervised_learning.md]] - Самоконтролируемое обучение как основа JEPA
- [[medical_imaging.md]] - Медицинская визуализация как область применения
- [[foundation_models.md]] - Foundation модели как общий контекст

## Визуализации

![EchoJEPA Architecture](../../../media/doc_1771308679_6553d241_arxiv_2602.02603.pdf)
*Рисунок 1: Архитектура EchoJEPA. Эхокардиограммы из multiple views партиционируются в spatio-temporal tubelets и разделяются на маскированные и не маскированные наборы. Encoder E_θ обрабатывает видимые кадры, predictor P_φ выводит эмбеддинги для маскированных областей.*

![Multi-view Probing Framework](../../../media/doc_1771308679_6553d241_arxiv_2602.02603.pdf)
*Рисунок 2: Multi-view probing framework. Замороженный EchoJEPA encoder извлекает видео эмбеддинги из multiple echocardiographic views. Каждый эмбеддинг аугментируется learnable view и clip stream embeddings.*

![Downstream Evaluation](../../../media/doc_1771308679_6553d241_arxiv_2602.02603.pdf)
*Рисунок 3: Downstream оценка. EchoJEPA оценивается на трех клинических задачах с frozen backbones и lightweight probes: RVSP estimation, LVEF regression, и view classification.*

## Источники

1. **EchoJEPA: A Latent Predictive Foundation Model for Echocardiography** - https://arxiv.org/abs/2602.02603
   - Авторы: Alif Munim, Adibvafa Fallahpour, Teodora Szasz, Ahmadreza Attarpour, River Jiang, Brana Sooriyakanthan, Maala Sooriyakanthan, Heather Whitney, Jeremy Slivnick, Barry Rubin, Wendy Tsang, Bo Wang
   - Опубликовано: Февраль 2026
   - Ключевые результаты: 18M видео, 300K пациентов, SOTA на LVEF и RVSP estimation

2. **V-JEPA 2** - https://arxiv.org/abs/2512.10942
   - Базовая архитектура для EchoJEPA

3. **MIMIC-IV-Echo** - https://physionet.org/content/mimic-iv-echo/
   - Публичный датасет для EchoJEPA-L

4. **EchoNet-Dynamic** - https://echonet.github.io/dynamic/
   - Датасет для внешней валидации

## Дополнительные материалы

- **GitHub репозиторий**: https://github.com/bowang-lab/EchoJEPA
- **EchoNet-Pediatric**: Датасет для педиатрической эхокардиографии

```metadata
category: applications
subcategory: computer_vision
tags: echocardiography, foundation_models, JEPA, medical_imaging, self_supervised_learning, ultrasound, latent_prediction
```
