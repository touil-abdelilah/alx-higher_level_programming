#!/usr/bin/node

// Wait for the DOM content to be fully loaded before executing the callback function
document.addEventListener('DOMContentLoaded', function () {
  // Set the color style of the <header> element to red (#FF0000)
  document.querySelector('HEADER').style.color = '#FF0000';
});
