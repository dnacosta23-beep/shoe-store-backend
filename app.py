from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

shoes = [
    {"id": 1, "name": "Running Shoes", "price": 60},
    {"id": 2, "name": "Boots", "price": 85},
    {"id": 3, "name": "Sandals", "price": 25}
]


