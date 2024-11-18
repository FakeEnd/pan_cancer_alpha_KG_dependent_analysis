import pandas as pd

# read data
df = pd.read_csv('/archive/bioinformatics/Zhou_lab/shared/jjin/project/pan_cancer_α_KG_dependent_analysis/datasets/CPTAC_data_raw.csv', index_col=0)

# get gene columns
gene_columns = df.columns[2:-2]

# make the missing values in each column to be the mean of that column
df[gene_columns] = df[gene_columns].apply(lambda col: col.fillna(col.mean()))

# set the mapping of cancer types
cancer_type_mapping = {
  "CCRCC_CPTAC_protein": 0,
  "GBM_CPTAC_protein": 1,
  "HNSCC_CPTAC_protein": 2,
  "LSCC_CPTAC_protein": 3,
  "LUAD_CPTAC_protein": 4,
  "PDAC_CPTAC_protein": 5,
  "UCEC_CPTAC1_protein": 6,
  "UCEC_CPTAC2_protein": 7
}

# add a new column 'cancer_type_int' and convert the cancer type to integer
df['cancer_type_int'] = df['cancer_type'].map(cancer_type_mapping)

# drop the rows with missing values in the 'OS' column
df = df.dropna(subset=['OS'])

# save the final data
df.to_csv('/archive/bioinformatics/Zhou_lab/shared/jjin/project/pan_cancer_α_KG_dependent_analysis/datasets/CPTAC_dataset.csv', index=False)

