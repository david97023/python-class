fpWord=[]
wordNum=0
with open('DB.txt','r') as f:
    print(f.read())
    f.close()
with open('DB.txt','r') as f:
    fpLine = f.readlines()
    print("總交易筆數:{}".format(len( fpLine )))
for i in range(len(fpLine)):
    fpWord.append( fpLine[i].split() )
    wordNum += len( fpWord[i] )
print("總商品個數:{}".format(wordNum))
