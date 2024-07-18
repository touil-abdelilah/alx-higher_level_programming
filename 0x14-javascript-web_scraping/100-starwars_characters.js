#!/usr/bin/node

const request = require('request');

// Construct the URL to access a specific Star Wars film using the provided film ID from the command line arguments
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

// Make an HTTP GET request to the constructed URL
request(starWarsUri, function (_err, _res, body) {
  // Extract the list of character URLs from the response body
  const characters = JSON.parse(body).characters;

  // Loop through each character URL
  for (let i = 0; i < characters.length; ++i) {
    // Make an HTTP GET request to each character URL
    request(characters[i], function (_cErr, _cRes, cBody) {
      // Print the name of the character to the console
      console.log(JSON.parse(cBody).name);
    });
  }
});
