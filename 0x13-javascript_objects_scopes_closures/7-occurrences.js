#!/usr/bin/node
/* returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
	let Occurrences = 0;
	for (let Occurrences = 0; Occurrences < list.length; Occurrences++) {
		if (list[Occurrences] === searchElement){
			Occurrences++;
		}
	}
	return Occurrences;
};
