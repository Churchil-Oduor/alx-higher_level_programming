#!/usr/bin/node

const { argv } = require('node:process')

let value = parseInt(argv[2])

if (isNaN(value)) {
	console.log('Not a number')
} else {
	console.log(value)
}
