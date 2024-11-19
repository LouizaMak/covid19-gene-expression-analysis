import pandas as pd
import math
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

def normalize_data_frame():

    #read tsv file as pandas data frame
    raw_df = pd.read_table('GSE147507_RawReadCounts_Human.tsv')

    #remove df columns that do not follow A549_Mock/A549_Covid convention
    remove_columns = ["ACE2", "NHBE", "Calu3", "HPIV", "Lung", "Series4", "Series3"]
    for substring in remove_columns:
        raw_df = raw_df.drop(columns=[col for col in raw_df.columns if substring in col])

    #remove gene label column for data processing
    filtered_df = raw_df.iloc[:, 1:].replace(0, 1)

    metadata = create_metadata(filtered_df)

    # normalized_df.insert(0, 'Unnamed: 0', raw_df['Unnamed: 0'])

    return filtered_df, metadata

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

def run_differential_analysis(df, metadata):
    dds = DeseqDataSet(
        counts=df.T,
        metadata=metadata,
        design_factors="condition"
    )

    #DESeq2 normalization and dispersion estimation of data
    dds.deseq2()

    #covid_treated vs covid_untreated
    covid_stats = DeseqStats(dds, contrast=["condition", "covid-treated", "covid-untreated"])

    #identify differentially expressed genes statistically
    covid_stats.summary()

    #set appropriate significance thresholds (e.g., adjusted p-value < 0.05)
    stats_df = covid_stats.results_df[covid_stats.results_df['pvalue'] < 0.05]
    stats_df = stats_df[stats_df['padj'] < 0.05]

    #sort by ascending pvalue and keep first 100 rows
    stats_df = stats_df.sort_values(by='pvalue').iloc[:100]

    #reassign gene labels to 100 rows

run_differential_analysis(*normalize_data_frame())
