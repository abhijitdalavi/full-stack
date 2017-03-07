import os
from flask import Flask, jsonify, session, render_template, request, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    # set message to return
    message = "try /getData to POST json"
    # spits out message on load
    return message


@app.route('/getData', methods=['POST'])
def getData():
    # return based on request
    if request.method == "POST":
        json_dict = request.get_json()
        token = json_dict['token']

        if token == 'jwcziqhurlubnm0972yg0e2y1bvxweflyfzws7mc':
            data = {
                "total_records": 4,
                "data": [
                    {
                        "Google Organic": {
                            "total_calls": 1000,
                            "touches": [
                                {
                                    "source__channel": "Google Organic",
                                    "first_touch": "Google Organic",
                                    "last_touch": "Psych Today",
                                    "number_of_callers": 200,
                                    "percent_total": 20
                                },
                                {
                                    "source__channel": "Google Organic",
                                    "first_touch": "Google Organic",
                                    "last_touch": "Content Net",
                                    "number_of_callers": 100,
                                    "percent_total": 10
                                }
                            ]
                        },
                        "Facebook Organic": {
                            "total_calls": 200,
                            "touches": [
                                {
                                    "source__channel": "Facebook Organic",
                                    "first_touch": "Facebook Organic",
                                    "last_touch": "Psych Today",
                                    "number_of_callers": 100,
                                    "percent_total": 50
                                },
                                {
                                    "source__channel": "Facebook Organic",
                                    "first_touch": "Google Organic",
                                    "last_touch": "Content Net",
                                    "number_of_callers": 50,
                                    "percent_total": 25
                                }
                            ]
                        }
                    }
                ],
                "records_end": 4,
                "records_start": 1,
                "page": 1,
                "per_page": 4
            }
            # if the token matches return the json object
            return jsonify(data)

    else:
        return "GET/POST NOT WORKING"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
