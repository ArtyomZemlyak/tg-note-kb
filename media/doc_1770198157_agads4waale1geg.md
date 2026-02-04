# Image Description

**File:** doc_1770198157_agads4waale1geg.pdf
**Original:** Spurious Rewards Paradox-3.pdf
**Received:** 1770198157

## Extracted Text (OCR)

## Spurious Rewards Paradox

Или почему RL не работает из-за memorization shortcuts

## Проблема

Reinforcement Learning for Reasoning in Large

## Language Models with One Training Example Reinforcing General Reasoning without Verifiers

idee! |“ №
Yiping Wang’ Qing Yang’ = Zhiyuan Zeng’  LiliangRen” \_—\_Liyuan Liu” Xiangxin Zhou*2", Zichen Liu*'*, Anya Sims*'°, Haonan Wang'*, Tianyu Pang’,

Chongxuan Li', Liang Wang-', Min Lin', Chao Du"' Baolin Peng' § HaoCheng*® $$ Xuehai Не! Kuan Wang' \_Jianfeng Gao* "Sea AI Lab, Singapore; University of Chinese Academy of Sciences; Weizhu Chen' — Shuohang Wang' ' — Simon Shaolei Du' "Institute of Automation, Chinese Academy of Sciences; niversity of Singapore; ' University of Oxford; "Renmin University of China ni998@gmail.com; iliuzc, tianyupang, linmin, duchao}@sea.com

## ity of Washington |” University of Southern Califor Qn yrigus Rewards: Rethinking Training Signals in RLVR

ту ог Са быта бага Стих Oe me

Rulin Shao'* Shuyue Stella Li'* RuiXin'* ScottGeng'* Yiping Wang' Sewoong Oh' SimonShaoleiDu' Nathan Lambert" Sewon Min' Ranjay Krishna'~ Yulia Tsvetkov' Hannaneh Hajishirzi'~ Pang Wei Koh'* Luke Zettlemoyer'

'University of Washington ~&lt;Allen Institute for Artificial Intelligence *University of California, Berkeley irulins,stelli,rx3i,sgeng}@cs.washington.edu

<!-- image -->

‘University of California, Santa Cruz °Georgia Institute «

Can Large Reasoning Models Self- lrain?

Sheikh Shafayat'* Fahim Tajwar-" Ruslan Salakhutdinov* Jeff Schneider~ Andrea Zanette-

' Independent Researcher * Carnegie Mellon University

The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning

## Проблема

## -Spurious Rewards:

- -Учим Qwen-2.5 на GT - получаем прирост
- -Учим Qwen-2.5 на Majority Vote из N роллаутов получаем прирост
- -Учим Qwen-2.5 на 1 примере - получаем прирост (?!)
- -Учим Qwen-2.5 только с учётом формата - получаем прирост (?!!)
- -Учим Qwen-2.5 на некорректных лейблах - получаем прирост (?!!!)
- -Учим Qwen-2.5 на рандомных ревардах - получаем прирост (?!!!!!!!!!!!!!!!!!!)
- -Учим Llama-3.1 или OLMo-2 со spurious rewards, прироста не получаем

Spurious Rewards: Rethinking Training Signals in RLY

'Scott Geng'*

Yiping Wang' Yulia Tsvetkov' Hannaneh Hajishirzi'* Pang Wei Koh'- Luke Zettlemoyer' 'University of Washington ~Allen Institute for Artificial Intelligence "University of California, Berkeley С} GitHub Repo

## Abstract

strong mathematical reasoning in certain models even with spurious rewards that have БШ. no, or even negative correlation with the correct answer. For exampic, RLVR improves МАЛ Н-200 performance for Qwen2.5-Math-/8 in absojute pomnts by 21.4% (random reward), 13.8% (format reward), 24.1% (incorrect label), 26.0% (1-shot RL), and 27.1% (majonty voting)-——nearly matching the 29.1% gained with ground truth rewards. However, the spurious rewards thal work for Qwen often fail to yield gains with other mode! families like Llama or OLMo2. In particular, we find code reasoning—thinking in code without actual code cxecution-—to be a distinctive Qwen2.5-Math behavior that becomes signilicantly more frequent after RLVR, from 65% to over 90%, even with spurious rewards. Overall, we hypothesize that, given the lack of useful reward signal, RLVR must somchow be surfacing useful reasoning representations learned during pretraining, although the cxact mechanism remains a topic for future work. We suggest thal future RLV K research should possibly be validated on diverse models rather than a single de facto choice, as we show thal if is casy to get performance gains on Qwen modcls even with compictely spurious reward signals.

<!-- image -->

-S00 accuracy after 500 steps of КГУ К on vanous training signals. We show that even "spunous rewards (c.g., rewarding incorrect labels or with compictcly random rewards) can yield strong MATH-500 gains on Qwen models. Notably, these reward signals do not work for other models like Liamas.1-55-instruct and OLMol-/5, which have dificrent reasoning priors.

## Почему так?

## Два варианта:

- -Либо Qwen-2.5 так необычно заоверфитился на бенчи (да)
- -Либо авторы работ криво отрепортили метрики бейзлайна бейзлайн (тоже да, но синенькое)

<!-- image -->

## Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs

Lecheng Yan"! Ruizhe 14° Guanhua Chen! Qing Li’ Jiahui Geng’ Wenxi Li* Vincent Wang! Chris Lee’

<!-- image -->

## Пререквизиты: Path Patching

## -Делаем 4 форварда:

- -Форвард со входом x\_n, кешируем активации a\_n
- -Форвард с пертурбированным входом x\_p, кешируем активации a\_p
- -Форвард со входом x\_n, но изменяем часть активаций a\_n на a\_p, сохраняем активации a\_p', логиты l\_p
- -Форвард со входом x\_n, заменяем активации a\_n на a\_p', кешируем логиты l\_p'
- -Сравниваем l\_p, l\_p' - по разнице между логитами определяем зависимость выхода от пертурбированного входа

Figure 1: Path patching methodology. Left: [here are four forward passes: (1,2) Run model on baseline and perturbed inputs and cache activations. (3) lo measure the effect of an upstream sender component (5) on a downstream receiver component (X), run the model on the baseline input, patch in 5, freeze all other components, and cache the activation of K. (4) Кип the model on the baseline input and patch in К. Right: Alternative visualization of step (3) using the residual stream. By allowing only the downstream receiver К to be recomputed when the sender 5 is patched, we effectively isolate the direct path from 5 to В, while preserving all other paths to К as they were in the baseline run.

<!-- image -->

## Пререквизиты: Logit Lens

- -Накладываем LM Head на хиддены не с последнего слоя
- -Смотрим, какие логиты получаются

model's top token and Its logit

<!-- image -->

## Пререквизиты: Neural ODEs

- -Нейросеть состоит из дискретных слоёв h\_1 -&gt; h\_2 -&gt; … -&gt; h\_n
- -То есть, h\_{t+1} = h\_t + f(h\_t, \theta)
- -Это метод Эйлера с шагом 1
- -Ну раз так, то это эквивалентно диффуру dh/dt = f(h, t, θ)

Figure 1: Рей; A Residual network defines a discrete sequence of finite transformations. Right: A ODE network defines a vector held, which continuously transforms the state. Both: Circles represent evaluation locations.

<!-- image -->

## Эксперименты

- -Модели: Qwen-2.5-Math-7B + Qwen-2.5-Math-7B-Spurious
- -Проливаем датасеты через модели, выявляем контаминацию
- -Partial Prompt Evaluation: даём часть промпта, смотрим, как продолжит (привет, gpt-oss и MMLU)
- -Смотрим на метрики до и после Spurious RL
- -LiveMathBench норм, MATH-500 и MinervaMath контаминированные

<!-- image -->

Figure I. Left: Overall accuracy of four models on six benchmarks. Right: Dataset-selection rationale. Based on the accuracy gap, we retain MAI H500, MinervaMath and LiveMathBench as our principal evaluation suites. Questions that are wrong before RLVR but correct after are treated as leaked and are the focus of subsequent mechanistic tests.

<!-- image -->

## Эксперименты

- -Смотрим на перплексию ответов и полного промпта во время Spurious RL
- -На Qwen-2.5-Math-7B перплексия ответов падает, перплексия обычного текста растёт
- -На Llama-3.1-8B и OLMo-2-1124-7B перплексия падает и там и там
- -Вывод: Spurious RL уменьшает качество language modeling у модели (но повышает метрики из-за вспоминания контаминированного датасета)

Figure 3. Perplexity Analysis With Accuracy. Full-text (top) and answer-only (bottom) perplexity heatmaps. Heatmaps display full-text and answer-only perplexity across checkpoints (step 0, 50, 100, 150) under spurious RLVR with incorrect rewards. Percentage annotations under each block show base model accuracy and accuracy improvement after RL training.

<!-- image -->

Figure 4. The Perplexity Paradox. While answer-only perplexity decreases (orange), full-text perplexity increases (blue), suggesting a trade-off between memorization and general language modeling capability.

<!-- image -->

## Эксперименты

- -Path Patching активациями базовой модели активациями из модели после Spurious RL
- -Если патчить MLP, а не аттеншн, качество становится выше - значит, знания хранятся в MLP
- -18-20 слои имеют пик восстановления качества
- -У LLaMA качество почти не меняется
- -Это - Functional Anchor слои, где модель делает выбор в пользу вспоминания ответа (memorization) вместо ризонинга (generalization)

(a) Qwen2.5-Math-7B (b) LLaMA-3.1-8B

<!-- image -->

<!-- image -->

Figure 5. Path Patching Accuracy Recovery Comparison. Left: Qwen exhibits a sustained peak at L18—L20 (marking the final injection of the correct answer) followed by a sudden drop at L21 (revealing a critical feature space divergence). Right: LLaMA shows no comparable recovery pattern and maintained extremely low recovery rates, confirming the absence of this memorization mechanism in the control model.

## Эксперименты

- -Накладывают Logit Lens на модель и считают JSD от Logit Lens с финальными логитами модели
- -Если JSD высокий, модель уже приняла решение по поводу выбранного токена, последующие слои бездельничают
- -Если JSD низкий, модель не знает, как будет отвечать, последующие слои не бездельничают
- -В Qwen есть чёткие слои во второй половине (L21-L22), где JSD максимальный, а потом он уменьшается
- -В Llama увеличение JSD монотонное
- -Вывод: слои 21-22 в Qwen - Structural Adapters, поворачивающие пространство активаций в сторону заученных ответов

Figure 6. Layer-wise MLP Sub-component JSD Scores. (a) In Qwen, JSD for Wup and W gate peaks around Layer 21 and subsequently declines, identifying this depth as the locus of тах!mal parametric change. (b) In LLaMA, all components exhibit a monotonic increase, lacking the structural adaptation signature.

<!-- image -->

## Эксперименты

- -Взяли заликаный вопрос из MATH, собрали Logit Lens двух траекторий
- -Траектория с верным ответом (4) - 23 слой (после ключевого по JSD L22) вставляет верный ответ
- -Траектория с неверным ответом (3) - 23 слой всё ещё вставляет верный ответ, но с меньшей вероятностью - и последующие слои пытаются зафорсить верный ответ, но менее активно
- -Вывод: 21-23 слои хранят в себе знания о верном ответе, добавлений с последних слоёв не хватает, чтобы изменить решение модели

(b) Failed Retrieval Trajectory (Output: Wrong Answer 3")

<!-- image -->

Figure 7. Logit Lens Analysis. (Top) In successful case, the Functional Anchor (L19) primes the stream, and after structural adaptation (L21-22), the MLP at L23 successfully injects the correct answer "4". (Bottom) In the failure case, despite the МЕР still attempting to ~ at L23-25 (visible in heatmap), the weaker initial signal from the Anchor allows the residual stream to drift towards the incorrect token "3°. [his confirms that MLPs store the memory, and will continue to output memories even in the presence of interference.

## Эксперименты

- -Если представить модель как Neural ODE, можно увидеть, что:
- -В первых слоях траектория PCA активаций у заликаных и не заликаных семплов пересекается
- -В середине и в конце - сильно отличается
- -Если посчитать разницу (separation force), то пик будет на слоях 18-20, где мы обнаружили Functional Anchor

Figure 5. Latent Space lLrajectory (PCA Projection). The average trajectories of Leakage (red) and Generalization (blue) samples bifurcate significantly after the middle layers.

<!-- image -->

Figure 10. NDE Dynamics Metrics. Left: Separation Force peaks at L18—L20, identifying the causal origin of trajectory divergence. Right: Velocity Difference increases in later layers, reflecting signal amplification by the Structural Adapter layers.

<!-- image -->

## Эксперименты

- -Пробуют подкладывать в Spuriously trained модель слои из базовой модели
- -Меняют как Functional Anchor, так и Structural Adapter
- -На не заликаных семплах резет почти не роняет качество, на заликаных качество проседает очень сильно
- -Для феномена Spurious RLVR важны оба вида слоёв - дроп только одного просаживает качество слишком сильно

MATH-500 (Leakage)

MinervaMath (Leakage)

98.0%

<!-- image -->

<!-- image -->

- (a) Overall accuracy on leakage samples across ablation conditions. (6b) Overall accuracy on stable samples. Performance remains Anchor reset and Adapter reset cause moderate drops. stable under reset conditions.

Figure 9. Ablation study results. Leakage samples from contaminated datasets exhibit higher sensitivity to layer manipulation than stable samples. The leakage-free LiveMathBench shows a different pattern, which are provided in Appendix E.

## Эксперименты

- -Пробуют стирить активации нейронов в Functional Anchor и в Structural Adapter
- -На не заликанном датасете разницы почти нет
- -На заликаном датасете стиринг на 18 слое (Functional Anchor) показывает наибольшую чувствительность
- -Вывод: активируются только те circuts, которые отвечают за вспоминание ответов из контаминированных данных
- -Можно подавлять меморизацию

## Accuracy Delta vs В:

Accuracy Delta vs Baseline - Leakage Datasets Results line - Full Datasets Results

## {MATH-500, MinervaMath) (LiveMathBench)

<!-- image -->

(a) Leakage Dataset (b) Leakage-free Dataset

Figure 13. Dataset-Level Steering: Accuracy Change. (Left) On the leakage datasets, Layer 18 exhibits maximal sensitivity -4%). (Right) On the leakage-free dataset, steering produces no systematic pattern, confirming that the intervention specifically targets contamination-dependent circuits rather than general reasoning pathways.

<!-- image -->

## Эксперименты

## -Всё воспроизводится на Qwen3!

Figure 235. Logit Lens Analysis for Qwen5-5B. Consistent with Qwen2.5-Math-/B, Qwen5-3B exhibits a single decisive peak-valley-rise trajectory in successful retrieval (Left), while failed cases display oscillatory mult signature indicates successful memorization activation.

<!-- image -->

Path Patching: Accuracy Recovery by Layer

730) += MLP Patching

(a) OLMo-2-1124-7B (b) Qwen3-3B

<!-- image -->

Figure 19. Path Patching Recovery for Additional Models. (a) Consistent with LLaMA, OLMo does not display the middle-layer Signal injection pattern observed in Qwen2.5-Math-/B. (6) Similarly, Qwen3-8B has a weaker contamination effects compared to Owen2.5-Math-/bB.

Аи] JO SSO[PILGII DOUBULIOJ.IOd [OAD] MO] Р 18 UIBUIS Я 1-57] [-Z7-OIN TO PUB 98-Г5-УретТ7Т ЭП "SAT snounds Jopun JUSWISAOICUI пещер руе АЕ JUTTOSEG YSIY SMOYS FR-CUIMA) "S}ISEJEG PUB эро! SsO1Dy UOSLIEdUIO,) AJBINIY "C] ans1]

<!-- image -->

Figure 20. Layer-wise МЕР Sub-component JSD Scores for Additional Models. (a) OLMo exhibits monotonic increase acros: all components, consistent with non-contaminated control models. (b) Qwen3-38B replicates the peak-and-decline pattern at Layer 35, confirming the generalizability of the Structural Adapter mechanism within the Qwen architecture family.

<!-- image -->

## Выводы

- -Qwen - заликанные модели, эксперименты с RL на них не ставим
- -OLMo 2 -  не заликанные модели, эксперименты с RL на них ставим
- -Показатель здоровья RL - prompt и answer perplexity: если перплексия промпта растёт, а ответа падает, то мы ломаем модель, а не учим
- -Partial Prompt Evaluation - для поиска случайных ликов
- -Steering в functional anchor layers позволяет избежать memorization shortcuts без перезаварки

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/doc_1770198157_agads4waale1geg.pdf) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
