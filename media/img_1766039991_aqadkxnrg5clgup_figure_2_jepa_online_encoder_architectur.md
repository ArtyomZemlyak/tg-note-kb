# Image Description

**File:** img_1766039991_aqadkxnrg5clgup_figure_2_jepa_online_encoder_architectur.jpg
**Original:** image.jpg
**Received:** 1766039991

## Extracted Text (OCR)

Figure 2: JEPA online encoder architecture. Input waveform passes through an initial Conv1D layer followed by 5 encoder blocks, each containing Conv1D with stride, SnakeBeta activation, residual blocks, and Gaussian Adaptive Attention gating. Features are projected through a bottleneck Conv1D layer and processed by 8 Conformer blocks (each with FNN, multi-head attention with 16 heads, depthwise convolution, and a second F-NN) to produce the final representation z. The target encoder shares this architecture but is updated via exponential moving average rather than backpropagation.

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766039991_aqadkxnrg5clgup_figure_2_jepa_online_encoder_architectur.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
