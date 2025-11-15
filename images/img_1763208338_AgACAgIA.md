# Image Description

**File:** img_1763208338_AgACAgIA.jpg
**Original:** image.jpg
**Received:** 1763208338

## Extracted Text (OCR)

## A.1 Examples

We provide some examples of the questions and CoT solutions for the datasets used in our experiments.

Question = "John cuts his grass to 2 inches. It grows .5 inches per month. When it gets to 4 inches he cuts it back down to 2 inches. It cost $100 to get his grass cut. How much does he pay

```
per year?" Steps = ["«4-2=2»", "«2/.5=4»", "«12/4=3>»", "«100*3=300>»"]
```

## ProntoQA

Question = "Brimpuses are not luminous. Shumpuses are amenable. Each yumpus is а lorpus. Gorpuses are shumpuses. Each zumpus is a grimpus. Gorpuses are rompuses. Dumpuses are not floral. Lempuses are cold. Brimpuses are impuses. Every lorpus is floral. Every rompus is transparent. Grimpuses are muffied. Rompuses are yumpuses. Rompuses are wumpuses. Zumpuses are fast. Vumpuses are bitter. Every sterpus is orange. Each lorpus 15 а vumpus. Yumpuses are feisty. Each yumpus is a lempus. Gorpuses are snowy. Zumpuses are gorpuses. Fivery lorpus is a sterpus. Stella is a brimpus. Stella is а zumpus. True or false: Stella is not

```
Steps = ["Stella is a zumpus. Zumpuses are gorpuses.", "Stella is a gorpus. Gorpuses are rompuses.", "Stella is а rompus. Rompuses are yumpuses."", "Stella is а yumpus. Each yumpus is a lorpus.", "Stella is a lorpus. Every lorpus is floral.", "Stella is floral."] Answer = "False"
```

## ProsQA

Question = "Every shumpus is а rempus. Every shumpus is a yimpus. Every terpus is a fompus. E:very terpus is a gerpus. Every gerpus is a brimpus. Alex is a rempus. Every rorpus is а scrompus. Every rorpus 1$ а yimpus. Every terpus 1s a brimpus. Every brimpus 15$ a lempus. Tom 15 а terpus. Every shumpus is a timpus. Every yimpus is а boompus. Davis is a shumpus. F.very gerpus is а lorpus. Vavis 1s a fompus. E.very shumpus is a boompus. Every shumpus 13 a rorpus. Every terpus is a lorpus. Every boompus is а timpus. Every fompus is a yerpus. om is а dumpus. Every rempus is а rorpus. [5 Tom а lempus or scrompus?" Steps = ["Tom 13 a terpus.", "Every terpus is a brimpus.", "Every brimpus is a lempus."]

Answer = "Tom 15 а lempus."

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../images/img_1763208338_AgACAgIA.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
