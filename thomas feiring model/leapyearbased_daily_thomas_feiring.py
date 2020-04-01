#thomas feiring model 
import math
import numpy as np
import pandas as pd
#enter the year for which you need prediction starting 2019
def leap_year(year):
    if (year%400==0):
        return True
    elif (year%100==0):
        return False
    elif (year%4==0):
        return True
    else:
        return False
def increment_year(year):
    if(leap_year(year)):
        return 366
    else:
        return 365
year=2019
number_of_years=2
number_of_days=0
day=1
df = pd.read_csv('groundtruth.csv')
u=df['Mean']
X_t= u[0]
sd=df['St dev']

#lag -1 correlation
lag=df['co relation']
np.random.seed(9001)
for j in range(number_of_years):
    number_of_days+=increment_year(year+j)
print("total number of days",number_of_days,",,")
print("Day,Year,Inflow")
for i in range(number_of_days):
    rn=np.random.normal(0,1,1)[0]
    z_t=(X_t-u[day-1])/sd[day-1]
    z_t1=lag[day-1]*z_t+rn*math.sqrt(1-lag[day-1]*lag[day-1])
    X_t1=u[day%366]+z_t1*sd[day%366]
    print(day,",",year,",",X_t1)
    if(day==increment_year(year)):
        year=year+1
        day=0
    day=day+1
    X_t=X_t1
