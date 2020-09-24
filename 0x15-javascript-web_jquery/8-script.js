#!/usr/bin/node
/* etches and lists all movies title by using this
URL: https://swapi-api.hbtn.io/api/films/?format=json */
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const i in data.results) {
    $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
