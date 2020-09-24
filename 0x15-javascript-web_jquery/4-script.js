#!/usr/bin/node
/* toggles the class of the HTML tag HEADER to red */
const $ = window.$;
$('div#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
