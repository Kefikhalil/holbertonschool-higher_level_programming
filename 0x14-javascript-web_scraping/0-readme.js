#!/usr/bin/node
/*reads and prints the content of a file*/
const filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

