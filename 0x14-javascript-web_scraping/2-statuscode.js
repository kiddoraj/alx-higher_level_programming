#!/usr/bin/node

const request = require('request');
const url = process.argv[2]; // Get the URL to request from the first argument

if (!url) {
  console.error('Please provide a URL to make a GET request.');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
