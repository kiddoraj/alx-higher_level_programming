// Use jQuery to select the <header> element by its tag name
const headerElement = $('header');

// Check if the header element was found
if (headerElement.length > 0) {
  // Update the text color to red
  headerElement.css('color', '#FF0000');
} else {
  console.error("The <header> element was not found in the document.");
}
