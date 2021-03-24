# Topic modeling of non parallel multilingual corpora
## Abstract
Topic model is a well proven tool to investigate the semantic content of textual corpora. Yet corpora sometimes include texts in several languages, making it impossible to apply language-specific computational approaches over their entire content. This is the problem we encountered when setting to analyze a philosophy of science corpus spanning over 8 decades and including original articles in Dutch, German and French, on top of a large majority of articles in English. To circumvent this multilingual problem, we propose to use machine-translation tools to bulk translate non-English documents into English. Though largely imperfect, especially syntactically, these translations should nevertheless provide correctly translated terms and preserve the semantic proximity of documents with respect to one another. To assess the quality of this translation step, we develop a “semantic topology preservation test” that relies on estimating the extent to which document-to-document distances have been preserved during translation. We then conduct an LDA topic-model analysis over the entire corpus of translated and English original texts, and compare it to a topic-model done over the English original texts only. We thereby identify the specific contribution of the translated texts. These studies reveal a more complete picture of main topics that can found in the philosophy of science literature, especially during the early days of the discipline when numerous articles were published in languages other than English.
## Requirements
### R
This code was tested on R Version 3.6.1. Other requirements are as follows:
- text2vec
- stringr
- dplyr
- xlsx
- readr
- FactoMineR
- vegan
- RSpectra
- parallelDist
### Python
This code was tested on Python 3.7.3. Other requirements are as follows:
- lda
- scipy
- sklearn
- numpy
- pandas
- (See requirements.txt)
## Quick Start
- Install libraries: pip install -r requirements.txt
### 1. Langage detection and machine translation\*
- Execute to replicate research : Langage_detection_and_machine_translation.py
### 2. Inspection
#### 2.1 Rule-based inspection\*
- Execute to replicate research : Rule-based inspection.Rmd
#### 2.2 Manual inspection
### 3. Topology preservation test
- Execute to replicate research : Topology_preservation_test.Rmd
### 4. Preprocessing and topic modeling
#### 4.1 Preprocessing\*
- Execute to replicate research : Preprocessing.py
#### 4.2 Topic modeling
- Execute to replicate research : Topic_modeling.py
### 5. Comparaison with previous topic-model
- Execute to replicate research : Comparisons with previous topic modeling.py
### 6. Diachronic and journal analyses
- Execute to replicate research : Diachronic_and_journal_analyses.py
### 7. Futher comparisons with previous topic-model
\*Note that for legal issues, the complete full-text of journal articles could not be included with the dataset (but can be retrieved by asking JSTOR and the respective publishers).
## Citation
Malaterre, Christophe., and Francis Lareau (draft). 
## Authors
### Christophe Malaterre
- Email: malaterre.christophe@uqam.ca
### Francis Lareau
- Email: francislareau@hotmail.com
## Acknowledgments
The authors are grateful to JSTOR, Elsevier, Oxford University Press, Springer, Taylor and Francis, and University of Chicago Press for providing access to journal articles for text-mining purposes. Special thanks are due to Pedro Peres-Neto for providing guidance with matrix similarity measures, to Sari Lemable and Frédérick Deschênes respectively for Dutch and German translation checks, and to Rens Strijbos for insights about W. M. Kruseman. The authors also thank the audiences of a 2020 TEC seminar at UQAM and of the DS2-2021 conference for comments on an earlier version of the manuscript. C.M. acknowledges funding from Canada Foundation for Innovation (Grant 34555) and Canada Research Chairs (CRC-950-230795). F.L. acknowledges funding from the Fonds de recherche du Québec - Société et culture (FRQSC-276470).
