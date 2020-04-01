import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
import math
month=11#int(input("enter the month number: "))-1
year=2017#int(input("enter year"))
X_t= 6401#int(input("inflow data: "))
number_of_months=20*12#int(input("Enter the number of months for which you want predictions"))
#mean
u=[5563.75, 5626.2, 7415.4, 10994.6, 21938.45, 32920.2,	45904.45, 48152.7, 27123.6, 12069.42, 7652.368,	6191.368]
month_name=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
#standard deviation
sd=[766.457, 922.113, 1793.752,	2550.227, 5808.079, 8193.273, 8201.919,	8091.542, 5783.090, 1897.098, 991.837, 653.419]
print("Month,Year,Inflow")
np.random.seed(9001)
#lag -1 correlation
lag=[0.227655, 0.551696, 0.401201485, 0.605124717, 0.491461791,	0.410272397, 0.399201027, 0.389443329, 0.472289721, 0.700926754, 0.85389162, 0.742986236]
entry=[]
for i in range(number_of_months):
    rn=np.random.normal(0,1,1)[0]
    z_t=(X_t-u[month])/sd[month]
    z_t1=lag[month]*z_t+rn*math.sqrt(1-lag[month]*lag[month])
    X_t1=u[(month+1)%12]+z_t1*sd[(month+1)%12]
    if(month==11):
        year=year+1
    month=(month+1)%12
    #print(month_name[month],",",year,",",X_t1)
    X_t=X_t1
    entry.append({'month':month_name[month],'year':year,'inflow':X_t})
month_dict={}
for items in entry:
    if items['month'] in month_dict:
        month_dict[items['month']]['year'].append(items['year'])
        month_dict[items['month']]['inflow'].append(items['inflow'])
    else:
        month_dict[items['month']]={'year':[items['year']],'inflow':[items['inflow']]}


# These are the colors that will be used in the plot
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']


fig, ax = plt.subplots(1, 1, figsize=(12, 14))

# Remove the plot frame lines. They are unnecessary here.
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

fig.subplots_adjust(left=.06, right=.75, bottom=.02, top=.94)
ax.set_xlim(1969.5, 2011.1)
ax.set_ylim(-0.25, 90)

plt.xticks(range(1970, 2011, 10), fontsize=14)
plt.yticks(range(0, 91, 10), fontsize=14)
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))


plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)
majors = month_name

y_offsets = {}
"""'Foreign Languages': 0.5, 'English': -0.5,
             'Communications\nand Journalism': 0.75,
             'Art and Performance': -0.25, 'Agriculture': 1.25,
             'Social Sciences and History': 0.25, 'Business': -0.75,
             'Math and Statistics': 0.75, 'Architecture': -0.75,
             'Computer Science': 0.75, 'Engineering': -0.25}
"""
for rank, column in enumerate(majors):
    column_rec_name = column.replace('\n', '_').replace(' ', '_')

    line = plt.plot(month_dict[month_name[i]]['year'],month_dict[month_name[i]]['inflow'],
                    lw=2.5,
                    color=color_sequence[rank])
    y_pos = month_dict[month_name[i]]['inflow'] - 0.5

    if column in y_offsets:
        y_pos += y_offsets[column]
    plt.text(2011.5, y_pos, column, fontsize=14, color=color_sequence[rank])
fig.suptitle('Month wise thomas fiering model prediction for 20 years', fontsize=18, ha='center')

plt.show()
