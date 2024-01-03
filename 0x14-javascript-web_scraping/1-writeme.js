#!/usr/bin/node
const fs = require('fs');

// Check if the correct numner of arguments is provides

if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> "<string_to_write>"');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content written to ${filePath}`);
  }
});
