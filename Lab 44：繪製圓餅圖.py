#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
list_labels = ['Taipei','llan','Taichunng','English']
list_colors = ['yellow','red','blue','green']
value = [50,10,30,10]
explode = (0,0,0.1,0)
plt.pie(value,
       explode = explode,
       labels = list_labels,
       colors = list_colors,
       labeldistance = 1.1,
        autopct = "%3.1f%%",
        shadow = True,
        startangle = 180,
        pctdistance = 0.6
       )
plt.axis("equal")
plt.legend()
plt.show()


# In[ ]:




