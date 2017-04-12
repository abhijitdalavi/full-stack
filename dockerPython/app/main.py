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
                "total_calls": 13000,
                "total_calls_over2": 7000,
                "total_calls_over5": 2000,
                "data": [
                    {
                        "name": "Google Organic",
                        "total_calls": 1000,
                        "total_calls_over2": 777,
                        "total_calls_over5": 212,
                        "touches": [
                                {
                                    "source__channel": "Google Organic",
                                    "first_touch": "Google Organic",
                                    "last_touch": "Psych Today",
                                    "number_of_callers": 215,
                                    "talk_time": 777,
                                    "percent_total": 27,
                                    "calls_over2": 77,
                                    "talk_time_over2": 154,
                                    "calls_over5": 22,
                                    "talk_time_over5": 110
                                },
                            {
                                    "source__channel": "Google Organic",
                                    "first_touch": "Google Organic",
                                    "last_touch": "Content Net",
                                    "number_of_callers": 109,
                                    "talk_time": 777,
                                    "percent_total": 13,
                                    "calls_over2": 63,
                                    "talk_time_over2": 126,
                                    "calls_over5": 17,
                                    "talk_time_over5": 85
                                }
                        ],
                        "records_end": 2,
                        "records_start": 1,
                    },
                    {
                        "name": "Facebook Organic",
                        "total_calls": 547,
                        "total_calls_over2": 653,
                        "total_calls_over5": 124,
                        "touches": [
                                {
                                    "source__channel": "Facebook Organic",
                                    "first_touch": "Facebook Organic",
                                    "last_touch": "Psych Today",
                                    "number_of_callers": 110,
                                    "talk_time": 777,
                                    "percent_total": 55,
                                    "calls_over2": 53,
                                    "talk_time_over2": 106,
                                    "calls_over5": 12,
                                    "talk_time_over5": 60
                                },
                                {
                                    "source__channel": "Facebook Organic",
                                    "first_touch": "Facebook Organic",
                                    "last_touch": "Content Net",
                                    "number_of_callers": 66,
                                    "talk_time": 777,
                                    "percent_total": 25,
                                    "calls_over2": 33,
                                    "talk_time_over2": 66,
                                    "calls_over5": 11,
                                    "talk_time_over5": 55
                                }
                        ],
                        "records_end": 2,
                        "records_start": 1,
                    }
                ],
                "page": 1,
                "per_page": 25
            }
            # if the token matches return the json object
            return jsonify(data)

    else:
        return "GET/POST NOT WORKING"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
