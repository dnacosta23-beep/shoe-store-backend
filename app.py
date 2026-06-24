from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

shoes = [
    {"id": 1, "name": "Running Shoes", "price": 60},
    {"id": 2, "name": "Boots", "price": 85},
    {"id": 3, "name": "Sandals", "price": 25}
]


@app.route("/")
def home():
    return {"message": "Shoe Store API"}


@app.route("/shoes", methods=["GET"])
def get_shoes():
    return shoes


@app.route("/shoes", methods=["POST"])
def add_shoe():
    data = request.get_json()

    new_shoe = {
        "id": len(shoes) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    shoes.append(new_shoe)

    return {
        "message": "Shoe added successfully!",
        "shoe": new_shoe
    }, 201


if __name__ == "__main__":
    app.run(debug=True)