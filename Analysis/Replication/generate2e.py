import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

i = 1

while(i<16):
  csvFile = pandas.read_csv('./dataneeded/Participant_'+str(i)+'.csv',usecols=['Payoff Condition','Time Condition','Reward','One value','Two value','Three value','Four value'], na_filter= False)
  df = csvFile.values.tolist()
  for k in range(len(df)):
    df[k].append('')

  for j in range(len(df)):
    if df[j][0] == 0.0:
      df[j][7] = np.nan
    elif df[j][0] == round(df[j][3],1):
      df[j][7] = 'q'
    elif df[j][0] == round(df[j][4],1):
      df[j][7] = 'w'
    elif df[j][0] == round(df[j][5],1):
      df[j][7] = 'o'
    elif df[j][0] == round(df[j][6],1):
      df[j][7] = 'p'

  datay = pandas.DataFrame(df)
  datay = datay.dropna()

  datay.rename(columns={0: 'Reward', 1: 'Time', 2: 'Payoff', 3:'One', 4:'Two', 5:'Three', 6:'Four', 7:'Real'}, inplace = True)
  dfreq = datay.groupby(['Payoff', 'Time', 'Real']).agg(n=('Real', 'count'))
  dfreq = dfreq.reset_index()
  dfreq['prop'] = dfreq['n'] / 40
  dfreq['random'] = 0.25
  i = i + 1

dfreq['p_value'] = dfreq['prop'] - dfreq['random']

fig, axs = plt.subplots(1, 4, figsize=(20, 5))

payoff_order = ['i', 'l', 'h', 'e']

real_order = ['q', 'w', 'o', 'p']

colors = {'Limited Time': 'khaki', 'Unlimited Time': 'palegreen'}
color_labels = {'khaki': 'Limited Time', 'palegreen': 'Unlimited Time'}

legend_patches = [Patch(color=k, label=v) for k,v in color_labels.items()]

for i, ax in enumerate(axs):

    payoff = payoff_order[i]
    df_payoff = dfreq[dfreq['Payoff'] == payoff]

    for j, real in enumerate(real_order):
        
        df_real = df_payoff[df_payoff['Real'] == real]
        
        for k, time in enumerate(['Unlimited Time', 'Limited Time']):

            df_time = df_real[df_real['Time'] == time]
            
            bar_height = df_time['p_value'].values
            bar_color = colors[time]
            
            ax.bar(j + k * 0.4, bar_height, width=0.4, color=bar_color, edgecolor = 'black')
    
    ax.set_title(f"Payoff: {payoff}")

    ax.set_xticks([0.2,1.2,2.2,3.2])
    ax.set_xticklabels(real_order)
    ax.set_ylabel('p(choice)-p(chance)')
    ax.axhline(y=0, color= 'black', linewidth=1)
    ax.legend(handles=legend_patches)

plt.savefig('Figure2e.png')