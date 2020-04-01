import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('../data1.csv',usecols=[0],engine='python', skipfooter=3)
dates=df.values
f=np.load('outfile.npz')
#seaborn styling 
sns.set_style('darkgrid')

#plot for the time and predictions of inflow 
line1,=plt.plot(dates,f['dataset'])
line2,=plt.plot(dates,f['trainPredictPlot'])
line3,=plt.plot(dates,f['testPredictPlot'])
plt.legend((line1, line2, line3), ('Dataset timeseries', 'Train timeseries', 'Test timeseries'))
plt.show()
