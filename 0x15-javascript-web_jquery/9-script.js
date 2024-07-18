#!/usr/bin/node

// Wait for the document to be ready before executing the code
$('document').ready(function () {
  // Make an HTTP GET request to fetch data from the API endpoint for French greeting
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // When the request is successful, set the text content of the <div> element with ID 'hello' to the greeting received
    $('DIV#hello').text(data.hello);
  });
});
