from flask_restful import  reqparse

def user_requestParser() -> reqparse.RequestParser:
    """_summary_

    Returns:
        reqparse.RequestParser: _description_
        
    Description:
        This function create a request parser for the request on the API.
    """
    user_submit_args = reqparse.RequestParser()
    user_submit_args.add_argument("client_number", type=int, help="Client number is required !", required=True)
    user_submit_args.add_argument("attrition_flag", type=str, help="Attrition Flag is required !", required=True)
    user_submit_args.add_argument("age", type=int, help="Age of the client is required !", required=True)
    user_submit_args.add_argument("gender", type=str, help="Gender of the client is required !", required=True)
    user_submit_args.add_argument("dependent_count", type=int, help="Number of dependent account is required !", required=True)
    user_submit_args.add_argument("education_level", type=str, help="Education level of the client is required !", required=True)
    user_submit_args.add_argument("marital_status", type=str, help="Marital status of the client is required !", required=True)
    user_submit_args.add_argument("income_category", type=str, help="The rought estimation of the client salary is required !", required=True)
    user_submit_args.add_argument("card_category", type=str, help="The type of card of the client is required !", required=True)
    user_submit_args.add_argument("months_on_book", type=int, required=True)
    user_submit_args.add_argument("total_relationship_count", type=int, required=True)
    user_submit_args.add_argument("months_inactive", type=int, required=True)
    user_submit_args.add_argument("contacts_count", type=int, required=True)
    user_submit_args.add_argument("credit_limit", type=float, required=True)
    user_submit_args.add_argument("total_revolving_bal", type=int, required=True)
    user_submit_args.add_argument("avg_open_to_buy", type=float, required=True)
    user_submit_args.add_argument("total_amt_chng", type=float, required=True)
    user_submit_args.add_argument("total_trans_amt", type=int, required=True)
    user_submit_args.add_argument("total_trans_ct", type=int, required=True)
    user_submit_args.add_argument("total_ct_chng", type=float, required=True)
    user_submit_args.add_argument("avg_utilization_ratio", type=float, required=True)
    user_submit_args.add_argument("NBCFC3CDELMI1", type=float, required=True)
    user_submit_args.add_argument("NBCFC3CDELMI2", type=float, required=True)