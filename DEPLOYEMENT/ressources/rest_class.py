from flask_restful import Resource
from ressources.requestparser import user_requestParser

class User_request(Resource):
    def get(self):
        user_submit_args = user_requestParser()
        args = user_submit_args.parse_args()
        new_user = {"client_number" : args["client_number"],
                    "total_relationship_count" : args["total_relationship_count"],
                    "months_inactive" : args["months_inactive"],
                    "contacts_count" : args["contacts_count"],
                    "total_revolving_bal" : args["total_revolving_bal"],
                    "total_amt_chng" : args["total_amt_chng"],
                    "total_trans_amt" : args["total_trans_amt"],
                    "total_trans_ct" : args["total_trans_ct"],
                    "total_ct_chng" : args["total_ct_chng"],
                    "avg_utilization_ratio" : args["avg_utilization_ratio"]}
        result = "The prediction model is not implemented yet !!!"
        return {"Prediction" : result}, 201