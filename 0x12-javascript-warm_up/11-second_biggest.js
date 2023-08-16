#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) {
  console.log(0);
} else if (argv.length > 2) {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > largest) {
      secondLargest = largest;
      largest = argv[i];
    }
  }
  console.log(secondLargest);
}
