// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Send an AJAX GET request to the URL
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    // Extract the list of movies from the response
    const movies = data.results;

    // Select the <ul> with id "list_movies"
    const movieList = $("ul#list_movies");

    // Loop through the movies and append each title to the list
    movies.forEach(function(movie) {
      const title = movie.title;
      movieList.append(`<li>${title}</li>`);
    });
  });
});
