#!/usr/bin/node
const length = parseInt(process.argv[2]);
if (!length) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    let y = 0;
    let myVar = '';

    while (y < length) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
