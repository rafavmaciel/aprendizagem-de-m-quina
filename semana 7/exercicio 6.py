# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:54:50 2021

@author: rafav
"""

import pandas as pd
from sklearn import metrics,preprocessing,model_selection
from sklearn.impute import SimpleImputer    
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from pandas import DataFrame,Series
import scipy as sp                                                         
import scipy.stats            
le = preprocessing.LabelEncoder()
proc = preprocessing.LabelEncoder()
data = pd.read_csv("processed.hungarian.data", )
y = data['class']
x = data.iloc[:,:13]

#verificando quantidade de campos faltando
x.loc[x['slope']=="?"]
x.loc[x['ca']=="?"]
x.loc[x['thal']=="?"]

x.drop(['slope','ca','thal'],axis=1, inplace=True)


X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = 1, stratify=y)
imp1 = SimpleImputer(missing_values="?",strategy="most_frequent")
knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
X_train = imp1.fit_transform(X_train)
X_train =pd.DataFrame(X_train)
X_train = X_train.apply(le.fit_transform)
knn.fit(X_train, y_train)

X_test = imp1.fit_transform(X_test)
X_test =pd.DataFrame(X_test)
X_test = X_test.apply(le.fit_transform)
y_pred = knn.predict(X_test)
score = metrics.accuracy_score(y_test,y_pred)
