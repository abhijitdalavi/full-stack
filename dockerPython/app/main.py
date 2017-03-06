import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
