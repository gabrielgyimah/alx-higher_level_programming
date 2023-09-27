#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, function (error, response, body) {
  if (error) throw error;
  const characters = JSON.parse(body).characters;

  for (item in characters) {
    await new Promise((resolve, reject) => {
      request.get(item, function (err, res, bod) {
        if (err) throw err;
	const result = JSON.parse(bod).name;
	console.log(result);
	resolve();
      });
    });
  }
});
