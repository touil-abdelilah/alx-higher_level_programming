#!/usr/bin/node

const request = require('request');

// Function to make an HTTP GET request and return a promise
function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, _res, body) {
      if (err) {
        // Reject the promise if an error occurs
        reject(err);
      } else {
        // Resolve the promise with the response body
        resolve(body);
      }
    });
  });
}

// Error handler function to log errors
function errHandler (err) {
  console.log(err);
}

// Function to print the names of characters in a specific Star Wars movie
function printMovieCharacters (movieId) {
  // Construct the URL to access the specific movie using the provided movie ID
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  // Get data from the movie URL and parse the response body
  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      // Extract the list of character URLs
      const characters = res.characters;
      const promises = [];

      // Loop through each character URL and get data from each URL
      for (let i = 0; i < characters.length; ++i) {
        promises.push(getDataFrom(characters[i]));
      }

      // Wait for all character data requests to complete
      Promise.all(promises)
        .then((results) => {
          // Print the name of each character
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          // Handle any errors that occur during the character data requests
          console.log(err);
        });
    });
}

// Call the function to print movie characters using the movie ID provided as a command line argument
printMovieCharacters(process.argv[2]);
