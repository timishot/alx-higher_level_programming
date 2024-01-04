#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const count = filmsData.reduce((acc, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        return acc + 1;
      }
      return acc;
    }, 0);
    console.log(count);
  } else {
    console.error(`Error: ${response && response.statusCode}`);
  }
});
