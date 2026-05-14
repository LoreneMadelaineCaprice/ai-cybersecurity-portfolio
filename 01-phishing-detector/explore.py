import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)

DATA_PATH = Path(__file__).parent / "data" / "Phishing_Legitimate_full.csv"
dataframe = pd.read_csv(DATA_PATH)

print("\n" + "="*100)
print("DATASET SHAPE")
print("="*100)
print(f"Rows    : {dataframe.shape[0]}")
print(f"Columns : {dataframe.shape[1]}")

print("\n" + "="*100)
print("FIRST 5 ROWS")
print("="*100)
print(dataframe.head())

print("\n" + "="*100)
print("DATAFRAME INFO")
print("="*100)
dataframe.info()

print("\n" + "="*100)
print("DESCRIPTIVE STATISTICS")
print("="*100)
print(dataframe.describe().T)


# Variance ------------------------------------------------------------------------
print("Variance of all columns :")
variance_check = dataframe.describe().loc['std']  # La ligne 'std'
print(variance_check)

useless_features = variance_check[variance_check < 0.1]
print("\n Features to remove (low variance) :")
print(useless_features)

# Correlation of Pearson with the label --------------------------------------------

print("\nCorrelation with CLASS_LABEL :")
correlations = dataframe.corr()['CLASS_LABEL'].sort_values(ascending=False)
print(correlations)

top_features = correlations[correlations.abs() > 0.1]
print("\n Best features (correlation > 0.1) :")
print(top_features)