#!/usr/bin/node

const request = require('request');

const url = 'http://swapi.co/api/films/' + process.argv[2];

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    var info = JSON.parse(body);
    console.log(info.title);
  }
}

request.get(url, callback);
