import pandas as pd
from sklearn import metrics,preprocessing,model_selection
       

proc = preprocessing.LabelEncoder()
data = pd.read_csv("forestfires.csv", )
