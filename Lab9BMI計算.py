#!/usr/bin/env python
# coding: utf-8

# In[1]:


t=float(input("輸入身高(公尺):"))
w=float(input("輸入體重(公斤):"))
BMI = w/(t*t)
print("BMI:"+str(BMI))
if(BMI<18.5):print("體重過輕")
if(24>BMI>=18.5):print("健康體位")
if(BMI>=24):print("體重過重")

