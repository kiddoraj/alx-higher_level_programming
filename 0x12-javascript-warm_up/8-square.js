#!/usr/bin/node

const arg1 = process.argv[2];
const size = parseInt(arg1, 10);

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log("Missing size");
  }
} else {
  console.log("Missing size");
}
