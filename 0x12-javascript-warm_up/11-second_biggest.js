#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) {
  console.log(0);
} else if (argv.length > 2) {
  let temp = 0;
  let before = 0;
  for (let i = 0; i < argv.length - 2; i++) {
    if (argv[2 + i] > temp) {
      before = temp;
      temp = argv[2 + i];
    }
  }
  console.log(before);
}
