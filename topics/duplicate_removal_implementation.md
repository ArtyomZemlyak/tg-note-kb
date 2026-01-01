# Рекомендации по устранению дубликатов в базе знаний

## Обзор

На основе анализа, проведенного в [duplicate_analysis_summary.md](duplicate_analysis_summary.md) <!-- TODO: Broken link -->, настоящий документ содержит конкретные инструкции по устранению дубликатов и оптимизации структуры базы знаний.

## Необходимые действия

### 1. Удаление дублирующихся файлов

#### 1.1 Удалить файл с дублирующей информацией о Mamba

```bash
# Файл для удаления:
rm "/app/knowledge_base/tg-note-kb/topics/algorithms_and_models/transformer_architectures/mamba_architecture.md"
```

**Примечание**: Основной файл с полной информацией находится в `/app/knowledge_base/tg-note-kb/topics/algorithms_and_models/neural_networks/architectures/mamba_architecture.md`

#### 1.2 Удалить файл с дублирующей информацией о механистической интерпретируемости

```bash
# Файл для удаления:
rm "/app/knowledge_base/tg-note-kb/topics/foundations_and_theory/interpretability/mechanistic_interpretability.md"
```

**Примечание**: Основной файл с полной информацией находится в `/app/knowledge_base/tg-note-kb/topics/algorithms_and_models/transformer_architectures/mechanistic_interpretability.md`

### 2. Обновление внутренних ссылок

После удаления файлов необходимо обновить все внутренние ссылки в базе знаний, которые указывали на удаленные файлы.

#### 2.1 Обновление ссылок на Mamba архитектуру

Найти и заменить все вхождения:
- `[[../../algorithms_and_models/transformer_architectures/mamba_architecture.md]]` → `[[../../algorithms_and_models/neural_networks/architectures/mamba_architecture.md]]`

#### 2.2 Обновление ссылок на механистическую интерпретируемость

Найти и заменить все вхождения:
- `[[../../algorithms_and_models/transformer_architectures/mechanistic_interpretability.md]]` → `[[../../algorithms_and_models/transformer_architectures/mechanistic_interpretability.md]]` (Файл остается, просто корректируем ссылки, ведущие на дубликат)
- `[[../../foundations_and_theory/interpretability/mechanistic_interpretability.md]]` → `[[../../algorithms_and_models/transformer_architectures/mechanistic_interpretability.md]]`

### 3. Консолидация структурированного прунинга

#### 3.1 Объединение содержимого файлов

Создать единый файл с полной информацией о структурированном прунинге:

```bash
# Объединить содержимое из двух файлов в один, размещенный в:
# /app/knowledge_base/tg-note-kb/topics/algorithms_and_models/transformer_architectures/optimization/structured_pruning.md
```

Содержимое объединенного файла должно включать всю информацию из обоих исходных файлов, с устранением дубликатов внутри самого файла.

### 4. Проверка целостности ссылок

После выполнения всех изменений необходимо:

1. Проверить все внутренние ссылки на разрывы
2. Убедиться, что все файлы, на которые ссылаются другие файлы, действительно существуют
3. Проверить, что нет "битых" (broken) ссылок

## Проверка выполнения

После реализации этих изменений:

1. Проверить, что количество файлов с одинаковыми именами уменьшилось
2. Убедиться, что вся информация из удаленных файлов доступна в основных файлах
3. Убедиться, что структура навигации не нарушена
4. Проверить, что метаданные и внутренние ссылки обновлены корректно

## Источники

1. [duplicate_analysis_summary.md](duplicate_analysis_summary.md) <!-- TODO: Broken link --> - Анализ дубликатов, на котором основаны эти рекомендации
2. Результаты анализа файлов в базе знаний
3. Структура каталогов и файлов в `/app/knowledge_base/tg-note-kb/topics/`

```metadata
category: knowledge_base_optimization
subcategory: implementation_guide
tags: knowledge_base, optimization, duplicates, cleanup, instructions
```