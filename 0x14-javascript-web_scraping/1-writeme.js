#!/usr/bin/node

const fs = ;
const file = process.argv[2];

require('fs').writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    return console.error(err);
  }
});
