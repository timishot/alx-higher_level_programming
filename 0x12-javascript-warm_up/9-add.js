#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  const c = a + b;
  console.log(c);
}

const num = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

add(num, num2);
