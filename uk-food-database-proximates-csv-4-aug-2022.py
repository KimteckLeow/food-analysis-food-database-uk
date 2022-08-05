#!/usr/bin/env python
# coding: utf-8

# In[2]:
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

#/food-database-uk/1.3_proximates.csv
   
# Import data from .csv file 
fname = os.path.join("1.3_proximates.csv")

# Import data using datetime and set index to datetime

# set the max columns to none
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
proximates_fooddb_uk = pd.read_csv(fname)
proximates_fooddb_uk.head()

# In[3]:
proximates_fooddb_uk.info()

# In[4]:
proximates_fooddb_uk = proximates_fooddb_uk.dropna(subset=['Food Code'])
proximates_fooddb_uk.head()

# In[6]:
#select all columns except 'rebounds' and 'assists'
#df.loc[:, ~df.columns.isin(['rebounds', 'assists'])]

proximates_fooddb_uk_select = proximates_fooddb_uk.loc[:, ~proximates_fooddb_uk.columns.isin(['Description', 'Previous','Main data references', 'Footnote'])]
proximates_fooddb_uk_select.head()

# In[7]:
proximates_fooddb_uk_select.info()

# In[8]:
proximates_fooddb_uk_select

# In[9]:
#view the distribution of food groups with value_counts
pd.value_counts(proximates_fooddb_uk_select.Group)

# In[13]:
len(pd.value_counts(proximates_fooddb_uk_select.Group))

# In[14]:
# Replace Multiple Values in a Column
# DataFrame.replace({'column_name' : { old_value_1 : new_value_1, old_value_2 : new_value_2}})

proximates_fooddb_uk_select_rpl = proximates_fooddb_uk_select.replace({'Group' : { "DR" : "Vegetable dishes", "DG" : "Vegetables, general", "FA" : "Fruit, genera", "MR" : "Meat dishes" , "JA" : "White fish", "MAE" : "Lamb", "MAC" : "Beef", "DB" : "Beans and lentils", "MAG" : "Pork", "MCA" : "Chicken"  }})
proximates_fooddb_uk_select_rpl.head()

# In[15]:
#view the distribution of food groups with value_counts
pd.value_counts(proximates_fooddb_uk_select_rpl.Group)






