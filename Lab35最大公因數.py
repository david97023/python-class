#!/usr/bin/env python
# coding: utf-8

# In[9]:


def compute(x,y):
    for i in range(1,x+1):
        if(x%i==0 and y%i==0):
            n=i
    return n
a=int(input())
b=int(input())
print(compute(a,b))

