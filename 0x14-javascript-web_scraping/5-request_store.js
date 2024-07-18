#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Make an HTTP GET request to the URL provided as the first command line argument
request(process.argv[2], function (_err, _res, body) {
  // Write the response body to a file specified as the second command line argument
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    // If an error occurs during the file writing process, print the error object to the console
    if (err) {
      console.log(err);
    }
  });
});
