#!/usr/bin/node

require('request')(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    require('fs').writeFile(process.argv[3], body, 'utf-8', (err, data) => {
      if (err) {
        return console.log(err);
      }
    });
  }
});
