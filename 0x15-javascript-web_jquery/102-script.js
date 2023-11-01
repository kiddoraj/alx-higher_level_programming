// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the button with id "btn_translate"
  $("input#btn_translate").click(function() {
    // Get the language code entered in the input with id "language_code"
    const languageCode = $("input#language_code").val();

    // Make an AJAX GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      // Extract the translation from the response
      const translation = data.hello;

      // Update the content of the <div> with id "hello" with the translation
      $("div#hello").text(translation);
    }).fail(function() {
      console.error("Failed to fetch the translation.");
    });
  });
});
