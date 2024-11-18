import pandas as pd
import math
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

def normalize_data_frame():

    #read tsv file as pandas data frame
    raw_df = pd.read_table('GSE147507_RawReadCounts_Human.tsv')

    #df with only CXCL10, IL6, and TNF rows
    filtered_df = raw_df.iloc[[15651,18271,17333]]

    #remove df columns that do not follow A549_Mock/A549_Disease convention
    remove_columns = ["ACE2", "NHBE", "Calu3", "HPIV", "Lung"]
    for substring in remove_columns:
        filtered_df = filtered_df.drop(columns=[col for col in filtered_df.columns if substring in col])

    filtered_df = filtered_df.iloc[:, 1:].replace(0, 1)

    # #normalize data
    # gene_lengths_kb = pd.Series([2.38, 6.0, 3.0], index=[15651,18271,17333])

    # #calculate RPK
    # rpk = filtered_df.iloc[:, 1:].div(gene_lengths_kb, axis = 0)

    # #sum RPK for each sample (column)
    # rpk_sum = rpk.sum(axis=0)

    # #calculate tpm: divide RPK by RPK sum and multiply by 1,000,000
    # tpm = rpk.div(rpk_sum, axis=1) * 1e6

    # #log2 all elements within filtered_df
    # def log2(x):
    #     return math.log2(x)

    # normalized_df = tpm.applymap(lambda x: log2(x))

    metadata = create_metadata(filtered_df)

    # normalized_df.insert(0, 'Unnamed: 0', raw_df['Unnamed: 0'])

    return filtered_df, metadata

def create_metadata(normalized_df):

    sample_names = normalized_df.columns.tolist()
    conditions = []
    
    for name in sample_names:
        if "Series2" in name or "Series5" in name:
            if "Mock" in name:
                conditions += ["covid_untreated"]
            else:
                conditions += ["covid_treated"]
        elif "Series3" in name or "Series8" in name:
            if "Mock" in name:
                conditions += ["rsv_untreated"]
            else:
                conditions += ["rsv_treated"]    
        elif "Series4" in name:
            if "Mock" in name:
                conditions += ["iav_untreated"]
            else:
                conditions += ["iav_treated"]
    
    metadata = pd.DataFrame({
        'condition': conditions
    }, index=sample_names)

    return metadata;

def run_differential_analysis(df, metadata):
    dds = DeseqDataSet(
        counts=df.T,
        metadata=metadata,
        design_factors="condition"
    )

    dds.deseq2()

    stat_res = DeseqStats(dds)

    stat_res.summary()

    print(stat_res.results_df)

run_differential_analysis(*normalize_data_frame())
