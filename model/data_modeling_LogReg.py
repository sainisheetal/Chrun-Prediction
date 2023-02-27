import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("PreProBankChurners.csv")

def training_results(y_train, y_test, train_pred, test_pred) -> list:
    train_mse = mean_squared_error(y_train, train_pred)
    train_r2 = r2_score(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    test_r2 = r2_score(y_test, test_pred)
    return [train_mse, train_r2, test_mse, test_r2]

x = df.iloc[:, [10,11,12,14,16,17,18,19,20]].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)

classifier = LogisticRegression(random_state = 0, max_iter=10000)
classifier.fit(X_train, y_train)

train_pred = classifier.predict(X_train)
test_pred = classifier.predict(X_test)

print ("Accuracy : ", accuracy_score(y_test, test_pred))
print(training_results(y_train, y_test, train_pred, test_pred))