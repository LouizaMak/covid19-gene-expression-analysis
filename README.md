# covid19-gene-expression-analysis

Utilizing [GEO Series GSE147507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147507), the main objective of `covid19-gene-expression-analysis` is to analyze and represent the top 100 differentially expressed genes in COVID-19 patients vs. non COVID-19 patients as a heat map and volcano plot. During the progression of a COVID-19 infection, patients' immune responses become dysregulated. A "cytokine storm" phenomenon occurs through an uncontrolled production of large amounts of cytokines - inflammatory signaling proteins. This elevated activity can have serious repercussions such as organ failure and tissue damage. Observed inhibition of the "cytokine storm", as well as reduction of these protein concentrations, lead to more effective treatment. 

In addition, many genes expressed can have overlap with other diseases, allowing scientists to identify risk severity for secondary diseases or symptomatic complications. In the case of COVID-19, it is understood that older ages pose a significantly higher risk of developing COVID pneumonia, and in the most severe cases, ARDS (acute respiratory distress syndrome).

# GEO Series GSE147507

For the scope of this project, only samples of A549 (human lung epithelial cell lines) treated and untreated with SARS-CoV-2 were used for the differential analysis. 

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Results](#results)
- [License](#license)

## Features
This project includes the capability to transform data from GEO using the pandas library, R, pyDESeq2, and DESeq2 to present it as a heatmap, top 100 differentially expressed genes list, and volcano plot. It can produce CSV files for normalized counts as well.

## Requirements
- Pipenv
- matplotlib
- pandas
- seaborn
- pyDESeq2
- DESeq2
- R

## Installation

Install Pipenv

```$ pip install pipenv --user```

Install all project dependencies

```pip install -r requirements.txt```

## Results

Summary and Results PDF [here](https://drive.google.com/file/d/1U5o99rULJWvpDyYst3Dv7pVyn0JUmGHG/view).

## References
[What Is Currently Known about the Role of CXCL10 in SARS-CoV-2 Infection?](https://pmc.ncbi.nlm.nih.gov/articles/PMC8998241/)

[GSE147507 Human Gene Raw Read Counts](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE147507)
(Data from 'GSE147507_RawReadCounts_Human.tsv.gz' file.)

[Enrichr](https://maayanlab.cloud/Enrichr/)

## License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)