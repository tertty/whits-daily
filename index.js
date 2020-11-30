const fetch = require('node-fetch');

let url = "https://www.instagram.com/whitsfordessert/";

fetch(url, options = {headers : {'User-Agent' : 'Mozilla/5.0'}})
    .then(res => res.text())
    .then(body => {
        console.log(body);

        today_flavor_start = body.indexOf("today");
        today_flavor_end = today_flavor_start;

        while(body[today_flavor_end] != '!'){
            today_flavor_end++;
        }

        today_flavor = body.substring(today_flavor_start, today_flavor_end);

        today_desc = ":)";

        console.log("Ok, so here's the sitch. What Whit's has is " + today_flavor + " for today's flavor. What is it? " + today_desc);
    });