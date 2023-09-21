#!/usr/bin/node

const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('Not a number');
} else {
  const num = Number(argv[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + String(parseInt(num, 10)));
  }
}
