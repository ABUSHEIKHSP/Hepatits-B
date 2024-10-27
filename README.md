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

* **col_pipeline**: Applies the `DropIrrelevantColumn`, `RenameColumn`, and `HBsAgValueChanger` transformers in sequence.
* **heatmap_pipeline**: Applies the `col_pipeline` and then generates a heatmap using the `HeatmapGenerator` transformer.

## Heatmap Generation
----------------------

The `heatmap.ipynb` file demonstrates how to use the `heatmap_pipeline` to generate heatmaps for acute and chronic hepatitis data. The heatmap generator can be customized to display different titles and correlation matrices.

## Example Usage
-----------------

```python
from hepatitis_modules import heatmap_pipeline

# Load your dataset here
df = ...

# Apply the heatmap pipeline
heatmap_pipeline.fit_transform(df)
```

This will generate a heatmap of correlations between numeric columns in the dataset, with a title indicating that it is for acute hepatitis data.

![image](https://github.com/user-attachments/assets/476d088e-32fd-4668-9896-a87133e740fa)


## Customization
-----------------

You can customize the heatmap generator by passing additional arguments to the `HeatmapGenerator` transformer. For example, you can change the title of the heatmap by passing a different value for the `acute` parameter:

```python
from hepatitis_modules import HeatmapGenerator

# Create a custom heatmap generator
heatmap_generator = HeatmapGenerator(acute=False)

# Apply the heatmap generator to your dataset
heatmap_generator.fit_transform(df)
```

This will generate a heatmap with a title indicating that it is for chronic hepatitis data.

![image](https://github.com/user-attachments/assets/c4dae829-74ff-4db5-9b3d-048d08cb5b4e)


## Getting Started
-------------------

1. Clone the repository: `git clone https://github.com/your-username/hepatitis-data-preprocessing.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Load your dataset and apply the `heatmap_pipeline` to generate a heatmap.

**Note:** This assumes you have Python and Jupyter Notebook installed on your system. If you don't have Jupyter Notebook installed, you can install it using `pip install jupyter` or `conda install jupyter`. Alternatively, you can use a Python IDE like PyCharm or Visual Studio Code to run the code.

**Prerequisites:**

* Python 3.x
* Jupyter Notebook (optional)
* pip or conda for package management

By following these steps, you should be able to get started with the hepatitis data preprocessing pipeline and generate a heatmap using the `heatmap_pipeline`.
