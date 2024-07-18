#!/usr/bin/node

// Make an HTTP GET request to fetch data from the Star Wars API for the list of films
$.get('https://swapi.co/api/films/?format=json', function (data) {
  // When the request is successful, append <li> elements with the titles of each film to the <ul> with ID 'list_movies'
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
