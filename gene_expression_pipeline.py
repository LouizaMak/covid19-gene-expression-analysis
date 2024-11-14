import pandas as pd
import math

#read tsv file as pandas data frame
raw_df = pd.read_table('GSE147507_RawReadCounts_Human.tsv')

#df with only CXCL10, IL6, and TNF rows
filtered_df = raw_df.iloc[[15651,18271,17333]]

#normalize data
gene_lengths_kb = pd.Series([2.38, 6.0, 3.0], index=[15651,18271,17333])

#calculate RPK
rpk = filtered_df.iloc[:, 1:].div(gene_lengths_kb, axis = 0)

#sum RPK for each sample (column)
rpk_sum = rpk.sum(axis=0)

#calculate tpm: divide RPK by RPK sum and multiply by 1,000,000
tpm = rpk.div(rpk_sum, axis=1) * 1e6

#log2 all elements within filtered_df
def log2(x):
    x += 1
    return math.log2(x)

df = tpm.applymap(lambda x: log2(x))
df.insert(0, 'Unnamed: 0', raw_df['Unnamed: 0'])