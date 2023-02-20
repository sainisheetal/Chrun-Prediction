from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    client_number = Column("CLIENTNUM", Integer, primary_key=True, autoincrement=False)
    attrition_flag = Column("Attrition_Flag", String, nullable=False)
    age = Column("Customer_Age", Integer, nullable=False)
    gender = Column("Gender", CHAR, nullable=False)
    dependent_count = Column("Dependent_count", Integer, nullable=False)
    education_level = Column("Education_Level", String, nullable=False)
    marital_status = Column("Marital_Status", String, nullable=False)
    income_category = Column("Income_Category", String, nullable=False)
    card_category = Column("Card_Category", String, nullable=False)
    months_on_book = Column("Months_on_book", Integer, nullable=False)
    total_relationship_count = Column("Total_Relationship_Count", Integer, nullable=False)
    months_inactive = Column("Months_Inactive_12_mon", Integer, nullable=False)
    contacts_count = Column("Contacts_Count_12_mon", Integer, nullable=False)
    credit_limit = Column("Credit_Limit", Float, nullable=False)
    total_revolving_bal = Column("Total_Revolving_Bal", Integer, nullable=False)
    avg_open_to_buy = Column("Avg_Open_To_Buy", Float, nullable=False)
    total_amt_chng = Column("Total_Amt_Chng_Q4_Q1", Float, nullable=False)
    total_trans_amt = Column("Total_Trans_Amt", Integer, nullable=False)
    total_trans_ct = Column("Total_Trans_Ct", Integer, nullable=False)
    total_ct_chng = Column("Total_Ct_Chng_Q4_Q1", Float, nullable=False)
    avg_utilization_ratio = Column("Avg_Utilization_Ratio", Float, nullable=False)
    NBCFC3CDELMI1 = Column("Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1", Float, nullable=False)
    NBCFC3CDELMI2 = Column("Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2", Float, nullable=False)
    
    def __init__(self, client_number : int,
                 attrition_flag : str, age : int,
                 gender : str, dependent_count : int,
                 education_level : str , marital_status : str,
                 income_category : str, card_category : str,
                 months_on_book : int, total_relationship_count : int,
                 months_inactive : int, contacts_count : int,
                 credit_limit : float, total_revolving_bal : int,
                 avg_open_to_buy : float, total_amt_chng : float,
                 total_trans_amt : int, total_trans_ct : int,
                 total_ct_chng : float, avg_utilization_ratio : float,
                 NBCFC3CDELMI1 : float, NBCFC3CDELMI2 : float):
        self.client_number = client_number
        self.attrition_flag = attrition_flag
        self.age = age
        self.gender = gender
        self.dependent_count = dependent_count
        self.education_level = education_level
        self.marital_status = marital_status
        self.income_category = income_category
        self.card_category = card_category
        self.months_on_book = months_on_book
        self.total_relationship_count = total_relationship_count
        self.months_inactive = months_inactive
        self.contacts_count = contacts_count
        self.credit_limit = credit_limit
        self.total_revolving_bal = total_revolving_bal
        self.avg_open_to_buy = avg_open_to_buy
        self.total_amt_chng = total_amt_chng
        self.total_trans_amt = total_trans_amt
        self.total_trans_ct = total_trans_ct
        self.total_ct_chng = total_ct_chng
        self.avg_utilization_ratio = avg_utilization_ratio
        self.NBCFC3CDELMI1 = NBCFC3CDELMI1
        self.NBCFC3CDELMI2 = NBCFC3CDELMI2
        
    def __repr__(self) -> str:
        return f"({self.client_number},{self.attrition_flag},{self.age},{self.gender},{self.dependent_count},{self.education_level},{self.marital_status},{self.income_category},{self.card_category},{self.months_on_book},{self.total_relationship_count},{self.months_inactive},{self.contacts_count},{self.credit_limit},{self.total_revolving_bal},{self.avg_open_to_buy},{self.total_amt_chng},{self.total_trans_amt},{self.total_trans_ct}
        self.total_ct_chng = total_ct_chng
        self.avg_utilization_ratio = avg_utilization_ratio
        self.NBCFC3CDELMI1 = NBCFC3CDELMI1
        self.NBCFC3CDELMI2 = NBCFC3CDELMI2 )"