#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line arguments

if (!filePath) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // If an error occurred during reading, print the error object
  } else {
    console.log(data); // Print the content of the file
  }
});
