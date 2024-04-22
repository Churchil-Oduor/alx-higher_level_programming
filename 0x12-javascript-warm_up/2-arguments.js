#!/usr/bin/node

const { argv } = require('node:process');

// check to see if any argument is passed
const num = argv.length;

if (num === 3) {
  console.log('Argument found');
} else if (num > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
