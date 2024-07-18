#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Construct the URL to access a specific Star Wars film using the provided film ID from the command line arguments
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

// Make an HTTP GET request to the constructed URL
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body from JSON format to a JavaScript object
  body = JSON.parse(body);

  // Print the title of the film to the console
  console.log(body.title);
});
