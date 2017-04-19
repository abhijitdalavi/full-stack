// Just a snippet sample from YAK (channels)
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

// The converter function, this is where the magic happens
function ConvertToCSV(jsonIn) {

    // Variables we gon' need.
    var result, ctr, keys, columnDelim, lineDelim, data;
    
    // Set data var to data input, otherwise nothing
    data = jsonIn.data || null;
    if (data == null || !data.length){
        // If nothing, tell them they didn't give us anything!
        return "No Data!";
    }

    // If delimiter's exist already use those, otherwise comma and newLine, what else?
    columnDelim = jsonIn.columnDelim || ',';
    lineDelim = jsonIn.lineDelim || '\n';

    // Grab the keys from the first object, we'll need these for header row
    keys = Object.keys(data[0]);

    // Start with empty result
    result = '';

    // Add in keys from the first object to create header row
    result += keys.join(columnDelim);
    result += lineDelim;

    // Loop through each data object
    data.forEach(function(item) {

        // Init counter
        ctr = 0;

        // Iterate through each value in said object
        keys.forEach(function(key){
            if (ctr > 0) result += columnDelim;
            result += item[key];
            ctr++;
        });

        // New line after we finish iterating through the values of a single object
        result += lineDelim;
    });

    // Spit out what we did
    return result;
}

// Download function, because how else they gonna get it?
function downloadCSV(stuff) {
    
    // We gon' need these
    var data, filename, link;

    // Call the previous func to create a csv object
    var csv = ConvertToCSV({
        data: dummyData
    });
    // If nothing comes back we can just start right here...
    if (csv == null) return;

    // Check for filename, otherwise give 'em one
    filename = stuff.filename || 'export.csv';

    // Magic that tells browser this thing is a CSV
    if (!csv.match(/^data:text\/csv/i)) {
        csv = 'data:text/csv;charset=utf-8,' + csv;
    }
    data = encodeURI(csv);

    // Now we setup the HTML link element for the downloads, and lulz
    link = document.createElement('a');
    link.setAttribute('href', data);
    link.setAttribute('download', filename);
    link.click();
}