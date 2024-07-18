#!/usr/bin/node

// Attach a click event handler to the <div> element with the ID "red_header"
$('DIV#red_header').click(function () {
  // When the <div> is clicked, change the color of the <header> element to red
  $('HEADER').css('color', '#FF0000');
});
