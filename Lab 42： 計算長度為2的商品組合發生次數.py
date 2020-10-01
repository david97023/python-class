fpWord=[]
fpAns = ['']
fpN = [0]
tw = []
ta = ['']
tn = [0]
c = []
cN = []
with open('DB.txt','r') as f:
    fpLine = f.read()
    fpLine = fpLine.replace(' ','')
    tmp = fpLine
    fpLine = fpLine.replace('\n',',')
    fpWord.append(fpLine.split(','))
for i in range(len(fpWord[0])):
    for j in range(len(fpAns)):
        if(fpAns[j] == fpWord[0][i]):
            fpN[j] += 1
            break
        if(j == len(fpAns)-1):
            fpAns.append(fpWord[0][i])
            fpN.append(1)
for i in range(1,len(fpAns)):
    tmp = tmp.replace(fpAns[i],str(i))

TL = tmp.replace('\n',',')
tw.append(TL.split(','))
for i in range(len(tw[0])):
    for j in range(len(ta)):
        if(ta[j] == tw[0][i]):
            tn[j] += 1
            break
        if(j == len(ta)-1):
            ta.append(tw[0][i])
            tn.append(1)
for i in range(1,len(ta)):
    for j in range(i,len(ta)):
        c.append(ta[i] + "-" + ta[j])

for i in range(len(c)):
    cN.append(0)
    
for i in range(len(tw[0])):
    for j in range(i,len(tw[0])):
        for w in range(len(c)):
            a = tw[0][i] + "-" + tw[0][j];
            if(a == c[w]):
                cN[w] += 1
for i in range(len(c)):
    print(c[i] + " : " + str(cN[i]))
