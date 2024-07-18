#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the file name from the command line arguments
const file = process.argv[2];

try {
  // Read the file contents as a UTF-8 encoded string
  const data = fs.readFileSync(file, 'utf8');

  // Print the file contents to the console
  console.log(data);
} catch (err) {
  // If an error occurs (e.g., file not found), print the error to the console
  console.error(err);
}
