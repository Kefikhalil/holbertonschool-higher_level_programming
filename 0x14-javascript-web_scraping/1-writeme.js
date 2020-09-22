#!/usr/bin/node
/* writes a string to a file*/
const filename = process.argv[2];
const fs = require('fs');
const filecontent = process.argv[3];
fs.writeFile(filename, filecontent, 'utf-8', function (err) {
	if (err) {
		console.log(err);
	}
});
