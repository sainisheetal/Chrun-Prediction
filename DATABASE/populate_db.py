import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from User import add_entry, User

def fill(csv_path : str, db_path : str):
    """_summary_

    Args:
        csv_path (str): _description_
        db_path (str): _description_
        
    Description:
        This function is used to populate our database with the datas from the BankChurners.csv file.
        the csv_path argument contain the path to the BankChurners.csv file that is going to be pushed on the database.
        The db_path argument contain the path to the database.
        DO NOT USE AGAIN EXCEPT IF YOU LOSE THE DATABASE !!!
    """
    try:
        df = pd.read_csv(csv_path)
        engine = create_engine("sqlite:///" + db_path, echo=True)
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