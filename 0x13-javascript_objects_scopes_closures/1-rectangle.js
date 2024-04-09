#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If either width or height is invalid, set both to 0
      this.width = 0;
      this.height = 0;
    } else if (h === undefined) {
      // If only one argument is provided, set both width and height to the same value
      this.width = w;
      this.height = w;
    } else {
      // Otherwise, initialize width and height with provided values
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
