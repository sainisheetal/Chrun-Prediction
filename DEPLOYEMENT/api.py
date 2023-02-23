from flask import Flask, render_template, request
from flask_restful import Api
from ressources.forms import user_entry_form
from ressources.rest_class import User_request
import pickle

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)

@app.route('/home', methods=['POST', 'GET'])
def home():
    form = user_entry_form()
    if form.is_submitted():
        result = request.form
        result = "model not implemented !!!"
        return render_template('index.html', form=form, result=result)
    return render_template('index.html', form=form)
            
api.add_resource(User_request, "/User")

if __name__ == '__main__':
    app.run(debug=True, port=5000)