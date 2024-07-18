#!/usr/bin/node

// Wait for the document to be ready before executing the code
$('document').ready(function () {
  // Attach a click event handler to the <div> element with ID "add_item"
  $('DIV#add_item').click(function () {
    // When clicked, append a new <li> element with text "Item" to the <ul> with class 'my_list'
    $('UL.my_list').append('<li>Item</li>');
  });

  // Attach a click event handler to the <div> element with ID "remove_item"
  $('DIV#remove_item').click(function () {
    // When clicked, remove the last <li> element from the <ul> with class 'my_list'
    $('UL.my_list li:last').remove();
  });

  // Attach a click event handler to the <div> element with ID "clear_list"
  $('DIV#clear_list').click(function () {
    // When clicked, empty the <ul> with class 'my_list' (remove all <li> elements)
    $('UL.my_list').empty();
  });
});
