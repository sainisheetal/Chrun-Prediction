def Attrition_Flag_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform the value from the Attrition_Flag column to a value understandable by the model.
    """
    return {"Existing Customer" : 0,
            "Attrited Customer" : 1}
    
def Attrition_Flag_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Attrition_Flag column.
    """
    return {"0" : "Existing Customer",
            "1" : "Attrited Customer"}
    
def Education_Level_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform the value from the Education_Level column to a value understandable by the model.
    """
    return {"Unknown" : 0,
            "Uneducated" : 1,
            "High School" : 2,
            "College" : 3,
            "Graduate" : 4,
            "Post-Graduate" : 5,
            "Doctorate" : 6}

def Education_Level_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Education_Level column.
    """
    return {"0" : "Unknown",
            "1" : "Uneducated",
            "2" : "High School",
            "3" : "College",
            "4" : "Graduate",
            "5" : "Post-Graduate",
            "6" : "Doctorate"}
    
def Marital_Status_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform the value from the Marital_Status column to a value understandable by the model.
    """
    return {"Unknown" : 0,
            "Single" : 1,
            "Married" : 2,
            "Divorced" : 3}

def Marital_Status_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Marital_Status column.
    """
    return {"0" : "Unknown",
            "1" : "Single",
            "2" : "Married",
            "3" : "Divorced"}
    
def Income_Category_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform the value from the Income_Category column to a value understandable by the model.
    """
    return {"Unknown" : 0,
            "Less than $40K" : 1,
            "$40K - $60K" : 2,
            "$60K - $80K" : 3,
            "$80K - $120K" : 4,
            "$120K +" : 5}
    
def Income_Category_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Income_Category column.
    """
    return {"0" : "Unknown",
            "1" : "Less than $40K",
            "2" : "$40K - $60K",
            "3" : "$60K - $80K",
            "4" : "$80K - $120K",
            "5" : "$120K +"}
    
def Card_Category_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
    
    Description:
        Create a dict to transform the value from the Card_Category column to a value understandable by the model.
    """
    return {"Blue" : 0,
            "Silver" : 1,
            "Gold" : 2,
            "Platinum" : 3}
    
def Card_Category_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Card_Category column.
    """
    return {"0" : "Blue",
            "1" : "Silver",
            "2" : "Gold",
            "3" : "Platinum"}
    
def Gender_str_to_number() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform the value from the Gender column to a value understandable by the model.
    """
    return {"M" : 0,
            "F" : 1}
    
def Gender_number_to_str() -> dict:
    """_summary_

    Returns:
        dict: _description_
        
    Description:
        Create a dict to transform back the value from the Gender column.
    """
    return {"0" : "M",
            "1" : "F"}