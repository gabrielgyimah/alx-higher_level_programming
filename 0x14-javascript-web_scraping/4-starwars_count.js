#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
    if (!error && response.statusCode == 200) {
        const data = JSON.parse(body);
        let count = 0;

        for (let i = 0; i < data.characters.length; i++) {
            if (data.characters[i].includes('18')) {
                count++;
            }
        }
        console.log(count);
    } else {
        console.error(error);
    }
});