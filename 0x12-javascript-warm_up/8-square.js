#!/usr/bin/node

const { argv } = require('node:process');

const length = argv.length;

if (length === 0 || isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  let x, y;
  let line = '';

  for (x = 0; x < argv[2]; x++) {
    for (y = 0; y < argv[2]; y++) {
      line += 'X';
    }
    console.log(line);
  }  
}
