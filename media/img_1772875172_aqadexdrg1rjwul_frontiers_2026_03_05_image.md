# Image Description

**File:** img_1772875172_aqadexdrg1rjwul_frontiers_2026_03_05_image.jpg
**Original:** image.jpg
**Received:** 1772875172

## Extracted Text (OCR)

—- А Frontiers 2026-03-05

<!-- image -->

## Phi-4-reasoning-vision-15B Technical Report

Jyoti Aneja, Michael Harrison, Neel Joshi, Tyler LaBonte, John Langford, Eduardo Salinas

<!-- image -->

<!-- image -->

5 https: / /aka.ms/ Phi-4-reasoning-vision ©) https: / /huggingface.co /microsoft/ Phi-4-reasoning-vision-15B Г https: / /aka.ms/Phi-4-r-v-FoundryLabs # https:/ / github.com/ microsoft / Phi-4-reasoning-vision-15B

<!-- image -->

<!-- image -->

We present Phi-4-reasoning-vision-15B, a compact open-weight multimodal reasoning model, and share the motivations, design choices, experiments, and learnings that informed its development. Our goal is to contribute practical insight to the research community on building smaller, efficient multimodal reasoning models and to share the result of these learnings as an open-weight model that is good at common vision and language tasks and excels at scientific and mathematical reasoning and understanding user interfaces. Our contributions include demonstrating that careful architecture choices and rigorous data curation enable smaller, open-weight multimodal models to achieve competitive performance with significantly less training and inference-time compute and tokens. The most substantial improvements come from systematic filtering, error correction, and synthetic augmentation—reinforcing that data quality remains the primary lever for model performance. Systematic ablations show that high-resolution, dynamic-resolution encoders yield consistent improvements, as accurate perception is a prerequisite for high-quality reasoning. Finally, a hybrid mix of reasoning and non-reasoning data with explicit mode tokens allows a single model to deliver fast direct answers for simpler tasks and chain-of-thought reasoning for complex problems.

## 1 Introduction

Phi-4-reasoning-vision-15B is a compact open-weight multimodal reasoning model that balances reasoning power, efficiency, and training data needs. It is a broadly capable model that allows for natural interaction for a wide array of vision-language tasks and excels at math and science reasoning and understanding user interfaces, as shown in Figure 1. Beyond these general capabilities, our model presents an appealing value relative to current open-weight models, pushing the Pareto frontier of the trade-off between accuracy and compute costs. We achieve competitive accuracy with much slower models that require ten times or more compute time and tokens, and better accuracy than similarly fast models, particularly when it comes to math and science reasoning, as shown in Figure 2.

In this report, we share the motivations, design choices, experiments, and learnings that informed its development, as well as an evaluation of the model's performance and guidance on how to use it. Our goal is to contribute practical insight to the community on building smaller, efficient multimodal reasoning models and to share an open-weight model that is competitive with models of similar size at general vision-language tasks, excels at computer use, and at scientific and mathematical multimodal reasoning.

## 1.1 Focus on Smaller and Faster Vision—Language Models

Many popular vision—language models (VLMs) have trended towards growing in parameter count and the number of tokens they consume and generate. 111$ leads to increased training and inference-time cost and latency, impeding their usability for downstream deployment, especially in resource-constrained or interactive settings.

A growing countertrend towards smaller models aims to boost efficiency, enabled by careful model design and data curation—a goal pioneered by the Phi (Gunasekar et al., 2023) family of models and furthered by Phi-4-reasoning-vision-15B. We specifically build on learnings from the Phi-4 (Abain et al., 2024) and Phi-4-Keasoning (Abdin et al., 2025) language models and show how a multimodal model can be trained

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1772875172_aqadexdrg1rjwul_frontiers_2026_03_05_image.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
