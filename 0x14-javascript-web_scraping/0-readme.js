#!/usr/bin/node

require('fs').readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
