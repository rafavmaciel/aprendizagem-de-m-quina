import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import SGD
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

le = preprocessing.LabelEncoder()
data = pd.read_csv("wine.data", delimiter=",", header=None)
dataset = data.to_numpy()
result = []

X = dataset[:,1:14].astype(float)
y = dataset[:,0]

# one hot encode input variables
onehot_encoder = OneHotEncoder(sparse=False)
X_proc = onehot_encoder.fit_transform(X)
# ordinal encode target variable


X_train, X_test, y_train, y_test = train_test_split(X_proc,y,test_size=0.3, random_state=1)

clf1= MLPClassifier( max_iter=500,learning_rate_init=0.3,verbose=0,hidden_layer_sizes=(10,),activation='logistic').fit(X_train, y_train)
y_pred1=clf1.predict(X_test)
result.append(accuracy_score(y_test,y_pred1)*100)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=2)

clf1= MLPClassifier( max_iter=500,learning_rate_init=0.3,verbose=0,hidden_layer_sizes=(10,),activation='logistic').fit(X_train, y_train)
y_pred1=clf1.predict(X_test)
result.append(accuracy_score(y_test,y_pred1)*100)
