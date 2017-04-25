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
                "start_date": "2017-03-02 00:00:00",
                "end_date": "2017-03-02 23:59:59",
                "label": "2 Mar",
                "time_frame": "daily",
                "data": {
                    "Google Organic": {
                        "total_calls": 922,
                        "touches": [
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Google Organic",
                                "talk_time": 219540,
                                "talk_time_over2": 205022,
                                "talk_time_over5": 164968,
                                "calls_over2": 432,
                                "calls_over5": 228,
                                "number_of_callers": 648,
                                "percent_total": 70.281995661605
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "direct",
                                "talk_time": 33556,
                                "talk_time_over2": 30606,
                                "talk_time_over5": 20656,
                                "calls_over2": 82,
                                "calls_over5": 34,
                                "number_of_callers": 120,
                                "percent_total": 13.015184381779
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "google ppc- content network",
                                "talk_time": 22376,
                                "talk_time_over2": 21458,
                                "talk_time_over5": 17710,
                                "calls_over2": 34,
                                "calls_over5": 16,
                                "number_of_callers": 48,
                                "percent_total": 5.2060737527115
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Bing Organic",
                                "talk_time": 9610,
                                "talk_time_over2": 8540,
                                "talk_time_over5": 6494,
                                "calls_over2": 26,
                                "calls_over5": 14,
                                "number_of_callers": 40,
                                "percent_total": 4.3383947939262
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Facebook CPC",
                                "talk_time": 7780,
                                "talk_time_over2": 7440,
                                "talk_time_over5": 6012,
                                "calls_over2": 16,
                                "calls_over5": 10,
                                "number_of_callers": 20,
                                "percent_total": 2.1691973969631
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "yahoo - organic",
                                "talk_time": 2592,
                                "talk_time_over2": 2344,
                                "talk_time_over5": 1956,
                                "calls_over2": 6,
                                "calls_over5": 4,
                                "number_of_callers": 12,
                                "percent_total": 1.3015184381779
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "other - referring",
                                "talk_time": 3698,
                                "talk_time_over2": 3698,
                                "talk_time_over5": 3446,
                                "calls_over2": 10,
                                "calls_over5": 8,
                                "number_of_callers": 10,
                                "percent_total": 1.0845986984816
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "bing ppc- content network",
                                "talk_time": 1338,
                                "talk_time_over2": 1338,
                                "talk_time_over5": 0,
                                "calls_over2": 6,
                                "calls_over5": 0,
                                "number_of_callers": 6,
                                "percent_total": 0.65075921908894
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "acadia corp sites",
                                "talk_time": 1134,
                                "talk_time_over2": 1134,
                                "talk_time_over5": 0,
                                "calls_over2": 6,
                                "calls_over5": 0,
                                "number_of_callers": 6,
                                "percent_total": 0.65075921908894
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "google ppc- unknown",
                                "talk_time": 224,
                                "talk_time_over2": 0,
                                "talk_time_over5": 0,
                                "calls_over2": 0,
                                "calls_over5": 0,
                                "number_of_callers": 4,
                                "percent_total": 0.43383947939262
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "google ppc- behavioral health ",
                                "talk_time": 762,
                                "talk_time_over2": 762,
                                "talk_time_over5": 762,
                                "calls_over2": 2,
                                "calls_over5": 2,
                                "number_of_callers": 2,
                                "percent_total": 0.21691973969631
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Psych Today Profiles",
                                "talk_time": 238,
                                "talk_time_over2": 0,
                                "talk_time_over5": 0,
                                "calls_over2": 0,
                                "calls_over5": 0,
                                "number_of_callers": 2,
                                "percent_total": 0.21691973969631
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Swoop",
                                "talk_time": 944,
                                "talk_time_over2": 944,
                                "talk_time_over5": 944,
                                "calls_over2": 2,
                                "calls_over5": 2,
                                "number_of_callers": 2,
                                "percent_total": 0.21691973969631
                            },
                            {
                                "first_touch": "Google Organic",
                                "last_touch": "Healthy Place",
                                "talk_time": 1652,
                                "talk_time_over2": 1652,
                                "talk_time_over5": 1652,
                                "calls_over2": 2,
                                "calls_over5": 2,
                                "number_of_callers": 2,
                                "percent_total": 0.21691973969631
                            }
                        ],
                        "percent_total": 100
                    },
                    "total_calls": 922
                },
                "last_updated": "2017-04-25 13:41:07",
                "cached": false
            }
            # if the token matches return the json object
            return jsonify(data)

    else:
        return "GET/POST NOT WORKING"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
