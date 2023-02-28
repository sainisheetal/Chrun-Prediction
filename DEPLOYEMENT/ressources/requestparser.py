from flask_restful import  reqparse

def user_requestParser() -> reqparse.RequestParser:
    """_summary_

    Returns:
        reqparse.RequestParser: _description_
        
    Description:
        This function create a request parser for the request on the API.
    """
    user_submit_args = reqparse.RequestParser()
    user_submit_args.add_argument("client_number", type=int, help="Client number is required !")
    user_submit_args.add_argument("total_relationship_count", type=int, required=True)
    user_submit_args.add_argument("months_inactive", type=int, required=True)
    user_submit_args.add_argument("contacts_count", type=int, required=True)
    user_submit_args.add_argument("total_revolving_bal", type=int, required=True)
    user_submit_args.add_argument("total_amt_chng", type=float, required=True)
    user_submit_args.add_argument("total_trans_amt", type=int, required=True)
    user_submit_args.add_argument("total_trans_ct", type=int, required=True)
    user_submit_args.add_argument("total_ct_chng", type=float, required=True)
    user_submit_args.add_argument("avg_utilization_ratio", type=float, required=True)
    return user_submit_args