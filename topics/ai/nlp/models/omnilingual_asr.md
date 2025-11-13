# Omnilingual ASR: Многоязычная система распознавания речи от Meta

## Краткое описание

Omnilingual ASR — это открытая система распознавания речи (Automatic Speech Recognition), разработанная Meta, поддерживающая более 1600 языков. Модель масштабирована до 7B параметров на базе архитектуры wav2vec 2.0 и представлена в различных размерах: от 300M (для мобильных устройств) до 7B параметров. Модель превосходит Whisper по метрике CER (Character Error Rate) и обеспечивает сопоставимое качество WER (Word Error Rate) с лучшей поддержкой языков.

## Основная информация

### Архитектура и подход

- **Базовая модель**: wav2vec 2.0, масштабированная до 7B параметров
- **Варианты декодера**: традиционный CTC и трансформер
- **Подход с использованием LLM**: in-context learning — можно дать несколько примеров аудио-текст пар и получить рабочее качество транскрипции без тренировки
- **Модель предоставлена в разных размерах**: от 300M до 7B параметров для различных сценариев использования

### Основные характеристики

- **Поддержка языков**: более 1600 языков
- **Character Error Rate (CER)**: ниже 10% для 78% языков
- **Состояние-искусства (state-of-the-art)**: качество на всех 1,600+ языках
- **Гибкость**: можно добавить новый язык на лету без переобучения

### Практические особенности

- **Все под Apache 2.0 и CC-BY лицензиями**: можно применять для чего угодно
- **Omnilingual ASR Corpus**: крупнейший датасет спонтанной речи на 350 низкоресурсных языках объёмом 1 ТБ
- **Сотрудничество с локальными организациями**: работали с локальными организациями по всему миру, нанимали носителей языков из удалённых регионов
- **Партнёрство**: с Mozilla Common Voice, Lanfrica/NaijaVoices и другими

## Результаты и достижения

Согласно [официальной статье Meta](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/), модель демонстрирует:

- CER<10% для 78% языков (CER почти всегда ниже WER)
- WER сравнимый с Whisper, но с лучшей поддержкой языков
- Превосходное покрытие языков, включая низкоресурсные

![Сравнение с Whisper и результаты по языкам](../../../../images/img_1763034818_AgACAgIA.jpg)

**Описание изображения:** Таблица сравнения Omnilingual ASR с Whisper v3, включая его большие (1.5B), средние (769M) и малые (244M) варианты. Для каждого бенчмарка указывается средний CER по языкам на разделах dev и test. Сравнение учитывает только языки, которые охватывает Whisper в каждом бенчмарке, а число после названия набора данных указывает количество рассматриваемых языков. Два самых правых столбца показывают процент побед нашей модели против Whisper large v3 на тестовом наборе FLEURS: n = 81 учитывает все 81 языка FLEURS, в то время как n = 34 учитывает только 50 наиболее распространенных языков мира, охватываемых FLEURS (34 из них).

## Применение и доступ

- **GitHub репозиторий**: https://github.com/facebookresearch/omnilingual-asr
- **Демонстрация**: https://aidemos.atmeta.com/omnilingualasr/language-globe
- **Песочница Hugging Face**: https://huggingface.co/spaces/facebook/omniasr-transcriptions
- **Датасет для обучения**: https://huggingface.co/datasets/facebook/omnilingual-asr-corpus

## Связи с другими темами

- [[speech_recognition.md]] - Общие принципы распознавания речи
- [[speech_synthesis.md]] - Синтез речи (обратная задача)
- [[speech_recognition_dialects.md]] - Распознавание речи с учётом диалектов, особенно актуальное для 1600+ языков
- [[wav2vec.md]] - Базовая архитектура, на которой основана модель
- [[whisper.md]] - Сравниваемая модель, на которую ссылается Omnilingual ASR

## Источники

1. [Omnilingual ASR: Open-Source Multilingual Speech Recognition for 1600+ Languages](https://github.com/facebookresearch/omnilingual-asr) - Основной репозиторий проекта на GitHub с исходным кодом и документацией
2. [Omnilingual ASR Corpus](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus) - Крупнейший датасет спонтанной речи на 350 низкоресурсных языках объемом 1 ТБ
3. [Meta AI Research Publication: Omnilingual ASR](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/) - Официальная статья от команды Meta AI Research о разработке Omnilingual ASR
4. [Meta AI Blog: Omnilingual ASR](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/) - Блог-пост от Meta AI с объяснением ключевых аспектов разработки
5. [AI VK Summary of Omnilingual ASR](https://t.me/langotime) - Обзор статьи подготовлен командой AI VK, содержащий ключевые моменты исследования