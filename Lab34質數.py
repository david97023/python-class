#!/usr/bin/env python
# coding: utf-8

# In[3]:


def compute(x):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                return 'Not Prime'
        return 'Prime'
    else:
        return 'Not Prime'
a=int(input())
print(compute(a))

