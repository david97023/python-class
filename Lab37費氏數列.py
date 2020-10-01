#!/usr/bin/env python
# coding: utf-8

# In[3]:


def compute(n):
    n1=0
    n2=1
    print(n1,n2,end=" ")
    for i in range(3,n+1):
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
x=int(input())
compute(x)


# In[ ]:




