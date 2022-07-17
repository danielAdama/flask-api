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

