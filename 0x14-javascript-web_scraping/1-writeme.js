#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Use the 'writeFile' method to write data to a file asynchronously
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  // If an error occurs, print the error object to the console
  if (err) {
    console.log(err);
  }
});
