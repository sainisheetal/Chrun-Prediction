from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField

class user_entry_form(FlaskForm):
    client_number = IntegerField("CLIENTNUM")
    total_relationship_count = IntegerField("Total_Relationship_Count")
    months_inactive = IntegerField("Months_Inactive_12_mon")
    contacts_count = IntegerField("Contacts_Count_12_mon")
    total_revolving_bal = IntegerField("Total_Revolving_Bal")
    total_amt_chng = FloatField("Total_Amt_Chng_Q4_Q1")
    total_trans_amt = IntegerField("Total_Trans_Amt")
    total_trans_ct = IntegerField("Total_Trans_Ct")
    total_ct_chng = FloatField("Total_Ct_Chng_Q4_Q1")
    avg_utilization_ratio = FloatField("Avg_Utilization_Ratio")
    submit = SubmitField('submit')