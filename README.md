# Topic modeling of non parallel multilingual corpora
## Abstract
Topic model is a well proven tool to investigate the semantic content of textual corpora. Yet corpora sometimes include texts in several languages, making it impossible to apply language-specific computational approaches over their entire content. This is the problem we encountered when setting to analyze a philosophy of science corpus spanning over 8 decades and including original articles in Dutch, German and French, on top of a large majority of articles in English. To circumvent this multilingual problem, we propose to use machine-translation tools to bulk translate non-English documents into English. Though largely imperfect, especially syntactically, these translations should nevertheless provide correctly translated terms and preserve the semantic proximity of documents with respect to one another. To assess the quality of this translation step, we develop a “semantic topology preservation test” that relies on estimating the extent to which document-to-document distances have been preserved during translation. We then conduct an LDA topic-model analysis over the entire corpus of translated and English original texts, and compare it to a topic-model done over the English original texts only. We thereby identify the specific contribution of the translated texts. These studies reveal a more complete picture of main topics that can found in the philosophy of science literature, especially during the early days of the discipline when numerous articles were published in languages other than English.
## Methodology
### 1. Langage detection and machine translation
a) Langage detection
b) Machine translation
### 2. Inspection
a) Rule-based inspection
b) Manual inspection
### 3. Topology preservation test
### 4. Preprocessing and topic modeling
a) Preprocessing
b) Topic modeling
### 5. Comparaison with previous topic-model
### 6. Diachronic and journal analyses
### 7. Futher comparisons with previous topic-model
## Requirements
### Topology preservation test
This code was tested on R Version 3.6.1. Other requirements are as follows:
- dplyr
- xlsx
- readr
- FactoMineR
- vegan
- RSpectra
- parallelDist
### Topic model
This code was tested on Python 3.7.3. Other requirements are as follows:
- lda
- scipy
- sklearn
- numpy
- pandas
- (See requirements.txt)
## Quick Start
### Topology preservation test
1. X
2. Y
### Topic model
1. Install libraries: pip install -r requirements.txt
2. X
## Citation
Malaterre, Christophe., and Francis Lareau (in press). 
## Authors
### Christophe Malaterre
- Email: malaterre.christophe@uqam.ca
### Francis Lareau
- Email: francislareau@hotmail.com
## Acknowledgments
The authors are grateful to JSTOR, Elsevier, Oxford University Press, Springer, Taylor and Francis, and University of Chicago Press for providing access to journal articles for text-mining purposes. Special thanks are due to Pedro Peres-Neto for providing guidance with matrix similarity measures, to Sari Lemable and Frédérick Deschênes respectively for Dutch and German translation checks, and to Rens Strijbos for insights about W. M. Kruseman. The authors also thank the audiences of a 2020 TEC seminar at UQAM and of the DS2-2021 conference for comments on an earlier version of the manuscript. C.M. acknowledges funding from Canada Foundation for Innovation (Grant 34555) and Canada Research Chairs (CRC-950-230795). F.L. acknowledges funding from the Fonds de recherche du Québec - Société et culture (FRQSC-276470).
