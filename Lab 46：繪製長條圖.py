import heapq
import matplotlib.pyplot as plt
fpWord=[]
fpAns = ['']
fpN = [0]
wordNum=0
with open('E:\chainstoreFIM.txt','r') as f:
    fpLine = f.read()
    fpLine = fpLine.replace('\n',' ')
    fpWord.append(fpLine.split(' '))
for i in range(len(fpWord[0])):
    for j in range(len(fpAns)):
        if(fpAns[j] == fpWord[0][i]):
            fpN[j] += 1
            break
            print(fpWord[0][i])
        if(j == len(fpAns)-1):
            fpAns.append(fpWord[0][i])
            fpN.append(1)
max = map(fpN.index, heapq.nlargest(5, fpN))
print(fpAns[list(max)[4]])
list1 = heapq.nlargest(5, fpN)
list2 = [fpAns[list(max)[0]],fpAns[list(max)[1]],fpAns[list(max)[2]],fpAns[list(max)[3]],fpAns[list(max)[4]]]
plt.bar(list2,list1)




