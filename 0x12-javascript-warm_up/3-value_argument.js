#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];

if (arg1 === undefined) {
  console.log('No argument');
} else {
  console.log(arg1);
}
