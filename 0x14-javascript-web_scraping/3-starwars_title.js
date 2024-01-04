#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Error: ${response && response.statusCode}`);
  }
});
