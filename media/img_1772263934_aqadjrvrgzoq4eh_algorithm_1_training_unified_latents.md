# Image Description

**File:** img_1772263934_aqadjrvrgzoq4eh_algorithm_1_training_unified_latents.jpg
**Original:** image.jpg
**Received:** 1772263934

## Extracted Text (OCR)

## Algorithm 1 Training Unified Latents

```
Sample х ~ Dgata Encode the data зат = E(x, 0} Sample t ~ U(0, 1), е ~ N(0,1) я = Az(t) clean + Oz (t)E Compute prior loss £,(@) = —"s\2 "8 ||
Zclean — 2(2 6)||? + KL|
p(z1|x)|p(z1) |

di Sample t ~ 14(0, 1), е ~ N(0,1), e. ~ N(0,1) 50 = Az(O)Zejean + 0, (ОЕ, x, = ay(t)x + 0,(te Compute decoder loss £,(0) = ast) "pe (А (Ех — R(x, 0, 92 Optimize £(0) = £,(0@) + £,.(@)
```

## Algorithm 2 Sampling Unified Latents

```
Sample z; ~ N(0,I) Sample 20 ~ ро(50|21) from diffusion base model Sample x; ~ ^/(0, Г) Sample x ~ pg(x|zo, x1) from diffusion decoder model
```

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1772263934_aqadjrvrgzoq4eh_algorithm_1_training_unified_latents.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
