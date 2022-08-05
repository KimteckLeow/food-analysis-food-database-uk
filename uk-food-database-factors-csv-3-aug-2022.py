#!/usr/bin/env python
# coding: utf-8

# In[1]:
# Import necessary packages
from matplotlib.axes._axes import _log as matplotlib_axes_logger
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import earthpy as et
import numpy as np

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Dealing with error thrown by one of the plots
matplotlib_axes_logger.setLevel('ERROR')
import warnings
warnings.filterwarnings('ignore')

# Adjust font size and style of all plots in notebook with seaborn
sns.set(font_scale=1.5, style="whitegrid")

# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, "earth-analytics","food-database-uk"))

# /food-database-uk/1.2_factors.csv
# /food-database-uk/factors_1.2.csv    

# Import data from .csv file 
fname = os.path.join("1.2_factors.csv")

# set the max columns to none
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
factors_fooddb_uk = pd.read_csv(fname)
factors_fooddb_uk

# In[7]:
print(factors_fooddb_uk.columns.tolist())

# In[8]:
factors_fooddb_uk.info()

# In[3]:
factors_fooddb_uk_select = factors_fooddb_uk[["Food Code", "Food Name", "Group", "Edible proportion", "Nitrogen conversion factor", "Glycerol conversion factor"]]
factors_fooddb_uk_select

# In[4]:
factors_fooddb_uk_select = factors_fooddb_uk_select.dropna(subset=['Food Code'])
factors_fooddb_uk_select.head()

# In[5]:
factors_fooddb_uk_select

# In[6]:
len(factors_fooddb_uk_select)

# In[9]:
#extract rows/columns with missing values
factors_fooddb_uk_select_nan = factors_fooddb_uk_select.isnull()
factors_fooddb_uk_select_nan







