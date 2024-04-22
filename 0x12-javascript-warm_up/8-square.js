#!/usr/bin/node

const { argv } = require('node:process')

const length = argv.length

if (length === 0 || isNaN(parseInt(argv[2]))) {
	console.log('Missing size');
} else {
	let x, y;
	let line = 'X';

	for (x = 0; x < length; x++) {
		for (y = 0; y < length - 1; y++) {
			line += 'X';
		}
		console.log(line);
	}
}
