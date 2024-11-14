# covid19-gene-expression-analysis

Utilizing [GEO Series GSE147507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147507), the main objective of `covid19-gene-expression-analysis` is to analyze and represent differentially expressed genes, CXCL10, IL6, and TNF, in COVID-19 patients vs. other respiratory disease patients as a heat map and volcano plot. During the progression of COVID-19 infection, patients' immune responses become dysregulated. A "cytokine storm" phenomenon occurs through an uncontrolled production of large amounts of cytokines - inflammatory signaling proteins. This elevated activity can have serious repercussions such as organ failure and tissue damage. Observed inhibition of the "cytokine storm", as well as reduction of these protein concentrations, lead to more effective treatment.

## CXCL10

CXCL10 is a known inflammatory marker that is shown to increase in COVID-19 cases, particularily in severe ones. It could also be a key regulator of the "cytokine storm" immune response.

## IL6

IL6 has a central role in inflammation and is a primary agent that causes the "cytokine storm". Analysis of the IL6 levels in patients allows healthcare professionals to understand the progression and severity of related diseases.

## TNF (TNF-a)

TNF, or Tumor Necrosis Factor, serves as a first line of defense by recruiting inflammatory cells to affected areas and containing infection through formation of granulomas. However, this mediated inflammation response can cause detrimental tissue damage & gradually promotes lung fibrosis as its inhibitors supress antibodies that protect against diseases and conditions such as pneumonia, pulmonary edema, and respiratory distress syndrome.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)

## Features
TBD

## Requirements
- Pipenv
- GEOparse
- matplotlib
- pandas
- seaborn
- DESeq2
- R

## Installation

TBD

## Usage
TBD

## Roadmap
TBD

## References
[What Is Currently Known about the Role of CXCL10 in SARS-CoV-2 Infection?](https://pmc.ncbi.nlm.nih.gov/articles/PMC8998241/)

[GSE147507 Human Gene Raw Read Counts](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE147507)
(Data from 'GSE147507_RawReadCounts_Human.tsv.gz' file.)

## License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)