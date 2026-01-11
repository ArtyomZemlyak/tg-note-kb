# Image Description

**File:** img_1768120672_aqadwbjrg9i88up_principles_tor_agentic_system_design.jpg
**Original:** image.jpg
**Received:** 1768120672

## Extracted Text (OCR)

## Principles tor Agentic System Design

- e Compressors can be scaled at a sublinear computational cost. Since larger models are more informationefficient (omit fewer tokens with higher information-density), FLOPs-per-generation scale sublinearly as a function ot model size.
- e "Front-load" compute into local compressors to reduce remote costs. Scaling compressors is more effective than scaling predictors. By running larger compressors on-device, we can reduce predictor serving costs in the cloud.
- Optimize for information density. The mutual information between an input context and an agent output is a task-agnostic indicator of compression quality and is tightly linked to downstream performance and perplexity.
- Expect model family to differ in scaling trends. Choice of compressor and predictor model family yields offsets in rate-distortion curves and scaling effects. QQWEN-2.5 compressors scale more compute-efficiently than LLAMA and GEMMA-3. QWEN-2.5 predictors yield higher accuracies than LLAMA.

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768120672_aqadwbjrg9i88up_principles_tor_agentic_system_design.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
