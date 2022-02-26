# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:43:45 2021

@author: rafav
"""

import pandas as pd
from sklearn import metrics,preprocessing,model_selection
from sklearn.impute import SimpleImputer    
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from pandas import DataFrame,Series
import scipy as sp                                                         
import scipy.stats            
le = preprocessing.LabelEncoder()
proc = preprocessing.LabelEncoder()
data = pd.read_csv("adult.data", )
y = data['class']
x = data.iloc[:,:14]

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = 1,stratify = y)
imp1 = SimpleImputer(missing_values=" ?",strategy="most_frequent")
tree =DecisionTreeClassifier(criterion='entropy')

X_train = imp1.fit_transform(X_train)
X_train =pd.DataFrame(X_train)
X_train = X_train.apply(le.fit_transform)

tree.fit(X_train,y_train)

X_test = imp1.fit_transform(X_test)
X_test =pd.DataFrame(X_test)
X_test = X_test.apply(le.fit_transform)

predict = tree.predict(X_test)

score = tree.score(X_test,y_test)
