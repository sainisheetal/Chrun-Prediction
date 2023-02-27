from flask import Flask, render_template, request
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
from ressources.entries_treatment import treat_information, create_predict_dataframe

import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)

with open("model/model.pickle", "rb") as file:
    model = pickle.load(file)

@app.route('/home', methods=['POST', 'GET'])
def home():
    form = user_entry_form()
    result_prediction = "Please enter the information of a client to get a prediction !"
    result_crossdata = "Please enter the information of a client to get the other services the bank provide to him !"
    if form.is_submitted():
        result = request.form
        result_prediction = treat_information(result)
        client_number = result[0]
        #créer la base de donnée No_sql et se servir du numéro client pour récupérer les assurances.
        #model_result = model.predict(create_predict_dataframe(result[1:]))
        #La ligne est foireuse, vérifier le travaille de Zak dans un fichier à part car flemme de tout refaire.
        return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=result_crossdata)
    return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=result_crossdata)

@app.route("/Contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/Insights")
def insights():
    return render_template("insights.html")
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)