#!/usr/bin/node

const request = require('request');

const options = {
  url: 'http://swapi.co/api/films'
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    const character = 'https://swapi.co/api/people/18/';
    let count = 0;
    for (let i = 0; i < info.results.length; i++) {
      if (info.results[i].characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
}

request(options, callback);
