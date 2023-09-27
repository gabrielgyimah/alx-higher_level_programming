#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function(error, res, body) {
  if (error) console.error(error);
  
  data = JSON.parse(body).results;
  const count = 0;
  for (const elem in data) {
    if(elem.includdes('/18')) {
      count +=1;
    }
  }
  console.log(count);
});
