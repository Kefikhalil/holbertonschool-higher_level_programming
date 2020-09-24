#!/usr/bin/node
/* fetches and replaces the name of this
URL: https://swapi-api.hbtn.io/api/people/5/?format=json */
const $ = window.$;
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
