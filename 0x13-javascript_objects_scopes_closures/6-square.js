#!/usr/bin/node
class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
