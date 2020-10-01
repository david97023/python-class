#!/usr/bin/env python
# coding: utf-8

# In[2]:


def compute(a,b,c):
    D=b**2-4*a*c
    if D < 0:
        return None
    elif D==0:
        return -b/2*a
    else:
        ans1=(-b+D**0.5)/(2*a)
        ans2=(-b-D**0.5)/(2*a)
        return str(ans1)+", "+str(ans2)
d=int(input())
e=int(input())
f=int(input())
ans=compute(d,e,f)
if ans==None:
    print("Your equation has noroot.")
else:
    print(ans)

