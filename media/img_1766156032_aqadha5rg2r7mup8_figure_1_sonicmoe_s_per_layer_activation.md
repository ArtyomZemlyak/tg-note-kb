# Image Description

**File:** img_1766156032_aqadha5rg2r7mup8_figure_1_sonicmoe_s_per_layer_activation.jpg
**Original:** image.jpg
**Received:** 1766156032

## Extracted Text (OCR)

Figure 1: SonicMoE's per-layer activation memory footprint (left) stays constant even when expert granularity (d/n where d is the embedding dimension and 7 1$ the expert intermediate dimension) increases, and 1$ 0.20-1.59x more memory-efficient than other baselines. SonicMoE's forward computation throughput (right) reaches an average of 88% (max 91%, min 66%) of the upper bound (cuBLAS BMM + activation + cuBLAS BMM + aggregation on Н100). Note that the cuBLAS upper bound baseline does not include the router computation. Here we use а ЗОВ MoE configuration with microbatch size of 32/768 tokens, and we vary the activated experts / total number of experts as 2/32, 4/64, 8/128, and 16/256 from left to right.

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766156032_aqadha5rg2r7mup8_figure_1_sonicmoe_s_per_layer_activation.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
