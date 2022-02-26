import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import SGD


data = pd.read_csv("wine.data", delimiter=",", header=None)
dataset = data.to_numpy()

X = dataset[:,1:3].astype(float)
y = dataset[:,0]

encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
bin_y = np_utils.to_categorical(encoded_Y)

X_train,X_test,y_train,y_test = train_test_split(X,bin_y, test_size = 0.5, random_state = 2)
model=Sequential()
model.add(Dense(20, input_dim=2, activation="sigmoid"))
model.add(Dense(20, activation="sigmoid"))
model.add(Dense(3, activation="softmax"))
model.compile(optimizer='adam',loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(X_train,y_train,epochs=700,batch_size=10)

model.fit(X_train,y_train,epochs=60, verbose=2)
result = model.predict(X_test)
loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
print("Accuracy = {:.2f}".format(accuracy))
