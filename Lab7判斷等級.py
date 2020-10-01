#!/usr/bin/env python
# coding: utf-8

# In[5]:


num=int(input("輸入分數:"))
if(num>94):print("等級:S")
elif(num<95 and num>89):print("等級:A++")
elif(num<90 and num>84):print("等級:A+")
elif(num<85 and num>79):print("等級:A")
elif(num<80 and num>69):print("等級:B")
elif(num<70 and num>59):print("等級:C")
if(num<60):print("等級:F")

