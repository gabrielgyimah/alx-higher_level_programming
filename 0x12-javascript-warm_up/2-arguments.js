#!/usr/bin/node

const len = process.argv.length - 2;

if (len > 1) {
  console.log('Arguments found');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
