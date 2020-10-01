#!/usr/bin/env python
# coding: utf-8

# In[1]:


minNum = int(input("輸入十個數字：") ) 
for i in range(1,10):
    a=int(input())
    if a<minNum: minNum=a
print("十個數值中的最小值:"+str(minNum))

