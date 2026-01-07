# Механизм REPL в Рекурсивных Языковых Моделях (RLM)

## Общее описание

Механизм REPL (Read-Eval-Print Loop) в контексте Рекурсивных Языковых Моделей (RLM) представляет собой ключевую архитектурную особенность, позволяющую модели программно взаимодействовать с длинными промптами как с переменными в программной среде. В отличие от традиционного подхода, где контекст напрямую подается в нейронную сеть, в RLM контекст загружается как переменная внутри среды REPL, что позволяет модели использовать программные инструменты для его анализа, разбиения и обработки.

## Архитектура и реализация

### Основные компоненты

1. **Контекст как переменная**: Входной промпт P устанавливается как значение переменной в среде REPL (обычно на Python)

2. **Функция llm_query**: Специальная функция, позволяющая запрашивать под-LLM изнутри REPL-среды, обычно с окном контекста около 500K символов

3. **Возможность печати**: Использование print() для просмотра результатов выполнения кода и продолжения рассуждения

4. **Переменные-буферы**: Возможность сохранять промежуточные результаты в переменных для построения финального ответа

### Системный промпт для RLM с REPL (GPT-5)

```
You are tasked with answering a query with associated context. You can access, transform, and analyze this context interactively in a REPL environment that can recursively query sub-LLMs, which you are strongly encouraged to use as much as possible. You will be queried iteratively until you provide a final answer. Your context is a {context_type} with {context_total_length} total characters, and is broken up into chunks of char lengths: {context_lengths}. The REPL environment is initialized with: 1. A 'context' variable that contains extremely important information about your query. You should check the content of the 'context' variable to understand what you are working with. Make sure you look through it sufficiently as you answer your query. 2. A 'llm_query' function that allows you to query an LLM (that can handle around 500K chars) inside your REPL environment. 3. The ability to use 'print()' statements to view the output of your REPL code and continue your reasoning.
```

## Стратегии использования REPL в RLM

### 1. Стратегия поиска "магического числа"

Пример использования:
```python
chunk = context[:10000]
answer = llm_query(f"What is the magic number in the context? Here is the chunk: {chunk}")
print(answer)
```

### 2. Итеративное разбиение и анализ

Пример:
```python
query = "In Harry Potter and the Sorcerer's Stone, did Gryffindor win the House Cup because they led?"
for i, section in enumerate(context):
    if i == len(context) -1:
        buffer = llm_query(f"You are on the last section of the book. So far you know that: {buffers}. Gather from this last section to answer {query}. Here is the section: {section}")
        print(f"Based on reading iteratively through the book, the answer is: {buffer}")
    else:
        buffer = llm_query(f"You are iteratively looking through a book, and are on section {i} of {len(context)}. Gather information to help answer {query}. Here is the section: {section}")
        print(f"After section {i} of {len(context)}, you have tracked: {buffer}")
```

### 3. Комбинация фрагментов и рекурсивный запрос

Пример:
```python
query = "A man became famous for his book 'The Great Gatsby'. How many jobs did he have?"
chunk_size = len(context) // 10
answers = []
for i in range(10):
    if i < 9:
        chunk_str = "\n".join(context[i*chunk_size:(i+1)*chunk_size])
    else:
        chunk_str = "\n".join(context[i*chunk_size:])
    answer = llm_query(f"Try to answer the following query: {query}. Here are the documents:\n{chunk_str}. Only answer if you are confident in your answer based on the evidence.")
    answers.append(answer)
    print(f"I got the answer from chunk {i}: {answer}")

final_answer = llm_query(f"Aggregating all the answers per chunk, answer the original query about total number of jobs: {query}\n\nAnswers:\n" + "\n".join(answers))
```

## Преимущества использования REPL в RLM

1. **Программное взаимодействие с контекстом**: Возможность использовать полноценные программные инструменты (регулярные выражения, структуры данных, алгоритмы) для анализа контекста

2. **Фильтрация и выборочная обработка**: Модель может сначала отфильтровать контекст с помощью кода, а затем использовать под-LLM только для наиболее релевантных частей

3. **Масштабируемость**: Возможность обрабатывать контексты, превышающие физические ограничения модели, за счет декомпозиции

4. **Семантическая обработка**: Комбинирование программной логики и семантического понимания для сложных задач

## Практические паттерны в REPL-траекториях RLM

1. **Поиск по регулярным выражениям**: Использование регулярных выражений для поиска фрагментов, содержащих ключевые слова из промпта

2. **Разбиение по разделителям**: Регулярное разбиение контекста по переносам строк или заголовкам

3. **Создание буферов**: Сохранение промежуточных результатов в переменных для последующей агрегации

4. **Верификация результатов**: Использование под-LLM вызовов для проверки корректности промежуточных результатов

## Влияние на производительность

- **API-стоимость**: RLM показали сопоставимую или даже более низкую стоимость по сравнению с базовыми моделями на длинных контекстах
- **Время выполнения**: Может быть значительно улучшено за счет асинхронности вызовов LLM
- **Вариативность**: Высокая вариативность затрат из-за различий в длине траекторий RLM в зависимости от сложности задачи

## Сравнение с другими архитектурами

| Архитектура | Взаимодействие с контекстом | Рекурсивные вызовы | Доступ к инструментам |
|-------------|----------------------------|-------------------|----------------------|
| Традиционный LLM | Прямое | Нет | Ограниченный |
| RLM с REPL | Программное | Да | Полный доступ к Python |
| CodeAct | Прямой промпт + код | Нет (обычно) | Через действия |
| RAG | Векторный ретривал | Нет | Ограниченный |

## Использование в задачах разной сложности

- **Низкая информационная плотность**: Разбиение кода и рекурсивные под-запросы к LLM для поиска подсказок
- **Высокая информационная плотность**: Семантическая классификация строк с помощью рекурсивных вызовов
- **Длинный вывод**: Сохранение результатов под-LLM в переменных для построения финального ответа

## Связи с другими темами

- [[../models/recursive_language_models.md]] - Общее описание RLM
- [[../../applications/nlp/memory_architectures/retrieval_augmented_generation.md]] - Другие подходы к работе с внешней информацией
- [[../../algorithms/neural_networks/transformers/tools/metatool_framework.md]] - Рамки для интеграции инструментов в LLM
- [[../../algorithms/neural_networks/transformers/memory/mcp_model_context_protocol.md]] - Протокол для управления контекстом в системах LLM

## Источники

- Zhang, A. L., Kraska, T., & Khattab, O. Recursive Language Models. arXiv preprint arXiv:2512.24601, 2025. URL: https://arxiv.org/abs/2512.24601