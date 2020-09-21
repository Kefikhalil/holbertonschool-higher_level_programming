#!/usr/bin/node
/* prints the number of arguments */

let a = 0;
exports.logMe = function (item) {
  console.log(a + ': ' + item);
  a++;
};
