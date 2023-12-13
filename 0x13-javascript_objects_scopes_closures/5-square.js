#!/usr/bin/node
class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
