# Image Description

**File:** img_1770036024_aqadja5rg07jut_image_a_grpo_5_549.jpg
**Original:** image.jpg
**Received:** 1770036024

## Extracted Text (OCR)

<!-- image -->

(a) GRPO (5,549 tokens) (b) SDPO (764 tokens)

Figure 7: Example responses from GRPO and SDPO after 50 training steps to the following question: "What is the correct octanol/ water distribution coefficient logD under the circumstance of pH 7.4 for the molecule 0=C10[C@@H] (COc2ccon2)CN1c1ccec(C2=CCOCC2)c(F)c1?" The answer options are А: 1.32, В: 1.85, С: 2.61, D: 3.76. The correct answer is С. СКРО'$ answer contains 5х "Hmm.", 9x "No.", and 25x "Wait". Further, GRPO's answer repeats calculations such as "10! = 69.3", which appears four times, and the model even explicitly generates "Wait I'm going in circles". SDPO's answer avoids any circular reasoning and is more than 7x shorter. The base model is Qwen3-8B.

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1770036024_aqadja5rg07jut_image_a_grpo_5_549.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
