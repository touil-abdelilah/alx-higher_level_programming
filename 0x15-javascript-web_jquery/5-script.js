#!/usr/bin/node

// Attach a click event handler to the <div> element with the ID "add_item"
$('DIV#add_item').click(function () {
  // When the <div> is clicked, append a new <li> element with text "Item" to the <ul> with class 'my_list'
  $('UL.my_list').append('<li>Item</li>');
});

