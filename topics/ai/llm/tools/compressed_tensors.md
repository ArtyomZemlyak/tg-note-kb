# Compressed Tensors

## Описание

Compressed Tensors - это расширение формата safetensors, которое предоставляет универсальный и эффективный способ хранения и управления сжатыми тензорными данными. Поддерживает различные схемы квантования и разреженности, обеспечивая унифицированный формат для обработки различных оптимизаций моделей, таких как GPTQ, AWQ, SmoothQuant, INT8, FP8, SparseGPT и другие.

## Ключевые особенности

### Универсальный формат чекпоинтов
- Поддерживает различные схемы сжатия в едином, последовательном формате
- Работает с популярными методами квантования, такими как GPTQ, SmoothQuant, и FP8
- Обеспечивает гибкость в применении различных методов сжатия

### Поддержка различных видов квантования
- Квантование только весов (например, W4A16, W8A16, WnA16)
- Квантование активаций (например, W8A8)
- Квантование KV-кеша
- Неоднородные схемы (разные слои могут быть квантованы по-разному)

### Поддержка разреженности
- Обрабатывает неструктурированные и полу-структурированные (например, 2:4) паттерны разреженности
- Позволяет эффективно хранить и использовать разреженные модели

## Технические детали

### Сохранение и загрузка сжатых тензоров
```python
from compressed_tensors import save_compressed, load_compressed, BitmaskConfig
from torch import Tensor
from typing import Dict

# Создание конфигурации сжатия
compression_config = BitmaskConfig()

tensors: Dict[str, Tensor] = {"tensor_1": Tensor(
    [[0.0, 0.0, 0.0], 
     [1.0, 1.0, 1.0]]
)}
# Сжатие тензоров и сохранение на диск
save_compressed(tensors, "model.safetensors", compression_format=compression_config.format)

# Декомпрессия тензоров
decompressed_tensors = {}
for tensor_name, tensor in load_compressed("model.safetensors", compression_config = compression_config):
    decompressed_tensors[tensor_name] = tensor
```

### Сохранение и загрузка сжатых моделей
```python
from compressed_tensors import save_compressed_model, load_compressed, BitmaskConfig
from transformers import AutoModelForCausalLM

model_name = "RedHatAI/llama2.c-stories110M-pruned50"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto")

compression_config = BitmaskConfig()

# Сохранение сжатых весов модели
save_compressed_model(model, "compressed_model.safetensors", compression_format=compression_config.format)

# Загрузка сжатых весов модели
state_dict = dict(load_compressed("compressed_model.safetensors", compression_config))
```

### Пост-обучение квантования (PTQ)
Библиотека может выполнять базовое пост-обучение квантования и сохранять квантованную модель сжатой на диске, используя функции `apply_quantization_config`, `freeze_module_quantization`, и `compress_quantized_weights`.

## Применение

Compressed Tensors используется для:
- Эффективного хранения сжатых моделей
- Оптимизации развертывания LLM
- Упрощения экспериментов с различными методами квантования
- Упрощения конвейеров развертывания моделей

## Установка

### Из PyPI:
- Стабильный релиз: `pip install compressed-tensors`
- Ночной релиз: `pip install --pre compressed-tensors`

### Из исходного кода:
```
git clone https://github.com/vllm-project/compressed-tensors
cd compressed-tensors
pip install -e .
```

## Связь с MoonShot AI

Согласно информации, MoonShot AI использовала скрипты конвертации в формат compressed-tensors для своей модели Kimi-K2-Thinking, что указывает на применение этого формата в их экосистеме сжатия и оптимизации моделей.

## Связи с другими темами

- [[moe_quant.md]] - Фреймворк для квантования MoE-моделей
- [[../model_quantization_techniques.md]] - Техники квантования моделей
- [[../architectures/mixture_of_experts.md]] - Архитектура Mixture of Experts
- [[kimi_k2_quantization.md]] - Квантизация моделей Kimi