#!/usr/bin/node

const request = require('request');


request.get(process.argv[2], (error, response, body) => {
    if (!error && response.statusCode == 200) {
        const data = JSON.parse(body);
        let dataRes = {}
        for (let i = 0; i < data.length; i++) { // Run through the entire length of data --i
            for (let y = 0; y < data.length; y++) { // Run throug the entire length of data --y
                if (data[i]['userId'] == data[y]['userId']) { // Check if the userId at i is the same as the userId at --y
                    if (data[y]['completed'] == 'true') { // Check if the value of completed of data at --y is true
                        dataRes[data['userId']] += 1;
                    }
                }
            }
        }
        console.log(dataRes);
    } else {
        console.error(error)
    }
})