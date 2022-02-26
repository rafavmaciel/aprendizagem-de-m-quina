import pandas as pd
from sklearn import metrics,preprocessing,model_selection
       

proc = preprocessing.LabelEncoder()
data = pd.read_csv("student-mat.csv", sep=";")
transform = data.apply(proc.fit_transform)