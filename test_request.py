import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/User", json={"client_number" : 7954265198,
                                              "total_relationship_count" : 7,
                                              "months_inactive" : 8,
                                              "contacts_count" : 9,
                                              "total_revolving_bal" : 7,
                                              "total_amt_chng" : 4.6,
                                              "total_trans_amt" : 78,
                                              "total_trans_ct" : 4,
                                              "total_ct_chng" : 8.5,
                                              "avg_utilization_ratio" : 7.4})

print(response.json())