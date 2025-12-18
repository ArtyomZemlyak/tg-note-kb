# Image Description

**File:** img_1766039991_aqadkhnrg5clgup_stage_1_jepa_pretraining_image.jpg
**Original:** image.jpg
**Received:** 1766039991

## Extracted Text (OCR)

Stage 1: JEPA Pretraining

<!-- image -->

Figure 1: The input waveform is processed by three parallel pathways: (1) an online encoder (trainable. green) that processes the full audio and feeds into a predictor network (yellow) after feature-space masking with a learned mask token, (2) a target encoder (purple) updated via EMA that also processes the full audio to generate Ztarget, and (3) a masking strategy module (blue) that generates binary masks. The MSE loss is computed only on masked regions between Zpredicted ANd Ztarget (Stop-gradient), with gradients backpropagating only through the online encoder and predictor. 'The target encoder provides stable representations without receiving gradients directly |Grill et al., 2020].

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766039991_aqadkhnrg5clgup_stage_1_jepa_pretraining_image.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
