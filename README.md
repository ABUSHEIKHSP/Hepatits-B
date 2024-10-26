# Hepatitis Data Correlation Analysis using Heatmaps

This repository contains a Python pipeline for analyzing the correlation between different variables in hepatitis data using heatmaps.
# Repository Contents

- ***hepatitis_modules.py***: This file contains the Python pipeline for preprocessing and visualizing hepatitis data.
- ***heatmap.ipynb***: This Jupyter Notebook file demonstrates how to use the pipeline to generate heatmaps for acute and chronic hepatitis B data.

# Pipeline Overview

The pipeline consists of two main components:

## 1. Column Preprocessing Pipeline: 
This pipeline performs the following tasks:
- Drops irrelevant columns from the dataset
- Renames columns to more descriptive names
- Converts HBsAg values to numerical values
  
## 2. Heatmap Generation Pipeline: 
This pipeline takes the preprocessed data and generates a heatmap showing the correlation between different variables.

# How the Pipeline Works

Here's a step-by-step overview of how the pipeline works:

- The column preprocessing pipeline is applied to the raw data, resulting in a cleaned and transformed dataset.
- The heatmap generation pipeline is applied to the preprocessed data, resulting in a heatmap showing the correlation between different variables.

# Example Use Cases

The pipeline can be used to generate heatmaps for different types of hepatitis data, such as acute and chronic hepatitis B. For example:

- Acute Hepatitis B Heatmap: This heatmap shows the correlation between different variables in acute hepatitis B patients.
- Chronic Hepatitis B Heatmap: This heatmap shows the correlation between different variables in chronic hepatitis B patients.

# Getting Started

To use the pipeline, simply clone this repository and run the heatmap.ipynb notebook. The notebook will guide you through the process of loading the data, applying the pipeline, and generating the heatmaps.

# Dependencies

The pipeline requires the following dependencies:

    Python 3.x
    NumPy
    Pandas
    Matplotlib
    Seaborn
    Scikit-learn

