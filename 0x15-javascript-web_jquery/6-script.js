#!/usr/bin/node

// Attach a click event handler to the <div> element with the ID "update_header"
$('DIV#update_header').click(function () {
  // When the <div> is clicked, set the text content of the <header> element to 'New Header!!!'
  $('HEADER').text('New Header!!!');
});
