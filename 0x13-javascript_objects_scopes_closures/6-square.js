#!/usr/bin/node

// Import the Square class from 5-square.js
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint(c) {
    // If c is undefined, use the character 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Loop through rows and columns to print the square with the specified character
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
