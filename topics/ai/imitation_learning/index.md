# Обучение с подражанием (Imitation Learning)

## Обзор

Раздел посвящен методам обучения с подражанием (Imitation Learning, IL) и поведенческому клонированию (Behavioral Cloning, BC) — подходам к обучению ИИ-агентов через демонстрации эксперта вместо обучения методом проб и ошибок.

## Основные концепции

**Обучение с подражанием** позволяет агенту учиться, наблюдая за действиями эксперта (человека или оптимального контроллера). Это особенно полезно когда:
- Функция вознаграждения неизвестна или сложна для определения
- Прямое обучение с подкреплением требует слишком много взаимодействий
- Экспертные демонстрации легко доступны (реплеи в играх, записи действий)

**Поведенческое клонирование** — простейший метод IL, формулируемый как задача супервизированного обучения на парах (состояние, действие).

## Ключевые методы

### Поведенческое клонирование (Behavioral Cloning)
- Супервизированное обучение на парах состояние-действие
- Простота реализации, высокая эффективность
- Проблема: каскадное накопление ошибок

[[behavioral_cloning.md]] - Подробное описание поведенческого клонирования, архитектур, проблем и решений

### DAGGER (Dataset Aggregation)
- Итеративный алгоритм с агрегацией данных
- Решает проблему накопления ошибок
- Гарантирует линейный рост ошибок вместо квадратичного

[[imitation_learning_methods.md]] - Обзор методов IL включая DAGGER, GAIL, IRL

### GAIL (Generative Adversarial Imitation Learning)
- Состязательный подход с использованием GAN
- Генератор vs Дискриминатор
- Может превзойти эксперта в некоторых задачах

### Обратное обучение с подкреплением (Inverse RL)
- Извлечение функции вознаграждения из демонстраций
- Затем использование RL для обучения оптимальной политики

## Применение в играх

Обучение на реплеях — практическое применение IL к видеоиграм:

- **Trackmania**: Обучение вождению по реплеям людей (скриншоты 64 FPS + логи клавиш)
- **Super Mario Bros**: Прохождение уровней по демонстрациям
- **Minecraft**: Навигация, строительство, крафт
- **StarCraft II, Dota 2**: Стратегическое управление

[[../../applications/gaming_ai/replay_learning_trackmania.md]] - Практическое руководство по обучению на реплеях Trackmania

## Связь с обучением с подкреплением

IL часто комбинируется с RL:

1. **Предобучение**: BC для инициализации политики перед RL
2. **Комбинирование**: BC loss + RL loss в многозадачном обучении
3. **Дообучение**: Fine-tuning BC модели через PPO/SAC
4. **Дистилляция**: Извлечение политики из RL-агента через BC

## Основные проблемы

| Проблема | Описание | Решения |
|----------|----------|---------|
| Compounding errors | Каскадное накопление ошибок | DAGGER, data augmentation |
| Ограниченное покрытие | Эксперт посещает не все состояния | Сбор разнообразных данных, активное обучение |
| Мультимодальность | Несколько правильных действий | Стохастические политики, Conditional VAE |
| Нарушение i.i.d. | Зависимость распределения от политики | Итеративные методы (DAGGER) |

## Содержание раздела

- [[behavioral_cloning.md]] - Поведенческое клонирование: основы, архитектуры, применение
- [[imitation_learning_methods.md]] - Методы обучения с подражанием: DAGGER, GAIL, IRL

## Связи с другими темами

- [[../../algorithms/classical_ml/reinforcement_learning/index.md]] - Обучение с подкреплением
- [[../../algorithms/classical_ml/reinforcement_learning/survey_rl_comprehensive.md]] - Обзор RL методов
- [[../../algorithms/classical_ml/reinforcement_learning/deep_rl/yandex_practical_rl_course.md]] - Практический курс RL
- [[../../algorithms/classical_ml/reinforcement_learning/deep_rl/huggingface_deep_rl_course.md]] - Deep RL курс
- [[../../algorithms/classical_ml/reinforcement_learning/ppo_algorithm.md]] - PPO алгоритм
- [[../../algorithms/classical_ml/supervised/index.md]] - Супервизированное обучение
- [[../../algorithms/neural_networks/convolutional/index.md]] - Сверточные сети
- [[../../algorithms/neural_networks/recurrent/index.md]] - Рекуррентные сети
- [[../../applications/gaming_ai/replay_learning_trackmania.md]] - Обучение на реплеях Trackmania

## Источники

1. Ross, S., & Bagnell, J. A. (2010). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. AISTATS 2011.
2. Ho, J., & Ermon, S. (2016). Generative Adversarial Imitation Learning. NeurIPS 2016.
3. Hussein, A., et al. (2017). Imitation Learning: A Survey of Learning Methods. ACM Computing Surveys.

```metadata
category: artificial_intelligence
subcategory: imitation_learning
tags: imitation_learning, behavioral_cloning, learning_from_demonstration, expert_policy, dagger, gail
```
