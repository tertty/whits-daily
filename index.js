const request = require('request');

let url = "https://raw.githubusercontent.com/tertty/whits-daily/master/whits_daily.json";

let options = {json: true};

request(url, options, (error, res, body) => {
    if (error) {
        return  console.log(error);
    }

    if (!error && res.statusCode == 200) {
        // do something with JSON, using the 'body' variable
          console.log(body.flav_ot_day.toString().toLowerCase() + ' ' + body.flav_desc.toString().toLowerCase());
    }
});