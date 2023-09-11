#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 4) {
  console.log(0);
} else {
  let big = Number.NEGATIVE_INFINITY;
  let second = big;
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > big) {
      second = big;
      big = parseInt(argv[i]);
    } else if (parseInt(argv[i]) > second) {
      second = parseInt(argv[i]);
    }
  }
  console.log(second);
}
