#!/usr/bin/node
/*  updates the text of the HTML tag HEADER to “New Header!!!”
 when the user clicks on DIV#update_header */
const $ = window.$;
$('div#update_header').click(function () {
  $('header').text('New Header!!!');
});
