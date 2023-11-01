// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the <div> with id "toggle_header"
  $("div#toggle_header").click(function() {
    // Toggle the class between "red" and "green" on the <header> element
    $("header").toggleClass("red green");
  });
});
