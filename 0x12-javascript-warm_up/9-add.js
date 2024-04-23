#!/usr/bin/node

const { argv } = require('node:process')


function add (a, b) {
	return parseInt(a) + parseInt(b);
}

if (argv.length < 3 || argv.length < 3 || isNaN(argv[2]) || isNaN(argv[3])) {
	console.log('NaN');

} else {
	let x = argv[2];
	let y = argv[3];
	console.log(add(x, y));
}

