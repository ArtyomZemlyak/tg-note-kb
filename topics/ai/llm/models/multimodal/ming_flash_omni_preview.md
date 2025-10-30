# Ming Flash Omni Preview: Мультимодельная ИИ-модель нового поколения

## Обзор
Ming Flash Omni Preview - это обновлённая версия модели Ming-Omni, построенная на разреженном варианте Mixture-of-Experts (MoE) архитектуры Ling-Flash-2.0 с 100 миллиардами общих параметров, из которых только 6 миллиардов активны на токен. Модель демонстрирует существенные улучшения в мультимодальном понимании и генерации.

## Архитектура
- **Разреженная MoE архитектура**: Использует 100B-A6B MoE основу (расширение Ling-Flash-2.0)
- **Двухбалансная маршрутизация**: Комбинирует дополнительную вспомогательную функцию балансировки загрузки с обновлением смещения маршрутизатора на уровне модальности для обеспечения равномерной активации экспертов и стабильного обучения по всем модальностям
- **Основана на Ling LLM**: Модель построена на архитектуре Ling LLM

## Ключевые особенности и возможности
1. **Контекстно-зависимое распознавание речи и диалектов**: Устанавливает новые рекорды State-of-the-Art на всех 12 бенчмарках ContextASR и значительно улучшает качество распознавания 15 китайских диалектов
2. **Парадигма генеративной сегментации как редактирования (Generative Segmentation-as-Editing)**: Объединяет сегментацию и редактирование в задачу генерации с сохранением семантики, достигая 0.90 на GenEval, превосходя методы без обучения с подкреплением в точном пространственном контроле
3. **Продвинутое распознавание речи**: Демонстрирует передовой результат как в контекстном ASR, так и в ASR, учитывающем диалекты
4. **Генерация изображений**: Вводит высококачественный рендеринг текста и демонстрирует значительные улучшения в согласованности сцены и сохранении идентичности при редактировании изображений
5. **Генеративная сегментация**: Возможность, которая достигает сильных результатов в отдельной сегментации и улучшает пространственный контроль в генерации изображений и согласованность редактирования

## Технические характеристики
- **Общее количество параметров**: 100 млрд
- **Активные параметры на токен**: 6 млрд
- **Тип архитектуры**: Разреженная Mixture-of-Experts (MoE)
- **Входные модальности**: Изображение, текст, видео, аудио
- **Выходные модальности**: Изображение, текст, аудио
- **Базовая модель**: Вариант Ling-Flash-2.0

## Применение
- Разговоры по видео в реальном времени
- Контекстное распознавание аудио и диалектное ASR
- Клонирование голоса
- Генерация и редактирование изображений

## Производительность
- Демонстрирует высококонкурентные результаты в различных бенчмарках модальностей по сравнению с ведущими моделями индустрии
- Показывает конкурентоспособные результаты в понимании визуального текста, генерации изображений, понимании аудио и синтезе речи

## Доступ к модели
Модель можно скачать по следующим ссылкам:
- [Hugging Face](https://huggingface.co/inclusionAI/Ming-flash-omni-Preview)
- [ModelScope](https://modelscope.cn/models/inclusionAI/Ming-flash-omni-Preview)

## Пример использования
Модель можно использовать с помощью следующего кода Python:

```python
import os
import torch
import warnings
from bisect import bisect_left
warnings.filterwarnings("ignore")

from transformers import AutoProcessor
from modeling_bailingmm2 import BailingMM2NativeForConditionalGeneration

def split_model():
    device_map = {}
    world_size = torch.cuda.device_count()
    num_layers = 32
    layer_per_gpu = num_layers // world_size
    layer_per_gpu = [i * layer_per_gpu for i in range(1, world_size + 1)]
    for i in range(num_layers):
        device_map[f'model.model.layers.{i}'] = bisect_left(layer_per_gpu, i)
    device_map['vision'] = 0
    device_map['audio'] = 0
    device_map['linear_proj'] = 0
    device_map['linear_proj_audio'] = 0
    device_map['model.model.word_embeddings.weight'] = 0
    device_map['model.model.norm.weight'] = 0
    device_map['model.lm_head.weight'] = 0
    device_map['model.model.norm'] = 0
    device_map[f'model.model.layers.{num_layers - 1}'] = 0
    return device_map

# Загрузка предварительно обученной модели
model_path = "inclusionAI/Ming-flash-omni-Preview"
model = BailingMM2NativeForConditionalGeneration.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
    device_map=split_model(),
    load_image_gen=True,
    load_talker=True,
).to(dtype=torch.bfloat16)

# Инициализация процессора
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
```

## Временная шкала релизов
- [2025.10.27] Выпущен предварительный вариант Ming-flash-omni
- [2025.07.15] Ming-lite-omni v1.5 с существенными улучшениями
- [2025.06.12] Технический отчет опубликован на arxiv
- [2025.05.28] Официальная версия Ming-lite-omni v1 выпущена
- [2025.05.04] Тестовая версия Ming-lite-omni выпущена

## Цитирование
Если вы считаете эту работу полезной, пожалуйста, сослайтесь на неё:

```
@misc{Mingomni2025,
      title  = {Ming-Omni: A Unified Multimodal Model for Perception and Generation}, 
      author = {Inclusion AI},
      year = {2025},
      eprint = {2506.09344},
      archivePrefix = {arXiv},
      url = {https://arxiv.org/abs/2506.09344}
}
```

## Связи с другими темами
- [[ming.md]] - Общая информация о проекте Ming как семействе мультимодальных моделей
- [[ming_family_evolution.md]] - Эволюция семейства моделей Ming, в контексте которой рассматривается эта флагманская модель
- [[omnivinci.md]] - Альтернативная omni-модель от NVIDIA, специализирующаяся на совместном понимании визуального, аудио и языкового контента, в отличие от Ming Flash Omni, которая имеет улучшенную архитектуру Sparse MoE и фокусируется на более точном контроле при генерации и редактировании
- [[generative_segmentation_as_editing.md]] - Подробное описание парадигмы генеративной сегментации как редактирования, используемой в модели
- [[speech_recognition_dialects.md]] - Технологии распознавания речи и диалектов, в которых модель достигла рекордных результатов

## Значение
Ming Flash Omni Preview представляет собой значительное продвижение в области мультимодального ИИ, с особыми сильными сторонами в распознавании речи, генерации изображений и возможностях генеративной сегментации.