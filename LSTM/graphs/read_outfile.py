import math
import numpy as np
import sys
print("Inflow(Cs),")
f=np.load('outfile.npz')
x=sys.argv[1]
for item in f[x+'PredictPlot']:
    if not math.isnan(item):
        print(item[0],",")
