import numpy as np
import os 

def convert_outfile_to_csv(outfile,total_epochs):
    for dataset in outfile.files:
        x=outfile[dataset]
        # no need for ground truth data as it is same for every epoch only test and train predictions may change
        if dataset==outfile.files[-1]: 
            continue
        np.savetxt("csv/"+dataset[:-4]+"_epochs_"+total_epochs+".csv",x,delimiter=',')


filenames = os.listdir("outfile")
for filename in filenames:
    outfile = np.load("outfile/"+filename)
    total_epochs = filename.split('_')[1].split('.')[0] # take number string from outfile_*.npy files
    convert_outfile_to_csv(outfile, total_epochs)
