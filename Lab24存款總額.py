#!/usr/bin/env python
# coding: utf-8

# In[5]:


money=int(input())
rate=float(input())
month=int(input())
print('Month\t Amount')
for i in range(1,month+1):
    total=money+(money*rate)/1200
    money=total
    print( '{:3d} \t {:.2f}'.format( i, total ) )

