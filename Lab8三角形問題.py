#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=float(input("輸入邊長:"))
y=float(input("輸入邊長:"))
z=float(input("輸入邊長:"))
if(x+y>z and x+z>y and y+z>x):
    print("周長:"+str(x+y+z))
else:print("無法組成三角形")

