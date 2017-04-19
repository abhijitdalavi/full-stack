var dummyData = {
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
            };

function ConvertToCSV(jsonIn) {
    // Variables we gon' need.
    var result, ctr, keys, columnDelimiter, lineDelimiter, data;
    
    // Set data var to data input, otherwise nothing
    data = jsonIn.data || null;
    if (data == null || !data.length){
        // If nothing, tell them they didn't give us anything!
        return "No Data!";
    }

    columnDelimiter = jsonIn.columnDelimiter || ',';
    lineDelimiter = jsonIn.lineDelimiter || '\n';

    keys = Object.keys(data[0]);

}