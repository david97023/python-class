#!/usr/bin/env python
# coding: utf-8

# In[1]:


nami=0
chopper=0
null=0

for i in range(5):
    vote = int(input())
    if vote==1:
        nami+=1
    elif vote==2:
        chopper+=1
    else:
        null+=1
    print('Total votes of No.1: Nami = ', nami)
    print('Total votes of No.2: Chopper = ', chopper)
    print('Total null votes = ', null)
    
if nami>chopper:
    print('=> No.1 Nami won the election.')
elif chopper>nami:
    print('=> No.2 Chopper won the election.')
else:
    print('=> No one won the election.')

