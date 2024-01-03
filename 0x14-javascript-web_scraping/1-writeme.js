#!/usr/bin/node
const fs = require('fs');

// Check if the correct numner of arguments is provides

if (process.argv.length !== 4) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to file', err);
  } else {
    console.log(filePath);
  }
});
