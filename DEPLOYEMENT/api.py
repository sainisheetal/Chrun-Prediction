from flask import Flask, render_template, request, Markup
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
from ressources.entries_treatment import treat_information
from ressources.insurance_calculation import calculate_client_value

import pickle

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
        if result_prediction != None:
            if result["client_number"] != "":
                result_prediction = model.predict([result_prediction[1:]])
                if result_prediction[0] == 0:
                    result_prediction = "The client is not about to chunk !"
                else:
                    result_prediction = "The client is about to chunk !"
                result_crossdata = calculate_client_value(int(result["client_number"]))
            else:
                result_prediction = model.predict([result_prediction[1:]])
                if result_prediction[0] == 0:
                    result_prediction = "The client is not about to chunk !"
                else:
                    result_prediction = "The client is about to chunk !"
                result_crossdata = "Enter a client number to get his insurance value !"
        else:
            result_prediction = "Please enter all the client data to get a prediction"
            result_crossdata = "Enter a client number to get his insurance value !"
            
        return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=Markup(result_crossdata))
    return render_template('index.html', form=form, result_prediction=result_prediction, result_crossdata=Markup(result_crossdata))

@app.route("/Contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/Dashboard")
def insights():
    return render_template("dashboard.html")
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)