#!/usr/bin/node

const request = require('request');

// Make an HTTP GET request to the URL provided as the first command line argument
request(process.argv[2], function (err, _res, body) {
  if (err) {
    // Print the error object if an error occurs
    console.log(err);
  } else {
    // Object to store the count of completed tasks by each user
    const completedTasksByUsers = {};

    // Parse the response body from JSON format to a JavaScript object
    body = JSON.parse(body);

    // Loop through each task in the response body
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      // Initialize the counter for the user if the task is completed and the user is not already in the object
      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      // Increment the counter for the user if the task is completed
      if (completed) ++completedTasksByUsers[userId];
    }

    // Print the object containing the count of completed tasks by each user
    console.log(completedTasksByUsers);
  }
});
