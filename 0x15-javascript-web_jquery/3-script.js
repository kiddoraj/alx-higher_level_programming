// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the <div> with id "red_header"
  $("div#red_header").click(function() {
    // Add the "red" class to the <header> element
    $("header").addClass("red");
  });
});
