# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:05:45 2021

@author: rafav
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score  
from sklearn import metrics,preprocessing,model_selection    
from sklearn.preprocessing import KBinsDiscretizer


le = preprocessing.LabelEncoder()

X,y = load_iris(return_X_y = True)
X = pd.DataFrame(X)
categoricos = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
X = categoricos.fit_transform(X)
k_range = range(1,101)
scores_list= []

for i in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state = i, stratify= y)
        tree =DecisionTreeClassifier(criterion='entropy')
        tree.fit(X_train,y_train)
        predict = tree.predict(X_test)
        score = tree.score(X_test,y_test)
        scores_list.append(score)