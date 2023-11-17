import json

from flask import Flask
from flask.json import jsonify

from dataset import get_country_data

app = Flask(__name__)

@app.route("/api")
def country_data():
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())
    return jsonify(data_dict)

@app.route("/api/<country>")
def country_specific_data(country):
    data_df = get_country_data()
    data_dict = json.loads(data_df.to_json())

    country_data = data_dict.get(country.lower(), {})

    #if country_data is None:
    #    return jsonify({}), 404
    
    return jsonify(country_data)