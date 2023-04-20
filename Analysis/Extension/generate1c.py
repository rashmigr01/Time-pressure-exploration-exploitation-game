import pandas
import matplotlib.pyplot as plt

i = 1
rows=[]
q_i = []
w_i = []
o_i = []
p_i = []
q_l = []
w_l = []
o_l = []
p_l = []
q_h = []
w_h = []
o_h = []
p_h = []
q_e = []
w_e = []
o_e = []
p_e = []
while(i<16):
    csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=["Payoff Condition","One value","Two value","Three value","Four value","Mean Shift"])
    data_list = csvFile.T.values.tolist()

    j = 0
    while(j<480):
        if (data_list[0][j] == 'i'):
                q_i.append(data_list[1][j]-data_list[5][j])
                w_i.append(data_list[2][j]-data_list[5][j])
                o_i.append(data_list[3][j]-data_list[5][j])
                p_i.append(data_list[4][j]-data_list[5][j])
        elif (data_list[0][j] == 'l'):
                q_l.append(data_list[1][j]-data_list[5][j])
                w_l.append(data_list[2][j]-data_list[5][j])
                o_l.append(data_list[3][j]-data_list[5][j])
                p_l.append(data_list[4][j]-data_list[5][j])
        elif (data_list[0][j] == 'h'):
                q_h.append(data_list[1][j]-data_list[5][j])
                w_h.append(data_list[2][j]-data_list[5][j])
                o_h.append(data_list[3][j]-data_list[5][j])
                p_h.append(data_list[4][j]-data_list[5][j])
        elif (data_list[0][j] == 'e'):
                q_e.append(data_list[1][j]-data_list[5][j])
                w_e.append(data_list[2][j]-data_list[5][j])
                o_e.append(data_list[3][j]-data_list[5][j])
                p_e.append(data_list[4][j]-data_list[5][j])
        j = j+1
    i=i+1

fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharey=True)

lis = q_i+w_i+o_i+p_i
lis2 = []
colors = []
for i in range(len(lis)):
    if(i<len(lis)/4):
        lis2.append('q')
        colors.append('lightcoral')
    elif(i<len(lis)/2):
        lis2.append('w')
        colors.append('bisque')
    elif(i<3*len(lis)/4):
        lis2.append('o')
        colors.append('palegreen')
    else:
        lis2.append('p')
        colors.append('skyblue')

axs[0, 0].scatter(lis2, lis,c=colors)
axs[0, 0].set_title('IGT condition')

lis = q_h+w_h+o_h+p_h
axs[0, 1].scatter(lis2, lis,c=colors)
axs[0, 1].set_title('High condition')

lis = q_l+w_l+o_l+p_l
axs[1, 0].scatter(lis2, lis,c=colors)
axs[1, 0].set_title('Low condition')

lis = q_e+w_e+o_e+p_e
axs[1, 1].scatter(lis2, lis,c=colors)
axs[1, 1].set_title('Equal condition')

for ax in axs.flat:
    ax.set_ylim(-50, 50)

plt.savefig('Figure1c.png')
