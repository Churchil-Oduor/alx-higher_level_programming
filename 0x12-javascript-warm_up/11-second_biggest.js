#!/usr/bin/node

const { argv } = require('node:process');

const count = argv.length;
let x;
let greatest = 0;

if (count <= 3) {
  console.log(0);
} else {
  for (x = 3; x < count + 3; x++) {
    if (argv[x] > greatest) {
      greatest = argv[x];
    }
  }
  console.log(greatest);
}
