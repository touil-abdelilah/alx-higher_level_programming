#!/usr/bin/node

// Attach a click event handler to the <div> element with the ID "toggle_header"
$('DIV#toggle_header').click(function () {
  // When the <div> is clicked, toggle between adding and removing classes 'green' and 'red' on the <header> element
  $('HEADER').toggleClass('green red');
});
