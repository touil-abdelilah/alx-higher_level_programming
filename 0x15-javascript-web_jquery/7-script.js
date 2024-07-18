#!/usr/bin/node

// Make an HTTP GET request to fetch data from the Star Wars API for the character with ID 5
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  // When the request is successful, set the text content of the <div> element with ID 'character' to the character's name
  $('DIV#character').text(data.name);
});
