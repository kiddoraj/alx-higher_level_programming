#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer or equal to 0
      return {};
    }
  }

  print() {
    // Check if width or height is 0 or not a positive integer
    if (this.width === 0 || this.height === 0) {
      return;
    }

    // Loop through rows and columns to print the rectangle
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate() {
    // Swap the width and height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Double the width and height of the rectangle
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
