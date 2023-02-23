from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, FloatField

class user_entry_form(FlaskForm):
    client_number = IntegerField('client_number')
    attrition_flag = SelectField('attrition_flag', choices=["Existing Customer",
                                                            "Attrited Customer"]) #Remettre les valeurs des types de propriété
    age = IntegerField('age')
    gender = SelectField('gender', choices=["M",
                                            "F"])
    dependent_count = IntegerField('dependent_count')    
    education_level = SelectField('education_level', choices=["Unknown",
                                                              "Uneducated",
                                                              "High School",
                                                              "College",
                                                              "Graduate",
                                                              "Post-Graduate",
                                                              "Doctorate"])
    marital_status = SelectField('marital_status', choices=["Unknown",
                                                            "Single",
                                                            "Married",
                                                            "Divorced"])
    income_category = SelectField('income_category', choices=["Unknown",
                                                              "Less than $40K",
                                                              "$40K - $60K",
                                                              "$60K - $80K",
                                                              "$80K - $120K",
                                                              "$120K +"])
    
    card_category = SelectField('card_category', choices=["Blue",
                                                          "Silver",
                                                          "Gold",
                                                          "Platinum"])
    months_on_book = IntegerField('months_on_book')
    total_relationship_count = IntegerField('total_relationship_count')
    months_inactive = IntegerField('months_inactive')
    contacts_count = IntegerField('contacts_count')
    credit_limit = FloatField('credit_limit')
    total_revolving_bal = IntegerField('total_revolving_bal')
    avg_open_to_buy = FloatField('avg_open_to_buy')
    total_amt_chng = FloatField('total_amt_chng')
    total_trans_amt = IntegerField('total_trans_amt')
    total_trans_ct = IntegerField('total_trans_ct')
    total_ct_chng = FloatField('total_ct_chng')
    avg_utilization_ratio = FloatField('avg_utilization_ratio')
    NBCFC3CDELMI1 = FloatField('NBCFC3CDELMI1')
    NBCFC3CDELMI2 = FloatField('NBCFC3CDELMI2')
    submit = SubmitField('submit')