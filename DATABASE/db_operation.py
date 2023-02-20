import pandas as pd
from User import add_entry, User, get_all_entries, get_entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def fill():
    """
    Description:
        This function is used to populate our database with the datas from the BankChurners.csv file
    """
    df = pd.read_csv("./data/BankChurners.csv")
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db", echo=True)
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
        
def get_all() -> list:
    """_summary_

    Returns:
        list: _description_
        
    Description:
        This function is used to get all the entries from our database as a list of User.
    """
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    users = get_all_entries(session)
    session.close()
    return users

#def get_all_in_dataframe() -> pd.DataFrame:

    
def get_one(client_number : int) -> User:
    """_summary_

    Args:
        client_number (int): _description_

    Returns:
        User: _description_
        
    Description:
        This function get a user in the database that has the same client number as the one in the arguments.
    """
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    user = get_entry(client_number, session)
    return user

#def get_one_in_dataframe() -> pd.DataFrame:

def add_one(user : User):
    """_summary_

    Args:
        user (User): _description_
        
    Description:
        This function add a User to the database.
    """
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    add_entry(user, session)
    session.close()