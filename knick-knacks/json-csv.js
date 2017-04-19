/*
    Just a simple solution to the "Quick Export" functionality I needed.
    All you gotta do is pass in a JSON object and click the button!
*/

// Just a snippet sample from YAK (channels)
var dummyData = [
    {
    "Datetime": "3:00am",
    "1st Touch": 23423,
    "Last Before Call": 7233200,
    "# of Callers": 202340,
    "Calls > 2min": 323,
    "Calls > 5min": 123,
    "Talk Time": 250000,
    "% Total": 56
},
{
    "Datetime": "11:00pm",
    "1st Touch": 3456,
    "Last Before Call": 456,
    "# of Callers": 73736,
    "Calls > 2min": 385,
    "Calls > 5min": 145,
    "Talk Time": 85546,
    "% Total": 27
},
{
    "Datetime": "16:00pm",
    "1st Touch": 8745,
    "Last Before Call": 4456,
    "# of Callers": 2756,
    "Calls > 2min": 345,
    "Calls > 5min": 174,
    "Talk Time": 4546,
    "% Total": 19
},
{
    "Datetime": "7:17am",
    "1st Touch": 9834,
    "Last Before Call": 9834,
    "# of Callers": 93847,
    "Calls > 2min": 234,
    "Calls > 5min": 451,
    "Talk Time": 349874,
    "% Total": 8
}
];

// The converter function, this is where the magic happens
function ConvertToCSV(jsonIn) {

    // Variables we gon' need.
    var result, ctr, keys, columnDelim, lineDelim, data;

    // Set data var to data input, otherwise nothing
    data = jsonIn.data || null;
    if (data == null || !data.length) {
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
    data.forEach(function (item) {

        // Init counter
        ctr = 0;

        // Iterate through each value in said object
        keys.forEach(function (key) {
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
function downloadCSV(input) {

    // We gon' need these
    var data, filename, link;

    // Call the previous func to create a csv object
    var csv = ConvertToCSV({
        data: dummyData
    });

    // If nothing comes back we can just start right here...
    if (csv == null) return;

    // Check for filename, otherwise give 'em one
    filename = input.filename || 'export.csv';

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