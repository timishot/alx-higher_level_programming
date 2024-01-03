#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (!error && response.statusCode === 200) {
    console.log(response.statusCode);
  } else {
    console.error(response && response.statusCode);
  }
});
