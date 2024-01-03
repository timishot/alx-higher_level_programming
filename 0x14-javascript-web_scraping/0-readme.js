#!/usr/bin/node
const { error } = require('console');
const fs = require('fs');

// Check if the correct numner of arguments is provides
if (process.argv.length !== 3){
	console.error('Usage: node 0-readme.js <file-path>');
	process.exit(1)
}

const filePath = process.argv[2];

//Read the content of the file in utf-8
try {
	const data = fs.readFileSync(filePath, 'utf-8');
	console.log(data);
} catch (error) {
	console.error(error)
}
