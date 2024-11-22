import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from diff_analysis_top_100_genes import create_data_frame

def create_heatmap():
    df = pd.read_csv('vst_normalized_counts.csv')
    gene_labels = create_data_frame()[2]

    # cut to 25 rows for heatmap readability
    top_25_genes_df = pd.read_csv('top_100_genes.csv').head(25)
    
    # reassign gene labels to df
    df.insert(0, gene_labels.name, gene_labels)

    # drop duplicate index column
    df.drop('Unnamed: 0', axis=1, inplace=True)

    # filter df using the top 100 differentially expressed genes list
    top_25_df = df[df['Gene_Labels'].isin(top_25_genes_df['Gene_Labels'])]

    # set gene_labels column as index
    top_25_df.set_index('Gene_Labels', inplace=True)

    plt.figure(figsize=(11,13))
    sns.heatmap(top_25_df, annot=True, fmt=".2f", cbar_kws={'label': 'Expression Level'}, square=True)
    plt.title("COVID-19 vs. Control Top 25 Differentially Expressed Genes in GEO Series GSE147507 Heatmap")
    plt.xlabel("Samples")
    plt.ylabel("Genes")

    plt.show()

create_heatmap()