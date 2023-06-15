#!/usr/bin/node
const length = parseInt(process.argv[2]);
if (!length) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < length; i++) {
    console.log('C is fun');
  }
}
