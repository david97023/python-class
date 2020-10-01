#!/usr/bin/env python
# coding: utf-8

# In[1]:


def compute(a,x,y):
    for i in range(0,y):
        for j in range(0,x):
            print(a,end=" ")
        print()
d=input()
e=int(input())
f=int(input())
compute(d,e,f)

