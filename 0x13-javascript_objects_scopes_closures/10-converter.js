#!/usr/bin/node
/* converts a number from base 10 to another base */
exports.converter = function (base) {
  return number => number.toString(base);
};
