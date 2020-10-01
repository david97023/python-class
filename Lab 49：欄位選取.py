#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
fpdata = pd.read_csv('D:\Step 0_Raw Data\walk1.csv')
print(fpdata.iloc[:,2:5])  #取第2.3.4行

