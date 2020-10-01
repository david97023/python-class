import pandas as pd
import csv
fw=csv.writer(f)
d=pd.read_csv(file)
df=pd.DataFrame(d)
w,s,c=0,100,1
fpdata = pd.read_csv('D:\Step 0_Raw Data\walk1.csv')
for i in range(0,fpdata.shape[0],s):
    print(fpdata.iloc[w:w+s,2:5])
    w=w+50
    file1="D:\\"+"DataSegment"+str(c)+".csv"
    c+=1
    df.iloc[w:w+s,2:5].to_csv(file1,sep=',',header=True,index=True)
