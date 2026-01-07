# Ошибка tesserocr в Docling: TESSDATA_PREFIX конфигурация

## Описание проблемы

Ошибка `convert_document_into_docling_document: Unexpected error: tesserocr is not correctly configured. No language models have been detected. Please ensure that the TESSDATA_PREFIX envvar points to tesseract languages dir` возникает при использовании библиотеки Docling для обработки документов с включенным OCR. Эта проблема указывает на то, что библиотека `tesserocr` не может найти языковые модели Tesseract, необходимые для выполнения OCR-операций.

## Причины возникновения

1. **Отсутствие переменной окружения TESSDATA_PREFIX**: Библиотека `tesserocr` ожидает, что переменная `TESSDATA_PREFIX` будет указывать на директорию с языковыми моделями Tesseract
2. **Неправильный путь к языковым моделям**: Переменная `TESSDATA_PREFIX` может быть установлена, но указывать на неправильную директорию
3. **Отсутствие языковых моделей**: В директории TESSDATA_PREFIX могут отсутствовать языковые модели (например, `eng.traineddata` для английского языка)
4. **Неправильная установка Tesseract**: Tesseract OCR может быть установлен некорректно или без необходимых языковых моделей
5. **Несовместимость версий**: Используется несовместимая версия `tesserocr` с установленным `tesseract`

## Решение проблемы

Для исправления этой ошибки, следуйте этим шагам:

1. **Установите Tesseract с языковыми моделями**:
   ```bash
   # Для Ubuntu/Debian:
   sudo apt-get install tesseract-ocr
   sudo apt-get install tesseract-ocr-eng # английская модель
   sudo apt-get install tesseract-ocr-rus # русская модель (и другие по необходимости)
   
   # Для macOS:
   brew install tesseract-lang
   
   # Для Windows:
   # Установите Tesseract с официального сайта и убедитесь, что языковые модели установлены
   ```

2. **Определите директорию с языковыми моделями**:
   ```bash
   # Найдите директорию с языковыми моделями
   tesseract --list-langs
   
   # Обычно пути могут быть:
   # Linux: /usr/share/tesseract-ocr/4.00/tessdata или /usr/share/tessdata
   # macOS: /usr/local/share/tessdata или /opt/homebrew/share/tessdata
   # Windows: C:\Program Files\Tesseract-OCR\tessdata
   ```

3. **Установите переменную окружения TESSDATA_PREFIX**:
   ```bash
   # В терминале (Linux/macOS):
   export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata
   # или
   export TESSDATA_PREFIX=/usr/share/tessdata
   
   # В Python-скрипте:
   import os
   os.environ['TESSDATA_PREFIX'] = '/path/to/tessdata/directory'
   
   # В файле .env:
   TESSDATA_PREFIX=/path/to/tessdata/directory
   ```

4. **Альтернативное решение - использовать pytesseract вместо tesserocr**:
   ```python
   from docling.datamodel.document import DocumentConversionInput, OCRConfig
   from docling.datamodel.pipeline_options import OcrOptions
   
   # Используйте pytesseract как альтернативу
   config = OCRConfig( # настройка для OCR
       do_ocr=True,
       # Укажите параметры OCR, которые поддерживает текущая версия
   )
   ```

5. **Установка языковых моделей вручную**:
   - Скачайте необходимые `.traineddata` файлы из [официального репозитория](https://github.com/tesseract-ocr/tessdata)
   - Поместите их в директорию, указанную в `TESSDATA_PREFIX`

## Пример фикса

Вместо запуска Docling без правильной конфигурации:

```python
# Это может вызвать ошибку
from docling.pipeline.simple_pipeline import SimplePipeline

try:
    # Это может привести к ошибке tesserocr
    pipeline = SimplePipeline()
except Exception as e:
    print(f"Ошибка: {e}")
```

Используйте правильную конфигурацию:

```python
import os

# Установите переменную окружения до импорта библиотек
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'  # адаптируйте под вашу систему

from docling.pipeline.simple_pipeline import SimplePipeline
from docling.datamodel.document import DocumentConversionInput, OCRConfig

# Теперь можно использовать Docling с OCR
try:
    pipeline = SimplePipeline()
    # Дальнейшие операции с конвертацией документов
except Exception as e:
    print(f"Произошла ошибка: {e}")
```

## Дополнительные проверки

1. **Проверьте установку tesserocr**:
   ```python
   import tesserocr
   print(tesserocr.tesseract_version())  # Проверит версию tesseract
   print(tesserocr.get_languages())      # Проверит доступные языки
   ```

2. **Проверьте переменные окружения в Python**:
   ```python
   import os
   print(f"TESSDATA_PREFIX: {os.environ.get('TESSDATA_PREFIX', 'Не установлено')}")
   ```

## Связь с другими темами

- [[docling.md]] - Общая информация о библиотеке Docling
- [[docling_error_ocrconfig.md]] - Описание других ошибок с OCRConfig
- [[docling_error_tesseract_psm.md]] - Другие ошибки, связанные с Tesseract OCR в Docling
- [[../ocr/chandra_ocr.md]] - Современные альтернативы OCR
- [[../ocr/deepseek_ocr.md]] - Другие решения для OCR

## Источники

1. [Официальный репозиторий Docling на GitHub](https://github.com/DS4SD/docling) - основной репозиторий библиотеки Docling, где можно найти актуальную документацию и примеры использования
2. [Документация tesserocr](https://pypi.org/project/tesserocr/) - официальная документация Python-обертки для Tesseract OCR
3. [Официальный сайт Tesseract OCR](https://tesseract-ocr.github.io/) - главный ресурс по Tesseract OCR, включая установку и настройку
4. [Репозиторий tessdata на GitHub](https://github.com/tesseract-ocr/tessdata) - репозиторий с языковыми моделями для Tesseract
5. [Документация Docling](https://ds4sd.github.io/docling/) - официальная документация библиотеки с описанием API и примерами