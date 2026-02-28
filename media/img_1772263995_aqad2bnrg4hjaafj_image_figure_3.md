# Image Description

**File:** img_1772263995_aqad2bnrg4hjaafj_image_figure_3.jpg
**Original:** image.jpg
**Received:** 1772263995

## Extracted Text (OCR)

<!-- image -->

Figure 3 | Illustration of our method of identifying deepthinking tokens. Suppose a model with 10 layers, by setting the depth fraction p = 0.8, the token is successfully classified as a deep-thinking token at generation step t since its JSD with the final-layer distribution first fall below the threshold g only until it reaches the latesettling regime.

```
Algorithm 1: Computing DeepThinking Ratio (DTR) Input :Autoregressive LM fg with L layers and unembedding matrix W,; Input prompt x; Threshold g; Depth fraction p Output : DTR(S) of the generated sequence к С < 0: // deep thinking token count // generated sequence у, < |BOS| ; // initialize with start token while у, + |EOS| do Sample у, ~ р, (<: | x, S)); Pr. = зоИтах(И В, 1); Di. = JSD (per, Pe); end if c, > [(1 — p)L] then Ce—C+l: end end return C/|S|;
```

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1772263995_aqad2bnrg4hjaafj_image_figure_3.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
