// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Send an AJAX GET request to the URL
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
    // Extract the character name from the response
    const characterName = data.name;

    // Update the content of the <div> with id "character" with the character name
    $("div#character").text(characterName);
  });
});
