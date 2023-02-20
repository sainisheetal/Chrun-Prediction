import pandas as pd
from User import add_entry, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

df = pd.read_csv("./data/BankChurners.csv")
engine = create_engine("sqlite:///mydb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

for row in df.iterrows():
    user = User(row['CLIENTNUM'],
                row['Attrition_Flag'],
                row['Customer_Age'],
                row['Gender'],
                row['Dependent_count'],
                row['Education_Level'],
                row['Marital_Status'],
                row['Income_Category'],
                row['Card_Category'],
                row['Months_on_book'],
                row['Total_Relationship_Count'],
                row['Months_Inactive_12_mon'],
                row['Contacts_Count_12_mon'],
                row['Credit_Limit'],
                row['Total_Revolving_Bal'],
                row['Avg_Open_To_Buy'],
                row['Total_Amt_Chng_Q4_Q1'],
                row['Total_Trans_Amt'],
                row['Total_Trans_Ct'],
                row['Total_Ct_Chng_Q4_Q1'],
                row['Avg_Utilization_Ratio'],
                row['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1'],
                row['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'])
    print(user)