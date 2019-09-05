from flask import request
from flask import Flask
import mongooperations as mo

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
