#!/usr/bin/env python
# coding: utf-8

# In[5]:


year=int(input("輸入一個年份:"))
if(year%4!=0):print("為平年")
elif(year%4==0 and year%100!=0):print("為閏年")
elif(year%100==0 and year%400!=0):print("為平年")
elif(year%400==0):print("為閏年")

