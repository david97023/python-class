#!/usr/bin/env python
# coding: utf-8

# In[6]:


gradeLi = [ [ 0 for i in range( 5 ) ] for j in range( 3 ) ]
for i in range( 3 ):
    print( 'The '+str(i+1)+'st student:' )
    for j in range( 5 ): gradeLi[i][j] = int( input() )

for i in range( 3 ):
    total = sum( gradeLi[i] )
    print("Student {}\n#Sum {}\n#Average {:.2f}".format( ( i+1 ), total, ( total/5 ) ) )

