# Связи между концепциями Spurious RLVR и механистической интерпретацией

## Overview

Этот файл описывает ключевые связи между концепциями, описанными в статье "Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs" (arXiv:2601.11061).

## Основные связи

### Spurious Rewards Paradox и Anchor-Adapter Circuit

[[spurious_rewards_paradox.md|Парадокс ложных наград]] ←→ [[spurious_rlvr_mechanistic_findings.md|Механистические находки по Spurious RLVR]]

**Описание связи:** Spurious Rewards Paradox описывает феномен, при котором модели показывают улучшения на бенчмарках при наличии спуральных (ложных) наград, особенно в семействе Qwen моделей. Механистические находки раскрывают внутреннюю кухню этого явления через открытие Anchor-Adapter Circuit.

### Functional Anchors и Structural Adapters

[[functional_anchors.md|Functional Anchors]] ←→ [[structural_adapters.md|Structural Adapters]]

**Описание связи:** Эти две концепции представляют собой два компонента Anchor-Adapter Circuit. Functional Anchors (слои ~18-20) принимают решение между меморизацией и рассуждением, а Structural Adapters (слои ~21+) обеспечивают трансформацию пространства активаций для реализации этого решения.

### Механистические методы

[[path_patching.md|Path Patching]] ←→ [[logit_lens.md|Logit Lens]] ←→ [[neural_ode.md|Neural ODE]] ←→ [[jensen_shannon_divergence.md|Jensen-Shannon Divergence]]

**Описание связи:** Все эти методы механистической интерпретации были использованы для идентификации и анализа Anchor-Adapter Circuit. Path Patching помог локализовать функциональные слои, Logit Lens показал эволюцию логитов по слоям, NDE математически подтвердил точку бифуркации, а JSD измерил различия между распределениями.

### Диагностика через Partial Prompt Evaluation

[[partial_prompt_evaluation.md|Partial Prompt Evaluation]] ←→ [[spurious_rewards_paradox.md|Парадокс ложных наград]]

**Описание связи:** PPE используется для идентификации контаминации данных, что является предпосылкой для проявления Spurious Rewards Paradox. Если модель может воспроизвести ответы на вопросы из тестовых наборов с частичного промпта, это указывает на то, что данные были пролиты в тренировочный сет, что позволяет модели использовать меморизацию вместо рассуждения.

### Перплексия и здоровье RL

[[spurious_rewards_paradox.md|Парадокс ложных наград]] ←→ [[perplexity_analysis.md|Анализ перплексии]]

**Описание связи:** "Perplexity Paradox" является ключевым индикатором Spurious RLVR: перплексия ответов уменьшается, но перплексия промптов увеличивается, что указывает на ухудшение общего языкового моделирования в пользу специфической меморизации ответов.

## Подтверждение универсальности

[[rlvr_layer_substitution_analysis.md|Анализ подстановки слоёв в RLVR]] ←→ [[spurious_rlvr_mechanistic_findings.md|Механистические находки по Spurious RLVR]]

**Описание связи:** Оба исследования подтверждают, что эффекты Spurious RLVR воспроизводятся на различных архитектурах, включая Qwen-3, что указывает на универсальность наблюдений, а не на артефакт конкретной модели.

## Значение для практики

Эти связи показывают, как современные методы механистической интерпретации позволяют глубоко понимать внутреннюю работу LLM и выявлять потенциальные уязвимости в процессах обучения с подкреплением.