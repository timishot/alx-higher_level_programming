#!/usr/bin/node

const { argv } = require('process');

const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else if (argv.length === 3) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
