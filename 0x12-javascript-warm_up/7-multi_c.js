#!/usr/bin/node
/* prints x times “C is fun” */
const xtimes = parseInt(process.argv[2]);
let x = 0;
for (x = 0; x < xtimes; x++) {
  console.log('C is fun');
}
