# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 23:14:26 2021

@author: rafav
"""

import pandas as pd
import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import SGD
from matplotlib import pyplot as plt
from IPython.display import clear_output

#classe de plot
class PlotLearning(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.acc = []
        self.val_acc = []
        self.fig = plt.figure()
        
        self.logs = []

class PlotLosses(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        
        self.fig = plt.figure()
        
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.i += 1
        
        clear_output(wait=True)
        plt.plot(self.x, self.losses, label="loss")
        plt.plot(self.x, self.val_losses, label="val_loss")
        plt.legend()
        plt.show();
        
plot_losses = PlotLosses()

##### rede neural


data = pd.read_csv("spirall.csv", delimiter=",", header=None)
dataset = data.to_numpy()

X = dataset[:,0:2].astype(float)
y = dataset[:,2]
acuracy_list= []

encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
bin_y = np_utils.to_categorical(encoded_Y)
X_train,X_test,y_train,y_test = train_test_split(X,bin_y, test_size = 0.7, random_state = 2)


model=Sequential()
model.add(Dense(4, input_dim=2, activation="sigmoid"))
model.add(Dense(4, activation="sigmoid"))
model.add(Dense(4, activation="sigmoid"))
model.add(Dense(3, activation="softmax"))
opt = SGD(learning_rate=0.3)
model.compile(optimizer=opt,loss="categorical_crossentropy",metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=50,batch_size = 10, validation_data=(X_test, y_test), callbacks=[plot_losses])


#  "Accuracy"
