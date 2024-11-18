
# Pan Cancer alpha KG Dependent Analysis for Biomarker Discovery

This repository contains code and data for a deep learning (DL)-based computational framework designed to discover and validate prognostic biomarkers for renal cell carcinoma (RCC). Using this framework, we identified Phytanoyl-CoA Dioxygenase Domain Containing 1 (PHYHD1) as a novel tumor suppressor and potential biomarker for RCC, offering insights into RCC growth mechanisms and potential therapeutic targets.

## Project Overview

### Research Background

Renal cell carcinoma (RCC) presents significant challenges in early diagnosis and has limited response to traditional treatments. This study explores the role of PHYHD1, identified as a promising prognostic biomarker via a DL-based framework that interprets complex tissue patterns. PHYHD1, predominantly expressed in normal tissues, was found to be downregulated in RCC tumors, suggesting its function as a tumor suppressor. Restoring PHYHD1 expression in RCC cells reduced tumor growth, revealing its potential as a therapeutic target. Further analyses identified Ceramide Transport Protein 1 (CERT1) as a downstream target of PHYHD1, forming the PHYHD1-CERT1 regulatory axis involved in RCC cell proliferation.

## Project Structure

```plaintext
pan_cancer_α_KG_dependent_analysis/
├── datasets/
│   └── preprocess/
│         └── CPTAC_data_preprocess.py
│   ├── CPTAC_cancer_type_mapping.json
│   ├── CPTAC_data_raw.csv
│   ├── CPTAC_dataset.csv
│   ├── TCGA_cancer_type_mapping.json
│   └── TCGA_dataset.csv
├── notebooks/
│   ├── TCGA_analysis.ipynb
│   └── CPTAC_analysis.ipynb
└── saves/
    ├── TCGA_best_model.pth
    └── CPTAC_best_model.pth
```

### Directory Breakdown

- **datasets/preprocess**: Contains raw datasets and preprocessing scripts, including:
  - `CPTAC_data_preprocess.py`: Preprocesses CPTAC data for DL model input.
  - JSON files: Mapping files for cancer types across datasets.
  - CSV files: Raw and processed datasets for RCC analysis from CPTAC and TCGA datasets.

- **notebooks**: Main analysis code in Jupyter notebooks.
  - `TCGA_analysis.ipynb`: Notebook focusing on TCGA dataset for model training and evaluation.
  - `CPTAC_analysis.ipynb`: Notebook focusing on CPTAC dataset for model training and evaluation.

- **saves**: Directory containing trained model files in `.pth` format for reproducibility and further analysis.

## Environment Setup

### Prerequisites

To replicate this study, install Anaconda and set up an environment with Python 3.9.

### Creating the Conda Environment

1. **Create and activate the environment**:
   ```bash
   conda create -n cancer_analysis python=3.9
   conda activate cancer_analysis
   ```

2. **Install required packages**:
   ```bash
   # PyTorch and dependencies
   conda install pytorch torchvision torchaudio -c pytorch

   # Other required packages
   conda install shap matplotlib pandas numpy scikit-learn

   # Install Captum (for model interpretability) and pyensembl using pip
   pip install captum pyensembl

   # Jupyter for running notebooks
   conda install jupyter
   ```

3. **Set up pyensembl** (if genomic data is analyzed):
   ```python
   import pyensembl
   data = pyensembl.EnsemblRelease(104, species="homo_sapiens")
   data.download()
   data.index()
   ```

### Running Jupyter Notebooks

Navigate to the project directory and start Jupyter Notebook:

```bash
jupyter notebook
```

Open `TCGA_analysis.ipynb` and `CPTAC_analysis.ipynb` in the `notebooks` folder to begin analysis.

## Usage

1. **Data Preprocessing**:
   - Ensure that CPTAC and TCGA dataset in the datasets folder.

2. **Model Training and Analysis**:
   - Open `TCGA_analysis.ipynb` and `CPTAC_analysis.ipynb` in `notebooks` to perform pan-cancer analysis, including Caputum and SHAP analysis.
   - These notebooks will load or train models, saving the results in the `saves` directory.


## Citation

Please credit this work if it assists in your research or academic projects.
