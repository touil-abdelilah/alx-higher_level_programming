#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Use the 'request' function to make an HTTP GET request to the URL provided as the first command line argument
request(process.argv[2], function (_err, res) {
  // Print the response status code if a response was received
  console.log('code:', res.statusCode);
});
