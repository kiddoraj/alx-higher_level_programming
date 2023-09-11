#!/usr/bin/node

function findSecondLargest(args) {
  if (args.length <= 1) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i], 10);
    if (!isNaN(num)) {
      if (num > largest) {
        secondLargest = largest;
        largest = num;
      } else if (num > secondLargest && num !== largest) {
        secondLargest = num;
      }
    }
  }

  return secondLargest === -Infinity ? 0 : secondLargest;
}

const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args);

console.log(secondLargest);
