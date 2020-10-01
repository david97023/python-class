#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
for i in range(n):
    for a in range(n-i):
        print(' ',end='')
    for b in range(2*i+1):    
        print('*',end='')
    print('\n',end='')

