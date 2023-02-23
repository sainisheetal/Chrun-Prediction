import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("PreProBankChurners.csv")

x = df.iloc[:, [2,3,5,6,7]].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print ("Accuracy : ", accuracy_score(y_test, y_pred))