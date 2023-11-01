document.addEventListener("DOMContentLoaded", function() {
  // Find the <header> element using document.querySelector
  const headerElement = document.querySelector('header');

  // Check if the header element was found
  if (headerElement) {
    // Update the text color to red
    headerElement.style.color = '#FF0000';
  } else {
    console.error("The <header> element was not found in the document.");
  }
});
