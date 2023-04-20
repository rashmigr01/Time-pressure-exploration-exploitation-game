import pandas
import matplotlib.pyplot as plt

i = 1
l1 = []
l2 = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_rep'+str(i)+'.csv',usecols=["Reaction Time","Time Condition"], na_filter= False)
    data_list = csvFile.T.values.tolist()
    rtu = []
    rtl = []
    j = 0
    while (j<320):
        if(data_list[1][j] == 'Unlimited Time'):
            rtu.append(float(data_list[0][j]))
        elif(data_list[1][j] == 'Limited Time'):
            if data_list[0][j]=='':
                rtl.append(400.0)
            else:
                rtl.append(float(data_list[0][j]))
        j = j + 1
        
    l1.append(sum(rtl)/160)
    l2.append(sum(rtu)/160)
    i = i + 1

lis = l1+l2

i = 1
l1e = []
l2e = []
l3e = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_ext'+str(i)+'.csv',usecols=["Reaction Time","Time Condition"], na_filter= False)
    data_list = csvFile.T.values.tolist()
    
    rtu = []
    rtl = []
    rtli = []
    j = 0
    while (j<480):
        if(data_list[1][j] == 'Unlimited Time'):
            rtu.append(float(data_list[0][j]))
        elif(data_list[1][j] == 'Limited Time - 800ms'):
            if data_list[0][j]=='':
                rtli.append(800.0)
            else:
                rtli.append(float(data_list[0][j]))
        elif(data_list[1][j] == 'Limited Time - 400ms'):
            if data_list[0][j]=='':
                rtl.append(400.0)
            else:
                rtl.append(float(data_list[0][j]))
        j = j + 1
        
    l1e.append(sum(rtl)/160)
    l2e.append(sum(rtli)/160)
    l3e.append(sum(rtu)/160)
    i = i + 1

lise = l1e+l2e+l3e

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8, 6))

xlis = []
for k in range(14):
    if k<(7):
        xlis.append('Replication')
    else:
        xlis.append('Extension')

ylis = lis[:7]+lise[:7]

ax1.scatter(xlis, ylis,c='khaki')
for i in range(7):
    ax1.plot(['Replication','Extension'], [lis[i],lise[i]], color='gray',lw=0.5, zorder=-1)
ylis = lis[-7:]+lise[-7:]
ax2.scatter(xlis, ylis,c='palegreen')
for i in range(7):
    ax2.plot(['Replication','Extension'], [lis[7+i],lise[14+i]], color='gray',lw=0.5, zorder=-1)

fig.suptitle('Reaction Time Comparision')
ax1.set_title('Limited Time - 400 ms')
ax2.set_title('Unlimited Time')

plt.savefig('Figure3.png')

