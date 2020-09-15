#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */
const i = process.argv;
if (i.length <= 3) {
	console.log(0);
}
else
{
	console.log(i.slice(2).sort((a, b) => a - b).reverse()[1]);
}
