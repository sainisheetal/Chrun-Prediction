from flask_restful import Resource
from ressources.requestparser import user_requestParser
import pickle
import json

class User_request(Resource):
    def get(self):
        with open("model/model.pickle", "rb") as file:
            model = pickle.load(file)
            user_submit_args = user_requestParser()
            args = user_submit_args.parse_args()
            new_user = [args["client_number"],
                        args["total_relationship_count"],
                        args["months_inactive"],
                        args["contacts_count"],
                        args["total_revolving_bal"],
                        args["total_amt_chng"],
                        args["total_trans_amt"],
                        args["total_trans_ct"],
                        args["total_ct_chng"],
                        args["avg_utilization_ratio"]]
        result_prediction = model.predict([new_user[1:]])
        with open('database/insurance.json') as file:
            data = json.load(file)
            insurances = data[f"{new_user[0]}"]
        return {"Prediction" : f"{result_prediction[0]}",
                "Other services" : insurances}, 201