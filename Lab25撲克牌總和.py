#!/usr/bin/env python
# coding: utf-8

# In[9]:


sum=0

for i in range(5):
    str=input()
    if str=='J':n=11
    elif str=='Q':n=12
    elif str=='K':n=13
    elif str=='A':n=1
    else: n=int(str)
    sum+=n
print(sum)

