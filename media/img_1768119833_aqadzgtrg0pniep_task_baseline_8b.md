# Image Description

**File:** img_1768119833_aqadzgtrg0pniep_task_baseline_8b.jpg
**Original:** image.jpg
**Received:** 1768119833

## Extracted Text (OCR)

|                                                 | Task  | Baseline (8B MoE Base) Baseline + MTP   |
|-------------------------------------------------|-------------------------------------------------|
| General Knowledge                               |                                                 |
| MMLU (5-shot, acc) 70.06 71.26                  |                                                 |
| MMLU-Pro (5-shot, CoT EM) 45.05 47.84           |                                                 |
| (lod  Е                                         |                                                 |
| MBPP-Sanitized (3-shot) | 65.58 66.89           |                                                 |
| Commonsense Understanding                       |                                                 |
| ARC-Challenge (25-shot, acc_norm) | 86.43 88.05 |                                                 |
| WinoGrande (0-shot, acc) | 74.59 75.45          |                                                 |
| Reading Comprehension                           |                                                 |
| RACE (0-shot, acc) 84.02 85.36                  |                                                 |
| GSM8K (8-shot, acc) 82.49 84.46                 |                                                 |

Table 2 | Accuracy scores with and without MTP on a simple 8B active parameter transformer MoE base model trained on ТТ tokens. We observe Improvements ш accuracy on multiple tasks spanning different categories.

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768119833_aqadzgtrg0pniep_task_baseline_8b.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
