from keras.utils.vis_utils import model_to_dot
import numpy as np
from keras.models import load_model
from keras.utils.vis_utils import plot_model
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
# fix random seed for reproducibility
np.random.seed(7)
# load the dataset
dataframe = read_csv('../data1.csv', usecols=[2], engine='python', skipfooter=3)
dataset = dataframe.values
dataset = dataset.astype('float32')
# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
path=input("what is type of model you wish to load?")
model=load_model("../weights/"+path+".h5")
print(model.summary())
print("plotting model")
plot_model(model, to_file='../model_plot/'+path+'.png', show_shapes=True, show_layer_names=True)
#SVG(model_to_dot(model).create(prog='dot', format='svg'))
model.reset_states()
print("model plotted")
batch_size=int(input("Enter batch size"))
look_back=3
data=[]
for items in dataset[-look_back:]:
    data.append(items[0])
ndataset=[]
for i in range(batch_size):
    ndataset.append(data)
print("ndataset shape: ",np.array(ndataset).shape)
trainX=np.reshape(np.array(ndataset),(batch_size,look_back,1))
months=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(sum(months[:4])):
    trainPredict = model.predict(trainX)
    dataset[0][-1]=trainPredict[0][0]
    print(scaler.inverse_transform(dataset)[0][-1],",")
    ndataset[0]=ndataset[0][1:]
    ndataset[0].append(trainPredict[0][0])
    trainX=np.reshape(np.array(ndataset),(batch_size,look_back,1))
