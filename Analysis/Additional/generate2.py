import pandas
import matplotlib.pyplot as plt

i = 1
l1 = []
l2 = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_rep'+str(i)+'.csv',usecols=["Choice","Reward","Time Condition","Payoff Condition"])
    data_list = csvFile.T.values.tolist()
    
    rep_resp_unlim = 0
    rep_resp_lim400 = 0
    
    j = 0
    while (j<320):
        if (data_list[0][j] == data_list[0][j-1]):
            if(data_list[2][j-1] == 'Unlimited Time'):
                rep_resp_unlim = rep_resp_unlim + 1
            elif(data_list[2][j-1] == 'Limited Time'):
                rep_resp_lim400 = rep_resp_lim400 + 1
        j = j + 1
        
    l1.append(rep_resp_lim400/160)
    l2.append(rep_resp_unlim/160)
    i = i + 1

lis = l1+l2
colors = []
for i in range(len(lis)):
    if(i<len(lis)/2):
        colors.append('khaki')
    else:
        colors.append('palegreen')


i = 1
l1e = []
l2e = []
l3e = []

while(i<8):
    csvFile = pandas.read_csv('./dataneeded/Participant_ext'+str(i)+'.csv',usecols=["Choice","Reward (Health Points)","Time Condition","Payoff Condition"])
    data_list = csvFile.T.values.tolist()
    
    rep_resp_unlim = 0
    rep_resp_lim400 = 0
    rep_resp_lim800 = 0
    
    j = 0
    while (j<480):
        if (data_list[0][j] == data_list[0][j-1]):
            if(data_list[2][j-1] == 'Unlimited Time'):
                rep_resp_unlim = rep_resp_unlim + 1
            elif(data_list[2][j-1] == 'Limited Time - 800ms'):
                rep_resp_lim800 = rep_resp_lim800 + 1
            elif(data_list[2][j-1] == 'Limited Time - 400ms'):
                rep_resp_lim400 = rep_resp_lim400 + 1
        j = j + 1
        
    l1e.append(rep_resp_lim400/160)
    l2e.append(rep_resp_lim800/160)
    l3e.append(rep_resp_unlim/160)
    i = i + 1


lise = l1e+l2e+l3e
colorse = []
for i in range(len(lise)):
    if(i<len(lise)/3):
        colorse.append('khaki')
    elif(i<2*len(lise)/3):
        colorse.append('skyblue')
    else:
        colorse.append('palegreen')

ylis = lis+lise
xlis = []
for k in range(7*(3+2)):
    if k<(7*2):
        xlis.append('Replication')
    else:
        xlis.append('Extension')

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

fig.suptitle('Repeat Clicks Comparision')
ax1.set_title('Limited Time - 400 ms')
ax2.set_title('Unlimited Time')

plt.savefig('Figure2.png')

