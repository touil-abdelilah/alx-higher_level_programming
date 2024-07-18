#!/usr/bin/node

// Import the 'fs' module to handle file system operations
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Try to read the file synchronously
try {
  // Read the file contents as a UTF-8 encoded string
  const data = fs.readFileSync(filePath, 'utf8');

  // Print the file contents to the console
  console.log(data);
} catch (err) {
  // If an error occurs (e.g., file not found), print the error object
  console.error(err);
}
