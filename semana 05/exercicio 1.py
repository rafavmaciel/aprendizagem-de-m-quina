import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp                                                         
import scipy.stats         

X,y = load_iris(return_X_y = True)
k_range = range(1,101)
scores_list= []

for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))
media = np.mean(scores_list)
maximo = np.max(scores_list)
minimo = np.min(scores_list)

plt.title('histograma de taxas de acerto')
plt.xlabel('Taxas de acerto')
plt.ylabel('Frequência Absoluta')
plt.hist(scores_list, 8, rwidth=0.8)
plt.show()

desvio_padrao = np.std(scores_list)
intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale=desvio_padrao)    

#letra d