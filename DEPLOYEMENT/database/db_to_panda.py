from sqlite3 import connect
import pandas as pd
from User import User, add_entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Modify to be used on the deployed DB !!!

def create_panda_frame(querry) -> pd.DataFrame:
    """_summary_

    Args:
        querry (_type_): _description_

    Returns:
        pd.DataFrame: _description_
        
    Description:
        This function take the result of a sql querry and transform it in a panda dataframe.
    """
    return pd.DataFrame(querry, columns=["CLIENTNUM", "Attrition_Flag", "Customer_Age",
                                         "Gender", "Dependent_count", "Education_Level",
                                         "Marital_Status", "Income_Category", "Card_Category",
                                         "Months_on_book", "Total_Relationship_Count", "Months_Inactive_12_mon",
                                         "Contacts_Count_12_mon", "Credit_Limit", "Total_Revolving_Bal",
                                         "Avg_Open_To_Buy", "Total_Amt_Chng_Q4_Q1", "Total_Trans_Amt",
                                         "Total_Trans_Ct", "Total_Ct_Chng_Q4_Q1", "Avg_Utilization_Ratio",
                                         "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
                                         "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"])

def get_all_panda(db_path : str) -> pd.DataFrame:
    """_summary_

    Args:
        db_path (str): _description_

    Returns:
        pd.DataFrame: _description_
        
    Description:
        This function get all the entries from the database and put them in a panda dataframe.
        The path to the database is specified in the db_path argument.
    """
    try:
        conn = connect(db_path)
        querry = pd.read_sql_query("SELECT * FROM user", conn)
        return create_panda_frame(querry)
    except Exception as e:
        print(e)
        return None
    
def get_one_panda(client_number : int, db_path : str) -> pd.DataFrame:
    """_summary_

    Args:
        client_number (int): _description_
        db_path (str): _description_

    Returns:
        pd.DataFrame: _description_
        
    Description:
        This function get one entry from the database based on a client number and return it in a panda dataframe.
        The client_number argument contain the client number of the client we want.
        The path to the database is specified in the db_path argument.
        
    """
    try:
        conn = connect(db_path)
        querry = pd.read_sql_query(f"SELECT * FROM user WHERE CLIENTNUM = {client_number}", conn)
        return create_panda_frame(querry)
    except Exception as e:
        print(e)
        return None
    
def add_panda(df : pd.DataFrame, db_path : str):
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        db_path (str): _description_
        
    Description:
        This function take a panda dataframe as an argument and store all its row as entries in the database.
        The path to the database is specified in the db_path argument.
    """
    try:
        engine = create_engine("sqlite:///" + db_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        for row in df.iterrows():
            user = User(row[1][0], row[1][1], row[1][2], row[1][3], row[1][4],
                        row[1][5], row[1][6], row[1][7], row[1][8], row[1][9],
                        row[1][10], row[1][11], row[1][12], row[1][13], row[1][14],
                        row[1][15], row[1][16], row[1][17], row[1][18], row[1][19],
                        row[1][20], row[1][21], row[1][22])
            add_entry(user, session)
        session.close()
    except Exception as e:
        print(e)