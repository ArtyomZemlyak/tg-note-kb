# Image Description

**File:** img_1768119833_aqadxqtrg0pniep_figure_3_standard_mok_vs.jpg
**Original:** image.jpg
**Received:** 1768119833

## Extracted Text (OCR)

Figure 3 | Standard Mok vs. LatentMoE architectures. In LatentMoE, tokens are projected from the model hidden dimension d into a smaller latent dimension # for expert routing and computation, which reduces routed parameter loads and all-to-all traffic by a factor of d/f (typically about 4х). We use this eficiency to increase both the total number of experts and the top-A active experts per token by the same factor d/f, which improves accuracy per byte while keeping overall inference cost approximately constant.

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768119833_aqadxqtrg0pniep_figure_3_standard_mok_vs.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
