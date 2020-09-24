#!/usr/bin/node
/* adds the class red to the HTML tag HEADER to red */
const $ = window.$;
$('div#red_header').click(function () {
  $('header').addClass('red');
});
