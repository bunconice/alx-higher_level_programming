#!/usr/bin/node
const arg = process.argv[2];

if (Number.isInteger(+arg)) {
  for (let index = 0; index < (+arg); index++) {
    let p = '';
    for (let a = 0; a < (+arg); a++) {
      p += 'x';
    }
    console.log(p);
  }
} else {
  console.log('Missing size');
}
