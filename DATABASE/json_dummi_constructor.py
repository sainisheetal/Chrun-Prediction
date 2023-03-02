import json
import pandas as pd
import random

def rand_dict_filler() -> dict:
    result_dict = {}
    nbr_assurance = random.randint(0,5)
    mylist = ["Dentist insurance", "Car insurance", "Pet insurance", "Travel insurance", "Hospitalisation insurance",
              "Family insurance", "Fire insurance", "Burglary insurance", "Divorce insurance", "Death insurance"]
    for i in range(nbr_assurance):
        result_dict[f"{mylist[random.randint(0,9)]}"] = f"{random.randint(5, 35)}"
    return result_dict
    

df = pd.read_csv("data/BankChurners.csv")
clients = df["CLIENTNUM"].values

file = open("DEPLOYEMENT/database/insurance.json", "w")
file.close()

for client in clients:
    result_dict = rand_dict_filler()
    with open("DEPLOYEMENT/database/insurance.json", "a") as file:
        json.dump({"CLIENTNUM" : f"{client}", "insurance_data" : result_dict}, file)
    
