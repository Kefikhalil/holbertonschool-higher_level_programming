#!/usr/bin/node
/* updates the text color of the HTML tag HEADER to red*/
const $ = window.$;
$("header").click(function(){
    $('#toggle_header').css("color", "#FF0000");
  });