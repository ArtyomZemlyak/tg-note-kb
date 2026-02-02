# Image Description

**File:** img_1770036024_aqadha5rg07jut_lable_3_comparison_of_sdpo_and.jpg
**Original:** image.jpg
**Received:** 1770036024

## Extracted Text (OCR)

lable 3: Comparison of SDPO and GRPO on reasoning-related benchmarks. We report the highest achieved avg@16 within 1 hour and 5 hours of wall-clock training time, respectively. Both SDPO and on-policy GRPO perform one gradient step per generation batch, while GRPO pertorms 4 oft-policy mini batch steps. We select optimal hyperparameters for 5DPO and baselines based on 5h accuracy. Each run is performed on a node with 4 NVIDIA GH200 GPUs. logether with initialization and validation, each run takes approximately 6 hours.

|                      |           | Physics   | Physics   | Biology    | Materials   | Materials   | Tool use   | Tool use   |
|----------------------|-----------|-----------|-----------|------------|-------------|-------------|------------|------------|
| Owen3-8b             |           | 4Y ?      | 4Y ?      |            | 55.9        | 55.9        | 4/5        | 4/5        |
|                      | 54./ 60.0 |           | 63.56 ИЛ  | 34.5 51.8  |             |             |            | 64.9 6/./  |
| + GRPO (on-policy)   | 54? 69.6  |           |           |            |             | 139 £=/4.]  |            | 60.2 65./  |
| + SDPO (on-policy)   | 60.0 70.1 |           |           | B15 529    |             | // | 1784   |            | 68.0 68.5  |
| ())imo3-7B-I nstruct | 15.85     | 4/./      | 4/./      | 15.1       | '46./       | '46./       | 39.53      | 39.53      |
|                      | 2, 465    |           |           | 4/8 62.0   |             | {09 /50     |            | 456.4 65.0 |
| + GRPO (on-policy)   | 45.8 54.5 |           | 62.7 6,   | 44? 633    |             | 15.5 1/35   |            |            |
| + SDPO (on-policy)   |           |           |           | 56.1 58.35 |             |             |            |            |

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1770036024_aqadha5rg07jut_lable_3_comparison_of_sdpo_and.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
