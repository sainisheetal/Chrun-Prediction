import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

df = pd.read_csv("PreProBankChurners.csv")

x = df.iloc[:, [2,3,5,6,7]].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

with open ('model.pickle', 'wb') as file:
    pickle.dump(model,file)

