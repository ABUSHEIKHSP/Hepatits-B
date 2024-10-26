import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

new_col_name = ['Age', 'Gender', 'HBsAg (S/Co)', 'Log DNA (IU/mL)', 'HBeAg','Platelets (10^9/L)', 'PT (Sec)', 'INR', 'TB (mg/dl)', 'DB (mg/dl)',
                'AST (IU/L)','ALT (IU/L)', 'ALT (X ULN)', 'APRI (AST/platelets)','IgM anti-HBc (S/Co)', 'Avidity Index', 'PRE S1 (RR)', 
                'PRE S2 (RR)','Mortality', 'Treatment']

# Custom transformers for column preprocessing:

class DropIrrelevantColumn(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self 
    def transform(self, X, y=None):
        try:
            X = X.drop(['No', 'Study ID'], axis=1)
        except KeyError as e:
            print("Column ['No', 'Study ID'] not found in axis. Skipping Transformation!")
        return X
    
class RenameColumn(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self 
    def transform(self, X, y=None):
        name_map = dict(zip(X.columns.values, new_col_name))
        return X.rename(columns=name_map)
    
def isfloat(x):
    try:
        x = float(x)
    except:
        pass
    return type(x) == float

class HBsAgValueChanger(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass 
    def fit(self, X, y=None):
        hbsag_bool = X['HBsAg (S/Co)'].apply(lambda x: isfloat(x))
        clean = X['HBsAg (S/Co)'][hbsag_bool].astype('float')
        notclean = X['HBsAg (S/Co)'][~hbsag_bool]
        self.max_value = clean.max()
        self.notclean_indeces = notclean.index.values
        return self
    def transform(self, X, y=None):
        X.loc[self.notclean_indeces, 'HBsAg (S/Co)'] = X['HBsAg (S/Co)'][self.notclean_indeces].apply(
                                                                    lambda x: np.nan if x == 'neg' else self.max_value)
        X['HBsAg (S/Co)'] = X['HBsAg (S/Co)'].astype('float')
        return X
    
# Custom transformer for automatically plotting heatmap:
   
class HeatmapGenerator(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None, acute=True):
        self.acute = acute
        X_num_col = [col for col in X.columns if X[col].dtype in ['int', 'float']]
        self.corr = X[X_num_col].corr()
        return self 
    def transform(self, X, y=None):
        plt.figure(figsize=(11, 9))
        sns.heatmap(self.corr, cmap='coolwarm', center=0, linewidths=0.5)
        if self.acute:
            plt.title('Correlation of acute hepatitis B with demographic and selected critical parameters', fontsize=11, fontweight='bold', pad=15)
        else:
            plt.title('Correlation of acute exacerbation of chronic hepatitis B with demographic and selected critical parameters', fontsize=11, fontweight='bold', pad=16)
        plt.tight_layout();


# Colum preprocessing pipeline:
col_pipeline = Pipeline([
    ('drop_col', DropIrrelevantColumn()),
    ('rename_col', RenameColumn()),
    ('hbsag_val_change', HBsAgValueChanger())
])

# Column preprocessing pipeline with Heatmap plotting:
heatmap_pipeline = Pipeline([
    ('col', col_pipeline),
    ('heatmap', HeatmapGenerator())
])