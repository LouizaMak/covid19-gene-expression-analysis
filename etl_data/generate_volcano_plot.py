import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from diff_analysis_top_100_genes import create_data_frame

def create_csv_files():

    # remove df columns that do not follow A549_Mock/A549_Covid convention
    # extract gene label column for reinsertion after running differential analysis
    # remove gene label column for data processing
    filtered_df, metadata, _ = create_data_frame()

    filtered_df.to_csv("filtered_raw_counts.csv")
    metadata.to_csv("metadata.csv")

def create_volcano_plot():
    data = pd.read_csv('deseq2_res_volcano_plot.csv')

    plt.figure(figsize=(7,10))
    sns.scatterplot(data=data, x='log2FoldChange', y='neg_log10_pvalue', hue='Significance')

    plt.title("GEO Series GSE147507 COVID-19 vs. Non-COVID-19 Differential Expression Analysis")
    plt.xlabel("log2(Fold Change)")
    plt.ylabel("-log10(Pvalue)")
    plt.show()

create_volcano_plot()