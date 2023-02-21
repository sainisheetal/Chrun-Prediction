from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from forms import property_entry_form
import pickle

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)

@app.route('', methods=['GET', 'POST'])
def home():
    form = property_entry_form()
    if form.is_submitted():
        result = request.form
        return render_template('index.html', form=form, result=result)
    return render_template('index.html', form=form)

property_put_args = reqparse.RequestParser()
property_put_args.add_argument("area", type= int, help="Area of the property is required !", required=True)
property_put_args.add_argument("property-type", type=str, help="The type of property is required !", required=True)
property_put_args.add_argument("rooms-number", type=int, help="The number of rooms is required !", required=True)
property_put_args.add_argument("zip-code", type=int, help="The zip code is required", required=True)
property_put_args.add_argument("land-area", type=int, help="the size of the land", required=False)
property_put_args.add_argument("garden", type=bool, help="Is there a garden ?", required=False)
property_put_args.add_argument("garden-area", type=int, help="the size of the garden", required=False)
property_put_args.add_argument("equipped-kitchen", type=bool, help="Is there a fully-equipped kitchen ?", required=False)
property_put_args.add_argument("full-address", type=str, help="the complete address of the property", required=False)
property_put_args.add_argument("swimming-pool", type=bool, help="Is there at least one swimming pool ?", required=False)
property_put_args.add_argument("furnished", type=bool, help="Is the property already furnished ?", required=False)
property_put_args.add_argument("open-fire", type=bool, help="Is there at least one open-fire ?", required=False)
property_put_args.add_argument("terrace", type=bool, help="Is there a terrace ?", required=False)
property_put_args.add_argument("terrace-area", type=int, help="what is the size of the terrace", required=False)
property_put_args.add_argument("facade-number", type=int, help="Number of facade of the property", required=False)
property_put_args.add_argument("building-state", type=str, help="The state of the property", required=False)

class Property(Resource):
    def get(self):
        args = property_put_args.parse_args()
        new_property = {"area" : args["area"],
                        "property-type" : args["property-type"],
                        "rooms-number" : args["rooms-number"],
                        "zip-code" : args["zip-code"],
                        "land-area" : args["land-area"],
                        "garden" : args["garden"],
                        "garden-area" : args["garden-area"],
                        "equipped-kitchen" : args["equipped-kitchen"],
                        "full-address" : args["full-address"],
                        "swimming-pool" : args["swimming-pool"],
                        "furnished" : args["furnished"],
                        "open-fire" : args["open-fire"],
                        "terrace" : args["terrace"],
                        "terrace-area" : args["terrace-area"],
                        "facade-number" : args["facade-number"],
                        "building-state" : args["building-state"]}
        #verifier les données avant de les passer au model
        result = model_prediction(new_property)
        return {"estimation" : result}, 201
            
api.add_resource(Property, "/Property")

if __name__ == '__main__':
    app.run(debug=True, port=5000)