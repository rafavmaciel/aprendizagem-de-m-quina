# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:04:01 2021

@author: rafav
"""

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp                                                         
import scipy.stats         

X,y = load_wine(return_X_y = True)
k_range = range(1,101)
k3_range = range(1,101)
scores_1knn= []
scores_3knn= []
diferenca=[]


for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_1knn.append(metrics.accuracy_score(y_test,y_pred))

for x in k3_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = x)
    knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean',weights='distance')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_3knn.append(metrics.accuracy_score(y_test,y_pred))

#calculando diferença    
for i in range(len(scores_1knn)):
    dif = scores_3knn[i] - scores_1knn[i]
    diferenca.append(dif)
    
    
#intervalo de confiamça da diferença    
media_dif = np.mean(diferenca)
desvio_padrao_dif = np.std(diferenca)
intervalo_conf_dif = scipy.stats.norm.interval(0.95, loc=media_dif, scale=desvio_padrao_dif) 

#intervalo de confiamça de 1 knn   
media_1knn = np.mean(scores_1knn)
desvio_padrao_1knn = np.std(scores_1knn)
intervalo_conf_1knn = scipy.stats.norm.interval(0.95, loc=media_1knn, scale=desvio_padrao_1knn)

#intervalo de confiamça de 3 knn com peso  
media_3knn = np.mean(scores_3knn)
desvio_padrao_3knn = np.std(scores_3knn)
intervalo_conf_3knn = scipy.stats.norm.interval(0.95, loc=media_3knn, scale=desvio_padrao_3knn)

