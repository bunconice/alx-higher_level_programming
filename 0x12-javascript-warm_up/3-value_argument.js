#!/usr/bin/node
const numArgv = process.argv[2];
if (numArgv === undefined) {
  console.log('No argument');
} else {
  console.log(numArgv);
}
