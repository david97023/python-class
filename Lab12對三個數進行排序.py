#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("1.輸入整數比大小:"))
b=int(input("2.輸入整數比大小:"))
c=int(input("3.輸入整數比大小:"))
if a>b:
    if b>c:
        print(str(c)+"<"+str(a)+"<"+str(b))
    else:
        if a>c:
            print(str(b)+"<"+str(c)+"<"+str(a))
        else:
            print(str(b)+"<"+str(a)+"<"+str(c))
elif a<b:
    if b<c:
        print(str(a)+"<"+str(b)+"<"+str(c))
    else:
        if c>a:
            print(str(a)+"<"+str(c)+"<"+str(b))
        else:
            print(str(c)+"<"+str(a)+"<"+str(b))
print("相加結果="+str(a+b+c))

