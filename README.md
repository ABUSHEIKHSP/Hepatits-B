# Hepatitis B Data Preprocessing and Analysis
==========================================================================================

## Overview
------------

This repository contains a collection of custom transformers and pipelines for preprocessing Hepatitis-B data, as well as a heatmap generator for visualizing correlations between demographic and critical parameters.

## Transformers and Pipelines
-----------------------------

### Custom Transformers

The `hepatitis_modules.py` file defines the following custom transformers:

* **DropIrrelevantColumn**: Drops irrelevant columns (`'No'` and `'Study ID'`) from the dataset.
* **RenameColumn**: Renames columns to a standardized set of names (`new_col_name`).
* **HBsAgValueChanger**: Converts non-numeric values in the `'HBsAg (S/Co)'` column to NaN or a maximum value.
* **HeatmapGenerator**: Generates a heatmap of correlations between numeric columns in the dataset.

### Pipelines

The repository defines two pipelines:

* **col_pipeline**: Applies the `DropIrrelevantColumn`, `RenameColumn`, and `HBsAgValueChanger` transformers in sequence. This pipeline is designed to perform the initial data cleaning and preprocessing steps, which are necessary for building a machine learning model in the future. Additional transformers can be added to this pipeline as needed for specific machine learning tasks.
* **heatmap_pipeline**: Applies the `col_pipeline` and then generates a heatmap using the `HeatmapGenerator` transformer. This pipeline is designed to provide a quick and easy way to generate a heatmap, without having to manually call the `col_pipeline` and `HeatmapGenerator` transformers separately.

## Heatmap Generation
----------------------

The `heatmap.ipynb` file demonstrates how to use the `heatmap_pipeline` to generate heatmaps for acute and chronic hepatitis data. The heatmap generator can be customized to display different titles and correlation matrices.

## How To Use
--------------

You can use the `heatmap_pipeline` to generate a heatmap with the initial data cleaning and preprocessing steps applied, or you can use the `HeatmapGenerator` transformer directly to an already preprocessed data to generate a heatmap.

### Using the Heatmap Pipeline

To use the `heatmap_pipeline`, you can simply apply it to your dataset without having to manually call the `col_pipeline` and `HeatmapGenerator` transformers separately.

```python
from hepatitis_modules import heatmap_pipeline

# Load your dataset here
df = ...

# Apply the heatmap pipeline
heatmap_pipeline.fit_transform(df)
```

### Using the HeatmapGenerator Directly

To use the `HeatmapGenerator` transformer directly, you will need to first apply the `col_pipeline` to your dataset to perform the necessary data cleaning and preprocessing steps.

```python
from hepatitis_modules import col_pipeline, HeatmapGenerator

# Load your dataset here
df = ...

# Apply the col_pipeline to your dataset
df = col_pipeline.fit_transform(df)

# Create a custom heatmap generator
heatmap_generator = HeatmapGenerator()

# Apply the heatmap generator to your dataset
heatmap_generator.fit_transform(df)
```

### Parameters

You can customize the heatmap by passing additional arguments to the `HeatmapGenerator` transformer or to the `heatmap_pipeline`. You can generate heatmap for `chronic` by passing `acute=False`. By default acute is set to True.

```python
# Generating heatmap for acute hepatits-B
heatmap_pipeline.fit_transform(df)
```
![image](https://github.com/user-attachments/assets/22dba8df-1c73-4b33-9155-7adf2a4de2a7)


```python
# Generating heatmap for chronic hepatits-B
heatmap_pipeline.fit_transform(df, acute=False)
```
![image](https://github.com/user-attachments/assets/8b7be12b-6825-41b3-9a02-c90b4875bf07)


## Getting Started
-------------------

1. Clone the repository: `git clone https://github.com/ABUSHEIKHSP/Hepatits-B.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Load your dataset and apply the `heatmap_pipeline` to generate a heatmap.

**Note:** This assumes you have Python and Jupyter Notebook installed on your system. If you don't have Jupyter Notebook installed, you can install it using `pip install jupyter` or `conda install jupyter`. Alternatively, you can use a Python IDE like PyCharm or Visual Studio Code to run the code.

**Prerequisites:**

* Python 3.x
* Jupyter Notebook (optional)
* pip or conda for package management

By following these steps, you should be able to get started with the hepatitis data preprocessing pipeline and generate a heatmap using the `heatmap_pipeline`.
