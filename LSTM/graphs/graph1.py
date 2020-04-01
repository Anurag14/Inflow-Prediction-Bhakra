import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('../data1.csv')
df=df.values
#time series vs reservoir levels(ft) graph
sns.set_style('darkgrid')
plt.plot(df[:,0],df[:,1],label="")
plt.plot(df[:,0],df[:,2])
plt.xlabel('Time Series')
plt.ylabel('Reservoir Levels(ft)')
plt.title('Dialy Bhakhra Reservoir Levels for past 20 years')
plt.show()
