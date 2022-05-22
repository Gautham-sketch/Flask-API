from flask import Flask, jsonify, request
from Data_Science_Project_Final import data

app = Flask(__name__)

@app.route("/")
def index():
    return({
        "data" : data,
        "message" : "success"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : star_data,
        "message" : "success"
    }), 200

if __name__ == '__main__':
    app.run()