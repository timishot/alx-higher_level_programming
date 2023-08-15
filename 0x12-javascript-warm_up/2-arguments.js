#!/usr/bin/node

const { argv } = require('process');//import

if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argmuent found');
}
