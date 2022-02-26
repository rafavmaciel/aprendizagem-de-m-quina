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
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("spiral.csv")
x=data.iloc[:,:2]
y=data['class']



X_train, X_test, y_train, y_test = train_test_split(x,y,stratify=y,test_size=0.3)

clf3= MLPClassifier(max_iter=1500,learning_rate_init=0.20,verbose=0,
                   hidden_layer_sizes=(9,3),activation='logistic').fit(X_train, y_train)


y_pred=clf3.predict(X_test)
result=accuracy_score(y_test,y_pred)*100