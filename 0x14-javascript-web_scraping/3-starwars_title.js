#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from the first argument

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(`Title: ${movieData.title}`);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
