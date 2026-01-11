# Image Description

**File:** img_1768119833_aqadxwtrg0pniep_image_figure_4.jpg
**Original:** image.jpg
**Received:** 1768119833

## Extracted Text (OCR)

<!-- image -->

Figure 4 | Relative difference in train loss (left) and validation loss (right) between models trained with NVFP4 and BF16, shown at two model scales: Nemotron 3 Nano (A3B) and the larger MoE model (A&amp;B). Loss gaps decrease as model size increases (A3B — АЗВ). Recipe ablation on Nemotron 3 Nano started from Nemotron 3 NVFEP4 checkpoint at 500B tokens, then quantizes sensitive layers (Mamba Output, QKV, and Attention projections) to NVFP4, highlighting the importance of keeping these layers in high precision.

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768119833_aqadxwtrg0pniep_image_figure_4.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
