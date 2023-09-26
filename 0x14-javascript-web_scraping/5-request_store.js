#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
    if (!error && response.statusCode == 200) {
        try {
            fs.writeFileSync(process.argv[3], body, 'utf-8')
        } catch (err) {
            console.error(err)
        }
    } else {
        console.error(error);
    }
})