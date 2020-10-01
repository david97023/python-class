#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import matplotlib.pyplot as plt
list_A = []
list_B = []
x = [1,2,3,4,5,6,7,8,9,10]
for i in range (10):
    list_A.append(random.randint(1,20))
    list_B.append(random.randint(1,20))
plt.plot(x,list_A,color = "red",lw = "3.0",ls = "--",label = 'A')
plt.plot(x,list_B,color = "blue",lw = "3.0",ls = "-",label = 'B')
plt.legend()
plt.show()

