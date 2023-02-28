from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Result(Base):
    """_summary_

    Args:
        Base (_type_): _description_

    Returns:
        _type_: _description_
        
    Description : 
        This is the class that is used to generate the table of our database. It also implement the basic manipulation on the table.
    """
    __tablename__ = "result"
    
    id = Column("Id", Integer, primary_key=True)
    client_number = Column("CLIENTNUM", Integer, nullable=True)
    total_relationship_count = Column("Total_Relationship_Count", Integer, nullable=False)
    months_inactive = Column("Months_Inactive_12_mon", Integer, nullable=False)
    contacts_count = Column("Contacts_Count_12_mon", Integer, nullable=False)
    total_revolving_bal = Column("Total_Revolving_Bal", Integer, nullable=False)
    total_amt_chng = Column("Total_Amt_Chng_Q4_Q1", Float, nullable=False)
    total_trans_amt = Column("Total_Trans_Amt", Integer, nullable=False)
    total_trans_ct = Column("Total_Trans_Ct", Integer, nullable=False)
    total_ct_chng = Column("Total_Ct_Chng_Q4_Q1", Float, nullable=False)
    avg_utilization_ratio = Column("Avg_Utilization_Ratio", Float, nullable=False)
    prediction_result = Column("Prediction_result", Boolean, nullable=False)
    client_value = Column("Client_value", Float, nullable=True)
    
    def __init__(self, total_relationship_count : int,
                 months_inactive : int, contacts_count : int, total_revolving_bal : int,
                 total_amt_chng : float, total_trans_amt : int, total_trans_ct : int,
                 total_ct_chng : float, avg_utilization_ratio : float, prediction_result : bool, client_number : int = None,
                 client_value : float = None):
        self.client_number = client_number
        self.total_relationship_count = total_relationship_count
        self.months_inactive = months_inactive
        self.contacts_count = contacts_count
        self.total_revolving_bal = total_revolving_bal
        self.total_amt_chng = total_amt_chng
        self.total_trans_amt = total_trans_amt
        self.total_trans_ct = total_trans_ct
        self.total_ct_chng = total_ct_chng
        self.avg_utilization_ratio = avg_utilization_ratio
        self.prediction_result = prediction_result
        self.client_value = client_value
        
    def __repr__(self) -> str:
        return f"{self.client_number},{self.total_relationship_count},{self.months_inactive},{self.contacts_count},{self.total_revolving_bal},{self.total_amt_chng},{self.total_trans_amt},{self.total_trans_ct},{self.total_ct_chng},{self.avg_utilization_ratio},{self.prediction_result},{self.client_value}"
    
def add_entry(user : Result, session : Session):
    """_summary_

    Args:
        user (User): _description_
        session (Session): _description_
        
    Description:
        Add an entry to the database using the session.
    """
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        print(e)
    
def get_all_entries(session : Session) -> list:
    """_summary_

    Args:
        session (Session): _description_

    Returns:
        list: _description_
        
    Description:
        Get all the entries of the database
    """
    try:
        users = session.query(Result).all()
    except Exception as e:
        print(e)
        return None
    return users

def get_entry(id : int, session : Session) -> Result:
    """_summary_

    Args:
        client_number (int): _description_
        session (Session): _description_

    Returns:
        User: _description_
        
    Description:
        Get an entry depending on the client number given in argument.
    """
    try:
        user = session.query(Result).filter(Result.id == id)
    except Exception as e:
        print(e)
        return None
    return user