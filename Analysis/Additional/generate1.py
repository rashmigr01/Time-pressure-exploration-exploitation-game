import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy.stats import entropy
import random

def myent(x):
    _, counts = np.unique(x, return_counts=True)
    return entropy(counts, base=2)/ np.log2(len(x))

i = 1
l1 = []
l2 = []
l3 = []

e1 = []
e2 = []
e3 = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_ext'+str(i)+'.csv',usecols=["Choice","Time Condition"])
    data_list = csvFile.T.values.tolist()
    
    j = 0
    while (j<480):
        if(data_list[1][j] == 'Unlimited Time'):
            l3.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time - 800ms'):
            l2.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time - 400ms'):
            l1.append(data_list[0][j])
        j = j + 1
        
    e1.append(myent(l1))
    e2.append(myent(l2))
    e3.append(myent(l3))
    i = i + 1

lis = e1+e2+e3

colors = []
for i in range(len(lis)):
    if(i<len(lis)/3):
        colors.append('khaki')
    elif(i<2*len(lis)/3):
        colors.append('skyblue')
    else:
        colors.append('palegreen')

i = 1
li1 = []
li2 = []

ei1 = []
ei2 = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_rep'+str(i)+'.csv',usecols=["Choice","Time Condition"])
    data_list = csvFile.T.values.tolist()
    
    j = 0
    while (j<320):
        if(data_list[1][j] == 'Unlimited Time'):
            li2.append(data_list[0][j])
        elif(data_list[1][j] == 'Limited Time'):
            li1.append(data_list[0][j])
        j = j + 1
        
    ei1.append(myent(li1))
    ei2.append(myent(li2))
    i = i + 1

lisr = ei1+ei2

colorsr = []
for i in range(len(lisr)):
    if(i<len(lisr)/2):
        colorsr.append('khaki')
    else:
        colorsr.append('palegreen')

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8, 6))

ran = []
for i in range(480):
    ran.append(random.choice(['q','w','o','p']))

ax1.axhline(y = myent(ran), color = 'black',linestyle = 'dashed')
ax2.axhline(y = myent(ran), color = 'black',linestyle = 'dashed')
xlis = []
for k in range(14):
    if k<(7):
        xlis.append('Replication')
    else:
        xlis.append('Extension')

ylis = lisr[:7]+lis[:7]
clis = colorsr+colors

ax1.scatter(xlis, ylis,c='khaki')
for i in range(7):
    ax1.plot(['Replication','Extension'], [lisr[i],lis[i]], color='gray',lw=0.5, zorder=-1)

ylis = lisr[-7:]+lis[-7:]
ax2.scatter(xlis, ylis,c='palegreen')
for i in range(7):
    ax2.plot(['Replication','Extension'], [lisr[7+i],lis[14+i]], color='gray',lw=0.5, zorder=-1)

fig.suptitle('Entropy Comparision')
ax1.set_title('Limited Time - 400 ms')
ax2.set_title('Unlimited Time')

plt.savefig('Figure1.png')