from flask import Flask, render_template, request
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
from ressources.entries_treatment import treat_information, create_predict_dataframe
from pymongo import MongoClient
from pprint import pprint

import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)
client = MongoClient('localhost', 27017)

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
        #créer la base de donnée No_sql et se servir du numéro client pour récupérer les assurances.
        #model_result = model.predict(create_predict_dataframe(result[1:]))
        #La ligne est foireuse, vérifier le travaille de Zak dans un fichier à part car flemme de tout refaire.
        result_prediction = "The model is not yet ready to be incorporated. When it will be the prediction will be here with possible other information depending on Zakaria's work."
        result_crossdata = "If a client number is entered in the form and the client number is present in the No_SQL database, the value of this client will be show here depending on the other services he paid for."
        return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=result_crossdata)
    return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=result_crossdata)

@app.route("/Contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/Dashboard")
def insights():
    return render_template("dashboard.html")
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)