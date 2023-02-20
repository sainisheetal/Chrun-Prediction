import pandas as pd
from User import add_entry, User, get_all_entries, get_entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def fill():
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
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    users = get_all_entries(session)
    session.close()
    return users

    
def get_one(client_number : int) -> User:
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    user = get_entry(client_number, session)
    return user

def add_one(user : User):
    engine = create_engine("sqlite:///DEPLOYEMENT/BankChurners.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    add_entry(user, session)
    session.close()