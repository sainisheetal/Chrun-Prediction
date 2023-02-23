from flask_restful import Resource
from ressources.requestparser import user_requestParser

class User_request(Resource):  #Mettre dans un nouveau dossier pour la propreter !!!
    def get(self):
        user_submit_args = user_requestParser()
        args = user_submit_args.parse_args()
        new_user = {"client_number" : args["client_number"],
                    "attrition_flag" : args["attrition_flag"],
                    "age" : args["age"],
                    "gender" : args["gender"],
                    "dependent_count" : args["dependent_count"],
                    "education_level" : args["education_level"],
                    "marital_status" : args["marital_status"],
                    "income_category" : args["income_category"],
                    "card_category" : args["card_category"],
                    "months_on_book" : args["months_on_book"],
                    "total_relationship_count" : args["total_relationship_count"],
                    "months_inactive" : args["months_inactive"],
                    "contacts_count" : args["contacts_count"],
                    "credit_limit" : args["credit_limit"],
                    "total_revolving_bal" : args["total_revolving_bal"],
                    "avg_open_to_buy" : args["avg_open_to_buy"],
                    "total_amt_chng" : args["total_amt_chng"],
                    "total_trans_amt" : args["total_trans_amt"],
                    "total_trans_ct" : args["total_trans_ct"],
                    "total_ct_chng" : args["total_ct_chng"],
                    "avg_utilization_ratio" : args["avg_utilization_ratio"],
                    "NBCFC3CDELMI1" : args["NBCFC3CDELMI1"],
                    "NBCFC3CDELMI2" : args["NBCFC3CDELMI2"]
                    }
        result = "The prediction model is not implemented yet !!!"
        return {"Prediction" : result}, 201