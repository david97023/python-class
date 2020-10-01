fpWord,fpAns,fpN,wordNum = [],[''],[0],0
with open('DB.txt','r') as fp:
    fpLine = fp.read()
    fpLine = fpLine.replace(' ','')
    tmp = fpLine
    fpLine = fpLine.replace('\n',',')
    fpWord.append(fpLine.split(','))
for i in range(len(fpWord[0])):
    for j in range(len(fpAns)):
        if(fpAns[j] == fpWord[0][i]):
            fpN[j] += 1
            break
            print(fpWord[0][i])
        if(j == len(fpAns)-1):
            fpAns.append(fpWord[0][i])
            fpN.append(1)
for i in range(1,len(fpAns)):
    tmp = tmp.replace(fpAns[i],str(i))
    print(fpAns[i])
with open('IDList.txt','w') as fp:
    for i in range(1,len(fpAns)):
        fp.write(fpAns[i]+", " + str(i) + "\n")
    fp.close()
with open('ItemID.txt','w') as fp:
    fp.write(tmp)
    fp.close()
