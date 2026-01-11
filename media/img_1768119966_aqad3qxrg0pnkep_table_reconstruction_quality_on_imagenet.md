# Image Description

**File:** img_1768119966_aqad3qxrg0pnkep_table_reconstruction_quality_on_imagenet.jpg
**Original:** image.jpg
**Received:** 1768119966

## Extracted Text (OCR)

Table |. Reconstruction quality on ImageNet-1K and MS-COCO 2017 (256x256). Note that our proposed UAE achieves state-of-theart reconstruction among unified tokenizers and remains competitive with strong autoencoders such as Flux-VAE and SD3-VAE. Under identical DINOv2 encoders, UAE significantly outperforms the RAE baseline in both PSNK and SSIM while reducing те by over 90%. When scaled to DINOv2-L, UAE attains the best overall perceptual quality (rFID=0.16) and fidelity (PSNR=33.08, SSIM=0.94), demonstrating the effectiveness of frequency-aware factorization in preserving both semantic and fine-grained visual detail.

|                                                                   | Method Type Katio ImageNet-lIK MS-COCO 2017   | Method Type Katio ImageNet-lIK MS-COCO 2017   | Method Type Katio ImageNet-lIK MS-COCO 2017   |
|-------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
|                                                                   |                                               | PSNRT SSIM7 rFID) PSNR7 SSIM7 rFiDl           |                                               |
| SD-VAER [32] Continuous 8 25.68 0.72 0.75 25.435 0.75 0.76        |                                               |                                               |                                               |
| SD-VAE-EMA [32] Continuous 8 24.99 9.7 0.63 24./6 0.72 0.51       |                                               |                                               |                                               |
| SD3-VAE |23] Continuous 5 29.58 0.86 Q.21 29.50) 0.8/ 0.19        |                                               |                                               |                                               |
| Flux-VAE |2 1] Continuous 8 31.07 0.89 0.17 30.99 0.90 0.19       |                                               |                                               |                                               |
| TokenFlow | 28 | Discrete 16 21.41 0.69 1.37                      |                                               |                                               |                                               |
| Dual Vilok | 12] Discrete 16 22.53 0.14 1.3/                      |                                               |                                               |                                               |
| ЕМОХ [37] Continuous 14 13.49 9.42 3.2}                           |                                               |                                               |                                               |
| Чт ДР [39] Continuous 32 22.99 0.75 0.79                          |                                               |                                               |                                               |
| RAE (DINOv2-B) Continuous 14 18.05 ().5 2.04 18.37 0.49 2.56      |                                               |                                               |                                               |
| UAE (DINOv2-B) Continuous 14 29.65 0.88 0.19 29.23 0.39 0.18      |                                               |                                               |                                               |
| UnikFlow (DINOv2-L) Continuous 14 32.32 0.91 0.17 32.29 0.90 0.18 |                                               |                                               |                                               |
| UAE (DINOv2-L) Continuous 14 33.08 0.94 0.16 52.54 0.94 0.1;      |                                               |                                               |                                               |

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768119966_aqad3qxrg0pnkep_table_reconstruction_quality_on_imagenet.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
