#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL to request from the first argument
const filePath = process.argv[3]; // Get the file path to store the response from the second argument

if (!url || !filePath) {
  console.error('Please provide a URL and a file path.');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(`Error writing to file: ${writeError}`);
      } else {
        console.log(`Webpage content saved to ${filePath}`);
      }
    });
  }
});

