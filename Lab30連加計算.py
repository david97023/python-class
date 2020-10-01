#!/usr/bin/env python
# coding: utf-8

# In[1]:


def compute(x,y):
    a=0
    for i in range(x,y+1):
        a+=i
    return a
a=int(input())
b=int(input())
compute(a,b)

