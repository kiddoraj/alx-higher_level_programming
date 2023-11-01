// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Add a click event handler to the document to handle clicks on the specified div elements
  $(document).on('click', 'div#add_item', function() {
    // Add a new <li> element to the UL with class "my_list"
    $('ul.my_list').append('<li>Item</li>');
  });

  $(document).on('click', 'div#remove_item', function() {
    // Remove the last <li> element from the UL with class "my_list"
    $('ul.my_list li:last').remove();
  });

  $(document).on('click', 'div#clear_list', function() {
    // Remove all <li> elements from the UL with class "my_list"
    $('ul.my_list').empty();
  });
});
