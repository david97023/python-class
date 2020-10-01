#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("輸入一個正整數:"))
if(num%2==0 and num%5==0):print("是2和5的倍數")
elif(num%2==0 and num%5!=0):print("是2的倍數，但不是5的倍數")
elif(num%2!=0 and num%5==0):print("是5的倍數，但不是2的倍數")
elif(num%2!=0 and num%5!=0):print("不是2和5的倍數")


# In[ ]:




