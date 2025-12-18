# Image Description

**File:** img_1766039991_aqadlhnrg5clgup9_table_3_model_architecture_and_parameter.jpg
**Original:** image.jpg
**Received:** 1766039991

## Extracted Text (OCR)

Table 3: Model architecture and parameter efficiency.

| Component Parameters           |                                |                                |
|--------------------------------|--------------------------------|--------------------------------|
| Stage 1: JEPA encoder training | Stage 1: JEPA encoder training | Stage 1: JEPA encoder training |
| (Online encoder 121.7M         | Trainable                      |                                |
| Target encoder (EMA) 118.5M    | Momentum update                |                                |
| Predictor network eA |         | Trainable                      |                                |
| Stage 1 total 240.2M           | 121.7M trainable               |                                |
| Stage 2: decoder training      | Stage 2: decoder training      | Stage 2: decoder training      |
| JEPA encoder IAD OM            | fine-tuned                     |                                |
| FSQ quantizer ~ (.01M          |                                |                                |
| Hikfi-GAWN decoder 69.2M       | Trainahle                      |                                |
| Stage 2 total 309.5M           | ЗМ trainable                   |                                |
| Final model (inference)        | Final model (inference)        | Final model (inference)        |
| Kncoder only 121.7M            | Online encoder only            |                                |
| FSQ + decoder 69.3M            |                                |                                |
| Interence total 191.0M         | Single-pass model              |                                |

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766039991_aqadlhnrg5clgup9_table_3_model_architecture_and_parameter.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
