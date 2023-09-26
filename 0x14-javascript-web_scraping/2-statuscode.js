#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');

request.get(process.argv[2], on.('res', (res) => {
	console.log("code:", res.statusCode);
});
