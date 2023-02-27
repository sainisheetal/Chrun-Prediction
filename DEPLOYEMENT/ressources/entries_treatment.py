from data_traduction.traduction_columns import Gender_str_to_number, Education_Level_str_to_number, Marital_Status_str_to_number, Income_Category_str_to_number

def treat_information(result) -> list:
    gender_dictionnary = Gender_str_to_number()
    education_level_dictionnary = Education_Level_str_to_number()
    marital_status_dictionnary = Marital_Status_str_to_number()
    income_category_dictionnary = Income_Category_str_to_number()
    if result['age'] == '':
        return "The age of the client was not entered !"
    return [int(result["age"]), 
            gender_dictionnary[result["gender"]], 
            education_level_dictionnary[result["education_level"]], 
            marital_status_dictionnary[result["marital_status"]], 
            income_category_dictionnary[result["income_category"]]]