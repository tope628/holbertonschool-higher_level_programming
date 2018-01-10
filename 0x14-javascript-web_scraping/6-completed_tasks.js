#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let info = JSON.parse(body);
    let myDict = {};
    for (let i in info) {
      let x = info[i];
      if (x.completed) {
        if (x.userId in myDict) {
          myDict[x.userId]++;
        } else {
          myDict[x.userId] = 1;
        }
      }
    }
    console.log(myDict);
  }
}
request(url, callback);
