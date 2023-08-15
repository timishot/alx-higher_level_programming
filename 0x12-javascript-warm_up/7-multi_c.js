#!/usr/bin/node

const { argv } = require('process');

const num = parseInt(argv[2]);

if (argv.length <= 2) {
  console.log('Missing number of occurrences');
} else if (argv.length === 3) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
