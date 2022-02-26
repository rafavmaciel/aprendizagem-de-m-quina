import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


le = preprocessing.LabelEncoder()
data = pd.read_csv("car.data")
data.columns.tolist()
data.rename(columns= {'0':'buying', '1':'maint', '2':'doors', '3':'persons',
                      '4':'lug_boot', '5':'safety', '6':'class'},inplace=True)
y = data['class']
x = data.iloc[:,:6]
x = x.apply(le.fit_transform)

k_range = range(1,101)
scores_list= []

for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(x,y, test_size = 0.5, random_state = k,stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))