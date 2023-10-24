#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // Get the API URL from the first argument

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

const characterId = 18; // Character ID for Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    try {
      const moviesData = JSON.parse(body);
      let count = 0;

      // Iterate through the movies to count where Wedge Antilles appears
      moviesData.results.forEach((movie) => {
        if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      });

      console.log(`Number of movies where Wedge Antilles appears: ${count}`);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
