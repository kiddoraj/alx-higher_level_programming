// Use jQuery to wait for the document to be ready
$(document).ready(function() {
  // Attach a click event handler to the <div> with id "add_item"
  $("div#add_item").click(function() {
    // Create a new <li> element with the text "Item"
    const newItem = $("<li>Item</li>");
    
    // Append the new <li> element to the <ul> with class "my_list"
    $("ul.my_list").append(newItem);
  });
});
