# Riemannian Flow Matching с регуляризацией Якоби (RJF)

Riemannian Flow Matching with Jacobi Regularization (RJF) — это геометрический фреймворк для генеративного моделирования, который решает фундаментальную проблему применения стандартных диффузионных трансформеров (DiT) к пространствам признаков предобученных энкодеров (DINOv2, SigLIP). Метод был предложен Kumar и Patel (2026) как опровержение гипотезы о «бутылочном горлышке ёмкости» (capacity bottleneck), выдвинутой в работе про RAE.

## Основная проблема: Геометрическая интерференция

### Гиперсферическая топология признаков

Признаки от энкодеров типа DINOv2 и SigLIP не живут в обычном евклидовом пространстве. Из-за повсеместного использования **LayerNorm** эти признаки жёстко прибиты к гиперсфере S^{d-1} и имеют почти нулевую радиальную дисперсию.

Формально вектор признаков z можно разложить на радиальную компоненту r и угловую z_hat:

```
z ≈ sqrt(d) * z_hat
```

Это создаёт геометрию «твёрдой оболочки» (hard shell geometry), где вся семантическая информация закодирована исключительно в угловой компоненте.

### Конфликт хорды и дуги

Стандартный **Flow Matching** строит пути вероятности через **линейную интерполяцию** (евклидовы хорды):

```
x_t = (1-t)x + t*epsilon
```

На гиперсферическом многообразии прямая линия между двумя точками поверхности проходит сквозь внутренности шара — область с низкой плотностью, где пространство представлений не определено.

В результате:
- Промежуточная точка x_t проваливается внутрь сферы
- Норма схлопывается: ||x_{0.5}|| ≈ 0.7 * sqrt(d)
- Модель вынуждена «галлюцинировать» градиенты в невалидной области
- Модель тратит ёмкость на минимизацию радиальных ошибок, которых не существует в топологии данных

## Решение: RJF

### 1. Геодезическая интерполяция (SLERP)

Вместо прямой линии траектория генерации следует по **геодезической** — дуге «большого круга» на сфере. Промежуточное состояние считается через **Spherical Linear Interpolation**:

```
x_t = SLERP(x, epsilon; t)
```

Это гарантирует, что норма всегда равна 1. Целевая скорость теперь лежит в **касательной плоскости** (ортогональна вектору позиции), и сеть учится предсказывать именно этот касательный вектор.

![Geometric Trajectories on the Hypersphere](../../../../media/img_1771471984_aqadqxvrgxb2seh_figure_2_geometric_trajectories_on_the.jpg) <!-- TODO: Broken image path -->

**Изображение показывает:** Визуализация путей flow matching на многообразии S^{d-1}. Стандартный Euclidean Flow Matching строит линейные пути (оранжевые и фиолетовые хорды), которые игнорируют геометрию многообразия и проходят через низкоплотную внутренность сферы. В отличие от этого, Riemannian Flow Matching следует по геодезической (синяя кривая), гарантируя, что промежуточное состояние x_t остаётся строго на поверхности многообразия. Результирующее поле скорости u_t^M(x_t) корректно определено в касательном пространстве (розовая плоскость), естественно уважая геометрию представлений.

### 2. Регуляризация Якоби

На положительно искривленном многообразии (сфере) геодезические линии сходятся («фокусируются») при приближении к полюсам. Это значит, что ошибки скорости распространяются неравномерно:

- Ошибка рядом с шумом (t=1) приведёт к большему отклонению в данных (t=0)
- Ошибка, допущенная позже (ближе к t=0), имеет меньший эффект

Для компенсации вводится весовой терм **lambda**, основанный на полях Якоби:

```
lambda(t, Omega) = sinc^2((1-t)*Omega)
```

Этот терм работает как **геометрически-осознанное внимание**:
- **Понижает вес** ошибок там, где фокусировка сама гасит возмущения (t=0)
- **Повышает требования** к точности там, где это критично (t=1)

### 3. Инженерная реализация

**На обучении:**
- Модель предсказывает вектор
- Проецирует его на касательную плоскость
- Считает взвешенный по Якоби MSE относительно теоретической касательной скорости

**На инференсе:**
Простого эйлерова шага (x + v*dt) недостаточно — касательный вектор мгновенно увёл бы состояние с поверхности сферы. Вместо этого используют **Геодезический Интегратор (Exponential Map)**. Обновление происходит через вращение:

```
x_new = cos(||v||*dt) * x + sin(||v||*dt) * (v/||v||)
```

Это закрытое решение гарантирует, что сэмплирование никогда не дрейфует с многообразия.

## Результаты

### Опровержение capacity bottleneck

Абляции с разделением радиальных и угловых компонент лосса подтвердили гипотезу геометрической интерференции:

- При минимизации евклидового MSE узкие модели страдают от «коллапса ранга» **не из-за нехватки ёмкости**, а потому что радиальный лосс доминирует в градиентах
- Если убрать радиальный лосс, даже маленькие модели начинают сходиться
- **Бутылочным горлышком была функция потерь, а не количество параметров**

![Geometric Interference vs. Capacity](../../../../media/img_1771471984_aqadshvrgxb2seh_figure_4_geometric_interference_vs_capac.jpg) <!-- TODO: Broken image path -->

**Изображение показывает:** Сравнение обучения DiT-S моделей различной ширины на токенах DINOv2 (d=768). Верхний ряд: при минимизации Euclidean MSE узкие модели (d < 768) страдают от коллапса — Angular Loss (семантика) застревает. Нижний ряд: когда радиальный лосс игнорируется, даже узкие модели (d = 384) идеально сходятся по угловой компоненте. Это доказывает, что бутылочное горлышко — не в размерности данных, а в геометрическом конфликте функции потерь.

### Сравнение с бейзлайнами

| Метод | Модель | Параметры | FID (без guidance) | FID (с guidance) |
|-------|--------|-----------|-------------------|------------------|
| Стандартный FM | DiT-B | 131M | 24.21 (не сходится) | - |
| **RJF (предложенный)** | **DiT-B** | **131M** | **6.77** | **3.37** |
| RAE (width scaling) | DiT-B | 131M+ | требует расширения | - |

RJF позволяет стандартному DiT-B (131M параметров) достичь FID 3.37 с guidance, обходя куда более тяжеловесные бейзлайны.

![Bridging the Geometric Gap](../../../../media/img_1771471984_aqadsrvrgxb2seh9_figure_bridging_the_geometric_gap.jpg) <!-- TODO: Broken image path -->

**Изображение показывает:** RJF (Riemannian Flow Matching with Jacobi Regularization) позволяет использовать стандартные Diffusion Transformers без архитектурных модификаций типа Width Scaling. Метод достигает FID 4.95 на стандартном LightningDiT-B без guidance, значительно превосходя VAE-based DiT (FID 15.83). В отличие от этого, применение стандартного Flow Matching к признакам DINOv2-B (+DiNO) не сходится (FID 21.64) из-за Geometric Interference.

![FID comparison on ImageNet 256x256](../../../../media/img_1771471984_aqadsbvrgxb2seh9_fable_comparison_on_imagenet.jpg) <!-- TODO: Broken image path -->

**Изображение показывает:** Сравнение FID на ImageNet 256x256 без guidance для различных размеров моделей LightningDiT с REPA. RJF (Ours) последовательно превосходит Euclidean Flow Matching и REPA на всех размерах моделей: DiT-B (6.77 vs 24.2), DiT-L (4.21 vs 10.08), DiT-XL (3.62 vs 9.29).

## Сравнение с RAE

| Аспект | RAE (Zheng et al., 2025) | RJF (Kumar, Patel, 2026) |
|--------|--------------------------|--------------------------|
| **Диагноз проблемы** | Capacity bottleneck (нехватка ширины) | Geometric Interference (геометрический конфликт) |
| **Решение** | Width scaling (расширение модели) | Геометрически-корректный лосс |
| **Требования к архитектуре** | DiT_DH с широкой головой | Стандартный DiT без изменений |
| **Ключевая инновация** | DiT DH architecture | SLERP + Jacobi Regularization |
| **FID (DiT-B)** | Требует расширения | 3.37 (с guidance) |

## Ограничения метода

1. **Полагается на строгую гиперсферичность** — верно для LayerNorm-архитектур типа DINOv2/SigLIP
2. **Для других топологий потребуются изменения** — метод специфичен для сферических многообразий
3. **Инференс требует специфического интегратора** — Exponential Map отсутствует в стандартных солверах «из коробки»

## Связи с другими темами

- [[../../applications/generative_models/representation_autoencoders_rae.md]] — RAE: альтернативный подход, использующий width scaling
- [[flow_matching.md]] — базовый метод Flow Matching в евклидовом пространстве
- [[computer_vision/diffusion_transformer.md]] — Diffusion Transformers (DiT)
- [[../../ai/foundations/geometry/feature_manifolds_geometry_counting.md]] — многообразия признаков в трансформерах
- [[../../applications/computer_vision/multimodal_models.md]] — SigLIP и DINOv2 как источники гиперсферических признаков

## Источники

1. **Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders** — Amandeep Kumar, Vishal M. Patel, 2026. arXiv:2602.10099. https://arxiv.org/abs/2602.10099
   - Оригинальная статья, представляющая метод RJF
   - Код: https://github.com/amandpkr/RJF
   - Ревью: https://arxiviq.substack.com/p/learning-on-the-manifold-unlocking

2. **Diffusion Transformers with Representation Autoencoders** — Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie, 2025. arXiv:2510.11690. https://arxiv.org/abs/2510.11690
   - Предыдущая работа, выдвинувшая гипотезу capacity bottleneck
   - Проект: https://rae-dit.github.io

3. **Flow Matching for Generative Modeling** — Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le, 2022. arXiv:2210.02747. https://arxiv.org/abs/2210.02747
   - Базовая работа по Flow Matching

4. **SiT: Exploring Flow and Diffusion-based Generative Models with Scalable Interpolant Transformers** — Nanye Ma, Mark Goldstein, Michael S. Albergo, Nicholas M. Boffi, Eric Vanden-Eijnden, Saining Xie, 2024. arXiv:2401.08740. https://arxiv.org/abs/2401.08740
   - Исследование интерполянтных трансформеров для диффузии

## Дополнительные материалы

- **DINOv2**: Oquab, M., Darcet, T., Moutakanni, T., et al. (2023). DINOv2: Learning robust visual features without supervision. https://arxiv.org/abs/2304.07193
- **SigLIP**: Tschannen, M., et al. (2025). SigLIP 2: Sigmoid Loss for Language Image Pre-training. https://arxiv.org/abs/2309.15350

```metadata
category: algorithms
subcategory: diffusion_models
tags: riemannian_flow_matching, jacobi_regularization, geometric_deep_learning, generative_models, DiT, DINOv2, SigLIP, manifold_learning, SLERP, hyperbolic_geometry
```
