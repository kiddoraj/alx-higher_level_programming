#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const num1 = parseInt(arg1, 10);
const num2 = parseInt(arg2, 10);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log("Invalid input. Please provide two integers as arguments.");
}
