# Image Description

**File:** img_1772263934_aqadjxvrgzoq4eh_table_2_increasing_the_loss.jpg
**Original:** image.jpg
**Received:** 1772263934

## Extracted Text (OCR)

Table 2 | Increasing the loss factor leads to improved reconstruction metrics (rFID, PSNR) at the cost of increased bitrate in the latent encoding. For small models, the loss factor (and bits in the latent) matter a lot. For larger base models the loss factor is less sensitive.

|                                   | LF | bits/pixel rFID@50k PSNR | gFID (small) gFID (medium)   |
|-----------------------------------|--------------------------------------------------------------|
| 1.3 | 0.035 0.79 25.7 | 1.42 1.3/ |                                                              |
| 15 | 0.059 0.47 27.6 | 1.54 1.31  |                                                              |
| 1.7 | 0083 0.36 28.9 | 1.77 1.38  |                                                              |
| 1.45                              |                                                              |
| 7. | 0116 0.27 30.1 | 2 38 1.58   |                                                              |

Figure 7 | Reconstruction quality vs loss factor. Fine details like small text are lost for low bitrate latents.

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1772263934_aqadjxvrgzoq4eh_table_2_increasing_the_loss.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
