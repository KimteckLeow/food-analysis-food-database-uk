#!/usr/bin/env python
# coding: utf-8

# In[1]:
Import necessary packages
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

#/food-database-uk/1.5_vitamins.csv
# Import data from .csv file 
fname = os.path.join("1.5_vitamins.csv")

# set the max columns to none
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
vitamins_fooddb_uk = pd.read_csv(fname)
vitamins_fooddb_uk.head()

# In[2]:
vitamins_fooddb_uk.info()

# In[3]:
#select all columns except 'rebounds' and 'assists'
#df.loc[:, ~df.columns.isin(['rebounds', 'assists'])]
vitamins_fooddb_uk_select = vitamins_fooddb_uk.loc[:, ~vitamins_fooddb_uk.columns.isin(['Description', 'Previous', 'Main data references', 'Footnote'])]
vitamins_fooddb_uk_select.head()

# In[4]:
vitamins_fooddb_uk_select.info()

# In[5]:
vitamins_fooddb_uk_select

# In[6]:
# Replace Multiple Values in a Column
# DataFrame.replace({'column_name' : { old_value_1 : new_value_1, old_value_2 : new_value_2}})
vitamins_fooddb_uk_select_rpl = vitamins_fooddb_uk_select.replace({'Group' : { "DR" : "Vegetable dishes", "DG" : "Vegetables, general", "FA" : "Fruit, genera", "MR" : "Meat dishes" , "JA" : "White fish", "MAE" : "Lamb", "MAC" : "Beef", "DB" : "Beans and lentils", "MAG" : "Pork", "MCA" : "Chicken"  }})
vitamins_fooddb_uk_select_rpl.head()

# In[7]:
#view the distribution of food groups with value_counts
pd.value_counts(vitamins_fooddb_uk_select_rpl.Group)

# In[8]:
len(pd.value_counts(vitamins_fooddb_uk_select_rpl.Group))

# In[11]:
#Drop 'Food Name'with null values
vitamins_fooddb_uk_select_rpl_drop = vitamins_fooddb_uk_select_rpl.dropna(subset=['Food Name'])
vitamins_fooddb_uk_select_rpl_drop.head()

# In[25]:
# user_df[user_df['sign_up_date'].str.contains('Mushrooms')]
vitamins_fooddb_uk_select_rpl_drop_mush = vitamins_fooddb_uk_select_rpl_drop[vitamins_fooddb_uk_select_rpl_drop["Food Name"].str.contains('Mushrooms')]
vitamins_fooddb_uk_select_rpl_drop_mush

# In[26]:
len(vitamins_fooddb_uk_select_rpl_drop_mush)

# In[27]:
# Select the seventh row with all columns
vitamins_fooddb_uk_select_rpl_drop_mush.iloc[7:8, :]

# In[28]:
#select the 4th, 6th, 7th, and 8th rows of the DataFrame
vitamins_fooddb_uk_select_rpl_drop_mush.iloc[[3, 5, 6, 7]]







