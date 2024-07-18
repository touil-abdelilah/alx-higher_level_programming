#!/usr/bin/node

// Wait for the document to be ready before executing the code
$('document').ready(function () {
  // Attach a click event handler to the <input> element with ID "btn_translate"
  $('INPUT#btn_translate').click(translate);

  // Attach a focus event handler to the <input> element with ID "language_code"
  $('INPUT#language_code').focus(function () {
    // Attach a keydown event handler to the focused <input> element
    $(this).keydown(function (e) {
      // Check if the Enter key (key code 13) is pressed
      if (e.keyCode === 13) {
        // Call the translate function when Enter key is pressed
        translate();
      }
    });
  });
});

// Function to perform translation
function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  // Make an HTTP GET request to fetch greeting data based on the language code input
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    // When the request is successful, set the HTML content of the <div> element with ID 'hello' to the greeting received
    $('DIV#hello').html(data.hello);
  });
}
