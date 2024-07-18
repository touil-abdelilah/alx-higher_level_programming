#!/usr/bin/node

// Wait for the document to be ready before executing the code
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  // Attach a click event handler to the <input> element with ID "btn_translate"
  $('INPUT#btn_translate').click(function () {
    // When clicked, make an HTTP GET request to fetch greeting data based on the language code input
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // When the request is successful, set the HTML content of the <div> element with ID 'hello' to the greeting received
      $('DIV#hello').html(data.hello);
    });
  });
});
