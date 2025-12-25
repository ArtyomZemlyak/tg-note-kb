# Image Description

**File:** img_1766649048_aqadqwtrgr2uep9_algorithm_1_next_embedding_prediction.jpg
**Original:** image.jpg
**Received:** 1766649048

## Extracted Text (OCR)

## Algorithm 1 Next-Embedding Prediction

```
Е £: embedding layer # В: autoregressive model for pixel _values in loader: # x, [B, H, W, С] input_embed = f{pixel values) т, [B, T, 0 pred_embed = h(input_embed) + z_hat, [8, T loss = D(input_embed, pred_embed) # loss loss.backward() + back—propagate О] update (f.param, h.param) # update parameters ег D(z, 2 hat): target = z.detach() # stop gradient pred

m Bat [:
"г

ПО:Т-1,

:| # ЗАТЕЕ,

[В,

Т-1, гГагаеЕЁ = taractt:, P22; 21 # &amith,. EB, Т-1, 0] f Use any suitable distance metric. pred = normalize(pred, axis=-1) # 12-norm target = normalize(target, ах15=-1) # 12-norm return —(pred * target) .sum(dim=—1) .mean ()
```

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766649048_aqadqwtrgr2uep9_algorithm_1_next_embedding_prediction.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
