# Методы расширения контекста в LLM (Context Extension Methods)

## Общее описание

Методы расширения контекста позволяют увеличить длину последовательности, которую языковые модели могут эффективно обрабатывать. Это критически важно для задач, требующих понимания длинных документов, больших diff кода, юридических текстов и других сценариев с большим объемом информации.

## Категории методов

### 1. Позиционные эмбеддинги и их модификации

#### RoPE (Rotary Positional Embeddings)
- Используются в современных архитектурах для кодирования позиции токенов
- Позволяют некоторую экстраполяцию длины через интерполяцию

#### Интерполяционные методы
- Linear interpolation
- Dynamic NTK (Neural Tangent Kernel) scaling
- YaRN (Yet another RoPE extension)

#### DroPE (Drop Positional Embeddings)
- Метод от Sakana AI для "выбрасывания" позиционных эмбеддингов после обучения
- Позволяет zero-shot экстраполяцию длины
- Требует минимальных вычислительных затрат по сравнению с тонкой настройкой
- [[../foundations/ml_theory/drope.md]] - Подробное описание DroPE

### 2. Архитектурные изменения

#### Модификации внимания
- Sparse attention (например, Longformer, BigBird)
- Linear attention (Linformer, Performer)
- Linear-complexity attention (Mamba, RetNet)

#### Механизмы памяти
- External memory networks
- Retrieval-augmented generation (RAG)
- Memory-augmented transformers

### 3. Методы обучения и дообучения

#### Curriculum learning
- Постепенное увеличение длины контекста во время обучения
- Техники для стабилизации обучения на длинных последовательностях

#### Fine-tuning на длинных контекстах
- Дообучение модели на более длинных последовательностях, чем видела на предобучении
- Методы калибровки для расширения контекста

## Сравнение методов

| Метод | Требует переобучения | Эффективность | Сложность реализации | Рекомендуемые сценарии |
|-------|---------------------|---------------|---------------------|------------------------|
| DroPE | Минимальное (калибровка) | Высокая | Низкая | Zero-shot экстраполяция длины |
| RoPE интерполяция | Нет | Средняя | Низкая | Легкое расширение контекста |
| Sparse attention | Да | Высокая | Средняя | Длинные документы, код |
| RAG | Нет | Высокая | Средняя | Внешняя информация, базы знаний |
| Fine-tuning | Да | Очень высокая | Высокая | Конкретные задачи с длинным контекстом |

## Применения

### 1. Обработка юридических документов
- Анализ контрактов на сотни страниц
- Поиск релевантной информации в правовых базах

### 2. Работа с кодом
- Обработка больших diff файлов
- Понимание монорепозиториев
- Code generation с контекстом всего проекта

### 3. Научные исследования
- Анализ научных работ
- Обработка экспериментальных данных
- Генерация отчетов

## Связи с другими темами

- [[../algorithms/neural_networks/transformers/long_context_handling_methods.md]] - подробные методы обработки длинного контекста
- [[../algorithms/neural_networks/transformers/context_limits_vs_positional_embeddings.md]] - анализ ограничений контекста и влияния позиционных эмбеддингов
- [[../foundations/ml_theory/positional_embeddings.md]] - различные типы позиционных эмбеддингов
- [[../algorithms/neural_networks/transformers/ruler_benchmark.md]] - бенчмарк для оценки длинноконтекстных возможностей
- [[../algorithms/neural_networks/transformers/training/ultra_long_context_curriculum_learning.md]] - методы обучения с длинным контекстом

## Источники

- "RULER: What's the Real Context Size of Your Long-Context Language Model?" (arXiv:2404.06654)
- "DroPE: Drop Positional Embeddings for Extended Context Lengths" (arXiv:2512.12167)
- Various RoPE interpolation and extension papers
- Sparse attention mechanism papers (Longformer, BigBird, etc.)