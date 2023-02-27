import pandas as pd

def treat_information(result : dict) -> list:
    return_list = []
    
    if result["client_number"] == "":
        return_list.append(None)
    else:
        return_list.append(int(result["client_number"]))
        
    if result["total_relationship_count"] == "":
        return None
    else:
        return_list.append(int(result["total_relationship_count"]))
        
    if result["months_inactive"] == "":
        return None
    else:
        return_list.append(int(result["months_inactive"]))
        
    if result["contacts_count"] == "":
        return None
    else:
        return_list.append(int(result["contacts_count"]))
        
    if result["total_revolving_bal"] == "":
        return None
    else:
        return_list.append(int(result["total_revolving_bal"]))
        
    if result["total_amt_chng"] == "":
        return None
    else:
        return_list.append(float(result["total_amt_chng"]))
        
    if result["total_trans_amt"] == "":
        return None
    else:
        return_list.append(int(result["total_trans_amt"]))
        
    if result["total_trans_ct"] == "":
        return None
    else:
        return_list.append(int(result["total_trans_ct"]))
        
    if result["total_ct_chng"] == "":
        return None
    else:
        return_list.append(float(result["total_ct_chng"]))
        
    if result["avg_utilization_ratio"] == "":
        return None
    else:
        return_list.append(float(result["avg_utilization_ratio"]))
        
    return return_list

def create_predict_dataframe(data : list) -> pd.DataFrame:
    df = pd.DataFrame({"Total_Relationship_Count" : data[0],
                         "Months_Inactive_12_mon" : data[1],
                         "Contacts_Count_12_mon" : data[2],
                         "Total_Revolving_Bal" : data[3],
                         "Total_Amt_Chng_Q4_Q1" : data[4],
                         "Total_Trans_Amt" : data[5],
                         "Total_Trans_Ct" : data[6],
                         "Total_Ct_Chng_Q4_Q1" : data[7],
                         "Avg_Utilization_Ratio" : data[8]})
    df = df.set_index()
    return df
    