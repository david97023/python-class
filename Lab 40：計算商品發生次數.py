fpWord,fpAns,fpN,wordNum=[],[''],[0],0
def countF1():
    with open('DB.txt','r') as f:
        fpLine = f.read()
        fpLine = fpLine.replace(' ','')
        fpLine = fpLine.replace('\n',',')
        fpWord.append(fpLine.split(','))
        return(fpWord)
fpWord=countF1()
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
    print(fpAns[i] + ':' + str(fpN[i]))
