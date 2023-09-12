#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of occurrences
  let count = 0;

  // Loop through the list and increment the counter for each matching element
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the final count of occurrences
  return count;
};
