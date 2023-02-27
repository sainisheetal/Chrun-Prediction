from flask import Flask, render_template, request
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
from ressources.entries_treatment import treat_information

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
    if form.is_submitted():
        result = request.form
        data = treat_information(result)
        if isinstance(data, list):
            result = model.predict(data)
            result = "The data are treated correctly but the model is not implemented yed !"
        return render_template('index.html', form=form, result=data)
    return render_template('index.html', form=form)
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)