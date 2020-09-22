#!/usr/bin/node
/* prints the title of a Star Wars movie
 * where the episode number matches a given integer*/

const request = require('request');
let episodeNumber = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episodeNumber;
request(url, function (error, response) {
	if (error){
		console.log(error);
	}
	{
		console.log('code: ' + response.statusCode);
	}
	console.log(JSON.parse(body).title);
});
