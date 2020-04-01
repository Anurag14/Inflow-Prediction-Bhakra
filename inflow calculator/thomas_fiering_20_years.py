#thomas feiring model 
import math
import numpy as np
import matplotlib.pyplot as plt

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

print(month_dict)

plt.style.use('seaborn')
 
# create a color palette
palette = plt.get_cmap('Set1')
fig = plt.figure()
# multiple line plot
num=0
for i in range(len(month_name)):
    plt.plot(month_dict[month_name[i]]['year'],month_dict[month_name[i]]['inflow'],color=palette(num), marker='', label=str(month_name[i]))
    #ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    num+=1
# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("Month wise thomas fiering model prediction for 20 years", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time in Years",fontsize=12)
plt.ylabel("Inflow",fontsize=12)
plt.show()
