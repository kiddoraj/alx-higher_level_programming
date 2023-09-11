#!/usr/bin/node

function computeFactorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

const arg1 = process.argv[2];
const num = parseInt(arg1, 10);

const factorial = computeFactorial(num);

console.log(factorial);
