#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  let x;

  for (x = 0; x < argv[2]; x++) {
    console.log('C is fun');
  }
}
