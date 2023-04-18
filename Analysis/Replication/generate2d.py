import pandas
import csv
import numpy
from sklearn import linear_model
import matplotlib.pyplot as plt

i = 1
row_reward_unlim=[]
row_reward_lim400=[]

while(i<15):
    csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=["Choice","Reward","Time Condition","Payoff Condition"])
    data_list = csvFile.T.values.tolist()
    
    j = 1
    while (j<320):
        if(data_list[2][j-1] == 'Unlimited Time'):
            if (data_list[0][j] == data_list[0][j-1]):
                entry=[1, data_list[1][j-1]]
                row_reward_unlim.append(entry)
            else:
                entry=[0, data_list[1][j-1]]
                row_reward_unlim.append(entry)
                
        elif(data_list[2][j-1] == 'Limited Time'):
             if (data_list[0][j] == data_list[0][j-1]):
                entry=[1, data_list[1][j-1]]
                row_reward_lim400.append(entry)
             else:
                entry=[0, data_list[1][j-1]]
                row_reward_lim400.append(entry)
            
        j = j + 1
    
    i = i + 1

X_lim400 = []
Y_lim400 = []
iterator_1 = 0
while(iterator_1 < len(row_reward_lim400)):
    X_lim400.append(row_reward_lim400[iterator_1][1])
    Y_lim400.append(row_reward_lim400[iterator_1][0])
    iterator_1 = iterator_1 + 1

X_unlim = []
Y_unlim = []
iterator = 0
while(iterator < len(row_reward_unlim)):
    X_unlim.append(row_reward_unlim[iterator][1])
    Y_unlim.append(row_reward_unlim[iterator][0])
    iterator = iterator + 1

X_unlim = numpy.array(X_unlim).reshape(-1,1)
Y_unlim = numpy.array(Y_unlim)

X_lim400 = numpy.array(X_lim400).reshape(-1,1)
Y_lim400 = numpy.array(Y_lim400)


logr = linear_model.LogisticRegression()
logr.fit(X_unlim, Y_unlim)

def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

x = numpy.arange(0,100)

logr_lim400 = linear_model.LogisticRegression()
logr_lim400.fit(X_lim400, Y_lim400)


y_lim400= logit2prob(logr_lim400, x)
y_unlim = logit2prob(logr, x)


plt.scatter(x, y_unlim, label="unlimited time",color= "palegreen", 
            marker= "*", s=10)
plt.scatter(x, y_lim400, label="limited time-400ms", color= "khaki", 
            marker= ".", s=10)
  
# x-axis label
plt.xlabel('Previous Reward')
# frequency label
plt.ylabel('Probability')
# plot title
plt.title('Repeat Response Curve')
# showing legend
plt.legend()
  
# function to show the plot
plt.savefig('Figure2d.png')

