#!/usr/bin/node
// Get the first argument
const firstArgument = process.argv[2];

// Convert the first argument to an integer
const convertedNumber = parseInt(firstArgument);

// Check if the conversion was successful
if (!isNaN(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log('Not a number');
}
