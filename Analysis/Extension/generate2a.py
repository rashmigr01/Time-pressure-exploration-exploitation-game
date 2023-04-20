import pandas as pd
import matplotlib.pyplot as plt

df = pd.concat([pd.read_csv('./dataneeded/Participant_'+str(i)+'.csv') for i in range(1,16)], ignore_index=True)

df['Unshifted Reward'] = df['Reward (Health Points)']-df['Mean Shift']

ddt = df.groupby(['Time Condition', 'Payoff Condition', 'Trial Number'])['Unshifted Reward'].agg(['mean', 'sem']).reset_index()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8), sharex=True, sharey=True)
colors = ['khaki', 'skyblue', 'palegreen']

for i, (pc, pc_group) in enumerate(ddt.groupby('Payoff Condition')):
    row = i // 2
    col = i % 2
    ax = axes[row, col]
    ax.set_title(str(pc))
    ax.set_xlabel('Trials')
    ax.set_ylabel('Performance ± SE')
    for j, (tc, tc_group) in enumerate(pc_group.groupby('Time Condition')):
        x = tc_group['Trial Number']
        y = tc_group['mean']
        y_err = tc_group['sem']
        ax.plot(x, y, label=str(tc), color=colors[j])
        ax.fill_between(x, y - y_err, y + y_err, alpha=0.5, color=colors[j])
        
        # Formatting for each subplot
        for spine in ax.spines.values():
            spine.set_visible(True)
        ax.tick_params(top=True, right=True)
        ax.spines['right'].set_linewidth(1.5)
        ax.spines['top'].set_linewidth(1.5)

    ax.legend(loc='lower right')

plt.savefig('Figure2a.png')
