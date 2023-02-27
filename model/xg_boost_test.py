import pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
import xgboost as xgb
from sklearn.metrics import classification_report
from xgboost import XGBClassifier


df = pd.read_csv("PreProBankChurners.csv")

cat_cols = list(df.select_dtypes("object"))

for col in cat_cols:
    dummy_cols = pd.get_dummies(df[col], drop_first=True, prefix=col)
    df = pd.concat([df,dummy_cols],axis=1)
    df.drop(columns=col, inplace=True)

y = df.pop("Attrition_Flag")
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=69)

req_cols = ['Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Total_Revolving_Bal',
            'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
            'Avg_Utilization_Ratio']

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train[req_cols])

X_test = scaler.transform(X_test[req_cols])

sm = SMOTE(sampling_strategy = 1.0)

X_train, y_train = sm.fit_resample(X_train, y_train)

xgb_model = XGBClassifier(use_label_encoder=False)

xgb_model.fit(X_train, y_train)

print(xgb_model.score(X_test, y_test))
print(classification_report(y_test, xgb_model.predict(X_test)))