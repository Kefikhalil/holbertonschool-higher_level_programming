#!/usr/bin/node
/* prints a square */
const squaresize = parseInt(process.argv[2]);
let x;
if (isNaN(squaresize)) {
  console.log('Missing size');
} else {
  for (x = 0; x < squaresize; x++) {
    console.log('X'.repeat(squaresize));
  }
}
