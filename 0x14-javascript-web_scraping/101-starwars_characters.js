#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // Get the Movie ID from the first argument

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
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
      const characterUrls = movieData.characters;

      function printCharacter (index) {
        if (index < characterUrls.length) {
          const characterUrl = characterUrls[index];
          request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error(charError);
            } else if (charResponse.statusCode !== 200) {
              console.error(`Request failed with status code: ${charResponse.statusCode}`);
            } else {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
              printCharacter(index + 1); // Continue with the next character
            }
          });
        }
      }

      console.log(`Characters in "${movieData.title}":`);
      printCharacter(0); // Start printing characters from the first character URL
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
