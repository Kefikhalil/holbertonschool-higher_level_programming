#!/usr/bin/node
/* returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
	let Occurrences = 0;
	for (const a of list) {
		if (a === searchElement){
			Occurrences++;
		}
	}
	return Occurrences;
};
