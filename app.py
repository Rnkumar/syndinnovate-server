from flask import request
from flask import Flask
import mongooperations as mo
import json

app = Flask(__name__)


# app.run()

@app.route('/home', methods=["GET"])
def home():
    return "hello"


@app.route('/populate', methods=["POST"])
def populate():
    data = request.json
    print(data)
    mo.insert_data(data)
    return "success"


@app.route('/getUsers', methods=["GET"])
def get_users():
    data = mo.get_users()
    return json.dumps({"response": data})


@app.route('/getData', methods=["GET"])
def get_data():
    query = request.args.get("id")
    data = mo.get_data(query)
    return json.dumps({"response": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
