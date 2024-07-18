#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the Star Wars API URL from the command line arguments
const starWarsUri = process.argv[2];

// Initialize a counter to keep track of how many times a specific character appears
let times = 0;

// Make an HTTP GET request to the provided Star Wars API URL
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body from JSON format to a JavaScript object
  body = JSON.parse(body).results;

  // Loop through each film in the results
  for (let i = 0; i < body.length; ++i) {
    // Get the list of characters for the current film
    const characters = body[i].characters;

    // Loop through each character in the list
    for (let j = 0; j < characters.length; ++j) {
      // Get the URL of the current character
      const character = characters[j];

      // Extract the character ID from the URL
      const characterId = character.split('/')[5];

      // If the character ID is '18', increment the counter
      if (characterId === '18') {
        times += 1;
      }
    }
  }

  // Print the total number of times the specific character appears
  console.log(times);
});
