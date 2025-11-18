# Image Description

**File:** img_1763477492_aqadkg1rgwyk6uh_souper_model_how_simple_arithmetic_unloc.jpg
**Original:** image.jpg
**Received:** 1763477492

## Extracted Text (OCR)

## Souper-Model: How Simple Arithmetic Unlocks State-of-the-Art LLM Performance

Shalini Maiti!"', Amar Budhiraja*', Bhavul Gauri', Gaurav Chaurasia'. Anton Protopopov'. Alexis Audran-Reiss~-, Michael Slater-, Despoina Magka-,. Tatiana Shavrina-, Roberta Raileanu-:'*. Yoram Bachrach-

"Мега SuperIntelligence Labs, “FAIR at Meta, ’ University College London

'Equal contribution, “Work done while working at Meta

Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse domains, but their training remains resource- and time-intensive, requiring massive compute power and careful orchestration of training procedures. Model souping—the practice of averaging weights from multiple models of the same architecture—has emerged as a promising pre- and post-training technique that can enhance performance without expensive retraining.

In this paper, we introduce Soup Of Category Experts (SoCE), a principled approach for model souping that utilizes benchmark composition to identify optimal model candidates and applies non-uniform weighted averaging to maximize performance. Contrary to previous uniform-averaging approaches, our method leverages the observation that benchmark categories often exhibit low inter-correlations in model performance. SoCE identifies "expert" models for each weakly-correlated category cluster and combines them using optimized weighted averaging rather than uniform weights. We demonstrate that the proposed method improves pertormance and robustness across multiple domains, including multilingual capabilities, tool calling, and math and achieves state-of-the-art results on the Berkeley Function Calling Leaderboard.

Wate: November 1%. 2025

Correspondence: Shalini Maiti at shalinimaitiG@meta.com, Amar Budhiraja at amarbudhiraja@meta.com

Code: https: //github. com/facebookresearch/11m\_souping

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1763477492_aqadkg1rgwyk6uh_souper_model_how_simple_arithmetic_unloc.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
