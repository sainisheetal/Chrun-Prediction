from pymongo import MongoClient, database, collection, InsertOne
from pprint import pprint

def verification_mangodb_table(client : MongoClient):
    dblist = client.list_database_names()
    if "services" not in dblist:
        db = client["services"]
        mycol = db["assurances"]
    else:
        db = client.services
        collist = db.list_collection_names()
        if "assurances" not in collist:
            mycol = db["assurances"]
        
def connection_mangodb_table(client : MongoClient) -> collection:
    db = client.services
    db = db.assurances
    return db

def add_one_result(result : dict, assurances : collection):
    assurances.insert_one(result)
    
def find_assurance_info(client_number : int, assurances : collection) -> dict:
    return assurances.find_one({"CLIENTNUM" : client_number})