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
    print(int(log[char2]+log[mantissa]),"Volume in Reservoir 1000 acre feet")
else:
    print(int(log[char2]),"1000 acre feet")
inflow=int(input("please enter your inflow in 1000 acre feet"))
release=int(input("please enter yout release in 1000 acre feet"))
currentvolume=int(log[char2])+inflow-release
if foundfloat and y[1]!='0':
    currentvolume+=int(log[mantissa])+inflow-release


#module to convert volume back to closest elevation
diff=abs(currentvolume-df.loc[0][1])
index=0
char=1
mantissa=-1
for i in range(len(df)):
    for j in range(10):
        if(abs(df.loc[i][j+1]-currentvolume)<diff):
            diff,index,char,mantissa=abs(df.loc[i][j+1]-currentvolume),i,j+1,-1
        for k in range(9):
            if(abs(df.loc[i][j+1]+df.loc[i][k+11]-currentvolume)<diff):
                diff,index,char,mantissa=abs(df.loc[i][j+1]+df.loc[i][k+11]-currentvolume),i,j+1,k+1



newelevation=str(10*int(int(df.loc[index][0])/10)+char-1)
if mantissa!=-1:
    newelevation=newelevation+'.'+str(mantissa)

print(newelevation, "feet")
