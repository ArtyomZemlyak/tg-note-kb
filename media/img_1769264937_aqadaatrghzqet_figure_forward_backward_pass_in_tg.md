# Image Description

**File:** img_1769264937_aqadaatrghzqet_figure_forward_backward_pass_in_tg.jpg
**Original:** image.jpg
**Received:** 1769264937

## Extracted Text (OCR)

Figure |: Forward/backward pass in TG. Each sentence step produces next-token predictions and a sentence vector, which is appended to a fixed-capacity memory without detaching its computation graph (removing the oldest memory entry if full). Next-token loss gradients flow back through memory to optimize parameters that produced earlier sentence representations (see Fig. 6 for a more detailed gradient-flow view).

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1769264937_aqadaatrghzqet_figure_forward_backward_pass_in_tg.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
