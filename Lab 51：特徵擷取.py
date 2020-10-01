import pandas as pd
import csv
w,s,c=0,100,1
fpdata=pd.read_csv("D:\\DataSegment"+str(c)+".csv")
for i in range(0,fpdata.shape[0],s):
    with open("D:\\DataSegment"+str(c)+'change.csv','w',newline='') as csvfile:
        write=csv.writer(csvfile)
        write.writerow(fpdata.iloc[:,1].mean())
        write.writerow(fpdata.iloc[:,1].std())
        write.writerow(fpdata.iloc[:,1].kurtosis())
    c+=1
