#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let info = JSON.parse(body).results;
    let count = 0;
    for (let i of info) {
	for(let x of i.characters){  
	      if (x.endsWith('18/')) {
		count++;
		      break;
	      }
    }
    }
    console.log(count);
  }
}

request(url, callback);
