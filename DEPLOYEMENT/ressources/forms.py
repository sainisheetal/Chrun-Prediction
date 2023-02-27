from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, FloatField

class user_entry_form(FlaskForm):
    age = IntegerField('age')
    gender = SelectField('gender', choices=["M",
                                            "F"])
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
    submit = SubmitField('submit')