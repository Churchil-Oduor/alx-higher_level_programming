#!/usr/bin/node

const SQR = require('./5-square');
class Square extends SQR {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      super.symbol = c;
      super.print();
    }
  }
}

module.exports = Square;
