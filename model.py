from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import joblib 

dataset=load_iris()
data=pd.DataFrame(dataset['data'],columns=["Petal length","Petal Width","Sepal Length","Sepal Width"])

data['Species']=dataset['target']
data['Species']=data['Species'].apply(lambda x: dataset['target_names'][x])

x = data.drop(['Species'], axis = 1)
y = data['Species']

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(x, y)