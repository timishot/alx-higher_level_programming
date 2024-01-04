#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Iterate through tasks and count completed tasks for each user
    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Output the results
    console.log(completedTasksByUser);
  } else {
    console.error(`Error: ${response && response.statusCode}`);
  }
});
