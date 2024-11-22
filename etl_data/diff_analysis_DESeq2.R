library(DESeq2)

raw_counts <- read.csv("filtered_raw_counts.csv", row.names = 1,
                       check.names = FALSE)
raw_counts <- as.matrix(raw_counts)
metadata <- read.csv("metadata.csv", row.names = 1)

# construct a DESeqDataSet object
dds <- DESeqDataSetFromMatrix(
  countData = raw_counts,
  colData = metadata,
  design = ~ covid19
)

# remove rows with low gene counts
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep, ]

# set the factor level
dds$covid19 <- relevel(dds$covid19, ref = "untreated")

dds <- DESeq(dds)
res <- results(dds)

# remove rows with NA values in pvalue or padj
res <- na.omit(res)

# calculate -log10(p-value) for volcano plot
res$neg_log10_pvalue <- -log10(res$pvalue)

# define thresholds for significant genes
fc_threshold <- 0
pval_threshold <- 0.05

# add column for significance
res$Significance <- "Not Significant"
res$Significance[res$log2FoldChange > fc_threshold &
                   res$padj < pval_threshold] <- "Upregulated"
res$Significance[res$log2FoldChange < -fc_threshold &
                   res$padj < pval_threshold] <- "Downregulated"

write.csv(res, file = "deseq2_res_volcano_plot.csv", row.names = FALSE)