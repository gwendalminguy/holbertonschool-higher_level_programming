#!/usr/bin/node

const { argv } = require('node:process');
const x = parseInt(argv[2]);

function recursion (n) {
  if (n > 1) {
    return n * recursion(n - 1);
  } else {
    return n;
  }
}

const result = recursion(x);
console.log(result);
