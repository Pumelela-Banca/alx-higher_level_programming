#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    for (const charac of JSON.parse(body).characters) {
      req(charac, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
