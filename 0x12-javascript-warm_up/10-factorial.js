#!/usr/bin/node

const { argv } = require('process');

function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return (n * factorial(n - 1));
}

const num = parseInt(argv[2]);

console.log(factorial(num));
