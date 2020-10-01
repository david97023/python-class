#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum=0
n=int(input("數字加總問題的啟始值:"))
m=int(input("數字加總問題的結束值:"))
for i in range(n, m+1):
    sum+=i
    i=i+1
print(str(sum))


# In[ ]:




