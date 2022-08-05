#!/usr/bin/env python
# coding: utf-8

# In[4]:


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

#/food-database-uk/1.4_inorganics.csv
   

# Import data from .csv file 
fname = os.path.join("1.4_inorganics.csv")

# Import data using datetime and set index to datetime

# set the max columns to none
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
inorganics_fooddb_uk = pd.read_csv(fname)
inorganics_fooddb_uk.head()


# In[5]:


inorganics_fooddb_uk = inorganics_fooddb_uk.dropna(subset=['Food Code'])
inorganics_fooddb_uk.head()


# In[6]:


inorganics_fooddb_uk.info()


# In[8]:


#select all columns except 'rebounds' and 'assists'
#df.loc[:, ~df.columns.isin(['rebounds', 'assists'])]

inorganics_fooddb_uk_select = inorganics_fooddb_uk.loc[:, ~inorganics_fooddb_uk.columns.isin(['Description', 'Previous', 'Main data references', 'Footnote'])]
inorganics_fooddb_uk_select.head()


# In[9]:


inorganics_fooddb_uk_select.info()


# In[10]:


inorganics_fooddb_uk_select


# In[11]:


#view the distribution of food groups with value_counts
pd.value_counts(inorganics_fooddb_uk_select.Group)


# In[12]:


len(pd.value_counts(inorganics_fooddb_uk_select.Group))


# In[13]:


# Replace Multiple Values in a Column
# DataFrame.replace({'column_name' : { old_value_1 : new_value_1, old_value_2 : new_value_2}})

inorganics_fooddb_uk_select_rpl = inorganics_fooddb_uk_select.replace({'Group' : { "DR" : "Vegetable dishes", "DG" : "Vegetables, general", "FA" : "Fruit, genera", "MR" : "Meat dishes" , "JA" : "White fish", "MAE" : "Lamb", "MAC" : "Beef", "DB" : "Beans and lentils", "MAG" : "Pork", "MCA" : "Chicken"  }})
inorganics_fooddb_uk_select_rpl.head()


# In[14]:


#view the distribution of food groups with value_counts
pd.value_counts(inorganics_fooddb_uk_select_rpl.Group)


# In[ ]:




