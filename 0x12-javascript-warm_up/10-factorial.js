#!/usr/bin/node

const { argv } = require('node:process')

function factorial (x) {

	if (isNaN(x)) {
		return -1;
	}else if (parseInt(x) === 1) {
		return 1;
	} else {
		return x * factorial(x - 1);
	}
}

if (factorial(argv[2]) === -1) {
	console.log(1);
} else {
	console.log(factorial(argv[2]));
}
