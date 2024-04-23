#!/usr/bin/node

const { argv } = require('node:process');

const count = argv.length;
let x;
let firstG = 0;
let secondG = 0;

if (count <= 3) {
  console.log(0);
} else {
  for (x = 2; x < count + 2; x++) {
    if (argv[x] > firstG) {
      firstG = argv[x];
    }
  }
  for (x = 2; x < count + 2; x++) {
    if (argv[x] > secondG && argv[x] < firstG) {
      secondG = argv[x];
    }
  }

  console.log(secondG);
}
