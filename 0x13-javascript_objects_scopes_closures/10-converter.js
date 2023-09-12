#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return '';
    } else {
      return exports.converter(base)(Math.floor(number / base)) + (number % base).toString();
    }
  };
};
