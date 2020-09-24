#!/usr/bin/node
/* that fetches from https://fourtonfish.com/hellosalut/?lang=fr 
and displays the value of hello f
rom that fetch in the HTML’s tag DIV#hello.*/
const $ = window.$;
$(document).ready(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
      $('div#hello').text(data.hello);
    });
  });