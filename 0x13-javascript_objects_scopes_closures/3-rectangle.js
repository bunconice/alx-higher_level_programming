#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      let p = '';
      for (let i = 0; i < this.width; i++) {
        p += 'X';
      }
      console.log(p);
    }
  }
}
module.exports = Rectangle;
