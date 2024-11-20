import pandas as pd
import math
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

def create_data_frame():
    
    # read tsv file as pandas data frame
    raw_df = pd.read_table('GSE147507_RawReadCounts_Human.tsv')

    raw_df = raw_df.rename(columns={'Unnamed: 0': 'Gene_Labels'})

    # remove df columns that do not follow A549_Mock/A549_Covid convention
    remove_columns = ["ACE2", "NHBE", "Calu3", "HPIV", "Lung", "Series4", "Series3"]
    for substring in remove_columns:
        raw_df = raw_df.drop(columns=[col for col in raw_df.columns if substring in col])

    # extract gene label column for reinsertion after running differential analysis
    gene_labels = raw_df['Gene_Labels']

    # remove gene label column for data processing
    filtered_df = raw_df.iloc[:, 1:].replace(0, 1)

    metadata = create_metadata(filtered_df)

    return filtered_df, metadata, gene_labels

def create_metadata(normalized_df):

    sample_names = normalized_df.columns.tolist()
    conditions = []
    
    for name in sample_names:
        if "Mock" in name:
            conditions += ["covid_untreated"]
        else:
            conditions += ["covid_treated"]
    
    metadata = pd.DataFrame({
        'condition': conditions
    }, index=sample_names)

    return metadata

def run_differential_analysis(df, metadata, gene_labels):
    dds = DeseqDataSet(
        counts=df.T,
        metadata=metadata,
        design_factors="condition"
    )

    # DESeq2 normalization and dispersion estimation of data
    dds.deseq2()

    # covid_treated vs covid_untreated
    covid_stats = DeseqStats(dds, contrast=["condition", "covid-treated", "covid-untreated"])

    # identify differentially expressed genes statistically
    covid_stats.summary()

    stats_df = covid_stats.results_df

    # reset indices for alignment
    gene_labels = gene_labels.reset_index(drop=True)
    stats_df = stats_df.reset_index(drop=True)

    # reassign gene labels to df
    stats_df.insert(0, gene_labels.name, gene_labels)

    # set appropriate significance thresholds (e.g., adjusted p-value < 0.05)
    stats_df = stats_df[(stats_df['pvalue'] < 0.05) & (stats_df['padj'] < 0.05)]

    # sort by ascending pvalue and keep first 100 rows
    stats_df = stats_df.sort_values(by='pvalue').iloc[:100]

    print(stats_df.to_string())

run_differential_analysis(*create_data_frame())
