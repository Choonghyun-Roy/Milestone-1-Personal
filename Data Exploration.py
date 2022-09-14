# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Package imports
import pandas as pd
import seaborn as sns 
import missingno as msno
# %matplotlib inline

df = pd.read_csv('./datasets/WDIData.csv')
df

# access to google drive

