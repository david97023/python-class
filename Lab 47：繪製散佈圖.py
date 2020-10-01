#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
p1=[0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
p2=[87,89,91,90,82,80,78,81,76,85,80,75,73,72]
plt.figure('Draw')
plt.scatter(p1,p2)
plt.xlabel('hours_phone_used')
plt.ylabel('work_performance')
plt.show()

