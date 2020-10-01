#!/usr/bin/env python
# coding: utf-8

# In[3]:


def compute(a,b):
    z=1
    w=2
    if(a>0 and b>0):
        while(a>=w and b>=w):
            if(a%w==0 and b%w==0):
                z=w
            w+=1
        return z
x,y=eval(input())
m,n=eval(input())
s= x*n + m*y
t=y*n
u=compute(s,t)
print(str(x)+"/"+str(y)+"+"+str(m)+"/"+str(n)+"="+str(s//u)+"/"+str(t//u))


# In[ ]:




