from flask import Flask, render_template, request
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
from data_traduction.traduction_columns import Gender_str_to_number, Education_Level_str_to_number, Marital_Status_str_to_number, Income_Category_str_to_number
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)

gender_dictionnary = Gender_str_to_number()
education_level_dictionnary = Education_Level_str_to_number()
marital_status_dictionnary = Marital_Status_str_to_number()
income_category_dictionnary = Income_Category_str_to_number()

with open("model/model.pickle", "rb") as file:
    model = pickle.load(file)

@app.route('/home', methods=['POST', 'GET'])
def home():
    form = user_entry_form()
    if form.is_submitted():
        result = request.form
        data = [int(result["age"]), 
                gender_dictionnary[result["gender"]], 
                education_level_dictionnary[result["education_level"]], 
                marital_status_dictionnary[result["marital_status"]], 
                income_category_dictionnary[result["income_category"]]]
        #result = model.predict(data)
        return render_template('index.html', form=form, result=data)
    return render_template('index.html', form=form)
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)