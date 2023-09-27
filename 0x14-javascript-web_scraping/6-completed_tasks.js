#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  const data = JSON.parse(body);
  let tasksCompleted = {};

  for (const item in data) {
    if (item.completed) {
      if (!tasksCompleted[item.userId]) {
        tasksCompleted[item.userId] = 1;
      } else {
        tasksCompleted += 1;
      }
    }
  }
  console.log(tasksCompleted);
});
