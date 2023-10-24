#!/usr/bin/node

const url = process.argv[2];

require('request')(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let n = 0;
    for (const d of data) {
      const characters = d.characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
