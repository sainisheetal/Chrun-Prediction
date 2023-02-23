from User import add_entry, User, get_all_entries, get_entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Modify to be used on the deployed DB !!!
      
def get_all_Users(db_path : str) -> list:
    """_summary_

    Args:
        db_path (str): _description_

    Returns:
        list: _description_
        
    Description:
        This function is used to get all the entries from our database as a list of User.
        The db_path argument contain the path to the database.
        It then return a list of User containing all the users informations from the database.
    """
    try:
        engine = create_engine("sqlite:///" + db_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        users = get_all_entries(session)
        session.close()
        return users
    except Exception as e:
        print(e)
        return None
    
def get_one_User(client_number : int, db_path : str) -> User:
    """_summary_

    Args:
        client_number (int): _description_
        db_path (str): _description_

    Returns:
        User: _description_
        
    Description:
        This function get a user in the database by his client number.
        The db_path argument contain the path to the database.
        It then return a User variable that contain the information from the user that has the same client number has the one in the arguments.
    """
    try:
        engine = create_engine("sqlite:///" + db_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        user = get_entry(client_number, session)
        session.close()
        return user
    except Exception as e:
        print(e)
        return None

def add_one_User(user : User, db_path : str):
    """_summary_

    Args:
        user (User): _description_
        db_path (str): _description_
    
    Description:
        This function add a User to the database using a User variable.
        The user variable contain the User that is going to be added to the database
        The db_path argument contain the path to the database.
    """
    try:
        engine = create_engine("sqlite:///" + db_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        add_entry(user, session)
        session.close()
    except Exception as e:
        print(e)
        
def add_multiple_User(users : list, db_path : str):
    """_summary_

    Args:
        users (list): _description_
        db_path (str): _description_
        
    Description:
        This function add multiple User to the database using a list of User.
        The users variable contain the list of User that are going to be added to the database
        The db_path argument contain the path to the database.
    """
    try:
        engine = create_engine("sqlite:///" + db_path)
        Session = sessionmaker(bind=engine)
        session = Session()
        for user in users:
            add_entry(user, session)
        session.close()
    except Exception as e:
        print(e)