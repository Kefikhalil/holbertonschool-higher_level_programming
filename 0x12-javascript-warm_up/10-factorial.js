#!/usr/bin/node
/* computes and prints a factorial */
const fac = process.argv[2];
function factorial (fac) {
  if (isNaN(fac) || fac === 1) {
    return (1);
  } else {
    return (fac * factorial(fac - 1));
  }
}
console.log(factorial(parseInt(fac)));
