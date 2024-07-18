#!/usr/bin/node

// Attach a click event handler to the <div> element with the ID "red_header"
$('DIV#red_header').click(function () {
  // When the <div> is clicked, add a class 'red' to the <header> element
  $('HEADER').addClass('red');
});
