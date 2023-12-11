#!/usr/bin/node
const x = process.argv[2];
// Convert the first argument to an integer
const convertedNumber = parseInt(x);
if (!isNaN(convertedNumber)) {
  let i = 0;
  while (i < convertedNumber) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
