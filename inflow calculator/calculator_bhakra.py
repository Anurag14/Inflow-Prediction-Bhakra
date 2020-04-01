import pandas as pd
df=pd.read_csv('data 1.csv')
x=input("Enter the number ")
foundfloat=False
for item in x:
    if item == '.':
        y=x.split('.')
        foundfloat=True
        break
if foundfloat:
    if y[1]!='0':
        mantissa=y[1]+".1"
else:
    y=[x]
char1=10*int(int(y[0])/10)
char2=str(int(y[0])%10)
log=df.loc[df['elevation']==char1]
if foundfloat and y[1]!='0':
    print(log[char2]+log[mantissa],"1000 acre feet")
else:
    print(log[char2],"1000 acre feet")
