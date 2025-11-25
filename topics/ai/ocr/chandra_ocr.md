# Chandra OCR

## Общее описание

Chandra OCR - это современная модель оптического распознавания символов (OCR), разработанная DataLab. Модель преобразует документы в форматы markdown, HTML и JSON с детальной информацией о макете. Обладает высокой точностью при извлечении текста из изображений и PDF-файлов.

## Особенности

- **Преобразование документов** в форматы markdown, html или json с детальной информацией о макете
- **Хорошая поддержка рукописного текста** - эффективно распознает как печатный, так и рукописный текст
- **Точное воссоздание форм** - включая флажки (checkboxes), что делает её полезной для обработки анкет и форм
- **Поддержка сложных структур** - таблиц, математических формул и сложных макетов
- **Извлечение изображений и диаграмм** с подписями и структурированными данными
- **Поддержка более 40 языков**, включая русский
- **Два режима инференса**: локальный (HuggingFace) и удаленный (vLLM сервер)

## Технические характеристики

- **Количество параметров**: 9 миллиардов
- **Тип задачи**: Image-to-Text
- **Тип тензоров**: Safetensors, BF16
- **Лицензия**: Apache 2.0

## Результаты тестирования

Chandra OCR показала лучший результат по сравнению с другими OCR-моделями на бенчмарке olmocr:

| Модель | Результат |
|--------|-----------|
| Datalab Chandra v0.1.0 | 83.1 ± 0.9 |
| Datalab Marker v1.10.0 | 76.5 ± 1.0 |
| Deepseek OCR | 75.4 ± 1.0 |
| Mistral OCR API | 72.0 ± 1.1 |
| GPT-4o (Anchored) | 69.9 ± 1.1 |

## Установка и использование

### Установка
```
pip install chandra-ocr
```

### Использование через CLI
```
# С использованием VLLM
chandra_vllm
chandra input.pdf ./output

# С использованием HuggingFace
chandra input.pdf ./output --method hf

# Интерактивное приложение Streamlit
chandra_app
```

### Использование в коде
```python
from chandra.model import InferenceManager
from chandra.model.schema import BatchInputItem

# Запустите chandra_vllm для начала работы с сервером vLLM, если передаете vllm, в противном случае передайте hf
# вы можете также запустить свой собственный сервер vllm с моделью datalab-to/chandra
manager = InferenceManager(method="vllm")
batch = [
    BatchInputItem(
        image=PIL_IMAGE,
        prompt_type="ocr_layout"
    )
]
result = manager.generate(batch)[0]
print(result.markdown)
```

### С использованием Transformers
```python
from transformers import AutoModel, AutoProcessor
from chandra.model.hf import generate_hf
from chandra.model.schema import BatchInputItem
from chandra.output import parse_markdown

model = AutoModel.from_pretrained("datalab-to/chandra").cuda()
model.processor = AutoProcessor.from_pretrained("datalab-to/chandra")

batch = [
    BatchInputItem(
        image=PIL_IMAGE,
        prompt_type="ocr_layout"
    )
]

result = generate_hf(batch, model)[0]
markdown = parse_markdown(result.raw)
```

## Примеры использования

- **Таблицы** - водоустойчивые формы, отчеты 10K
- **Формы** - рукописные формы, договоры аренды
- **Рукописный текст** - медицинские записи, домашние задания по математике
- **Книги** - учебники географии, задачи
- **Математика** - внимательные диаграммы, рабочие листы
- **Газеты** - New York Times, LA Times
- **Прочее** - расшифровка, блок-схемы

## Ссылки

- [Официальный репозиторий на GitHub](https://github.com/datalab-to/chandra)
- [Модель на HuggingFace](https://huggingface.co/datalab-to/chandra)
- [Демонстрация](https://www.datalab.to/playground/documents/new)

## Связи с другими темами

- [[./hunyuanocr.md]] - Компактная OCR-модель от Tencent с 1 миллиардом параметров, достигающая SOTA результатов, конкурент Chandra OCR по эффективности
- [[./object_detection_yolo_ocr.md]] - Общие концепции OCR и компьютерного зрения
- [[./deepseek_ocr.md]] - Другая современная OCR-модель с похожими возможностями
- [[../computer_vision/index.md]] - Компьютерное зрение
- [[../machine_learning.md]] - Машинное обучение, на котором основана технология