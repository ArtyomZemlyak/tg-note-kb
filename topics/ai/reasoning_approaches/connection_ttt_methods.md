# Связь между методами Test-Time Training

## Описание

Этот файл описывает связи между различными подходами к обучению во время инференса (Test-Time Training), включая TTT-Discover, ThetaEvolve и MiGrATe.

## Сравнение подходов

[[test_time_training_methods.md]] содержит общее описание различных методов TTT, включая:
- [[ttt_discover_learning_at_test_time.md]] - детальное описание метода TTT-Discover
- [[reinforcement_learning_for_discovery.md]] - применение RL для научных открытий

## Взаимосвязи

TTT-Discover, ThetaEvolve и MiGrATe представляют собой различные подходы к задаче обучения во время инференса:
- TTT-Discover фокусируется на энтропийной оптимизации и PUCT-повторном использовании для научных открытий
- ThetaEvolve использует эволюционные стратегии и является более близким к AlphaEvolve
- MiGrATe использует смешанные политики и GRPO для адаптации во время тестирования

## Дополнительные материалы
- [[../machine_learning/test_time_adaptation.md]]
- [[../reinforcement_learning/online_learning.md]]

## Источники
- TTT-Discover: Learning to Discover at Test Time, Mert Yuksekgonul et al., https://arxiv.org/abs/2601.16175
- ThetaEvolve: https://arxiv.org/abs/2511.23473
- MiGrATe: https://arxiv.org/abs/2508.08641