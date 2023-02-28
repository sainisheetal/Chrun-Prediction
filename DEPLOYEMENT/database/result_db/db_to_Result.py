from Result import add_entry, Result, get_all_entries, get_entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
      
def get_all_Results(db_path : str) -> list:
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
        results = get_all_entries(session)
        session.close()
        return results
    except Exception as e:
        print(e)
        return None
    
def get_one_Result(id : int, db_path : str) -> Result:
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
        result = get_entry(id, session)
        session.close()
        return result
    except Exception as e:
        print(e)
        return None

def add_one_Result(result : Result, db_path : str):
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
        add_entry(result, session)
        session.close()
    except Exception as e:
        print(e)
        
def add_multiple_Result(results : list, db_path : str):
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
        for result in results:
            add_entry(result, session)
        session.close()
    except Exception as e:
        print(e)