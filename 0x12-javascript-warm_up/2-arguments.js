#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length >= 3) {
    console.log('Argument found');
}
