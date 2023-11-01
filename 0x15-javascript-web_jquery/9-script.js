// Use jQuery to send an AJAX request to fetch the translation
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function(data) {
    // Extract the translation value from the response
    const translation = data.hello;

    // Update the content of the <div> with id "hello" with the translation
    $('div#hello').text(translation);
  },
  error: function() {
    console.error('Failed to fetch the translation.');
  }
});
