from crypt import methods
from distutils.log import debug
from flask import Flask, jsonify, request

# you’ll look at a REST API in each framework. All the examples will be for a similar 
# API that manages a collection of countries.

# Each country will have the following fields:
# name is the name of the country.
# capital is the capital of the country.
# area is the area of the country in square kilometers.
# The fields name, capital, and area store data about a specific country somewhere in the world.

app = Flask(__name__)

countries = [
    {'id':1, 'name':"Thailand", 'capital':"Bangkok", 'area':513120},
    {'id':2, 'name':"Australia", 'capital':"Canberra", 'area':7617930},
    {'id':3, 'name':"Egypt", 'capital':"Cairo", 'area':1010408}
]

def get_next_id():
    return max(country['id'] for country in countries) + 1

@app.route('/countries', methods=["GET"])
def get_country():
    return jsonify(countries)

@app.route('/countries', methods=["POST"])
def add_country():
    if request.is_json:
        country = request.get_json()
        country['id'] = get_next_id()
        countries.append(country)
        return countries, 201 # A new country has been created
    return {'error':'Request must be JSON'}, 415 # The request data format is not supported by the server.


if __name__ == "__main__":
    app.run(debug=True)