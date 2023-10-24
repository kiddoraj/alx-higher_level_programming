#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the first argument
const content = process.argv[3]; // Get the string to write from the second argument

if (!filePath || !content) {
  console.error('Please provide a file path and content to write.');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // If an error occurred while writing, print the error object
  } else {
    console.log(`Content successfully written to ${filePath}.`);
  }
});
