#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Use the 'readFile' method to read the file asynchronously
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  // If an error occurs, print the error object to the console
  if (err) {
    console.log(err);
  } else {
    // If no error occurs, print the file contents to the console
    process.stdout.write(data);
  }
});
