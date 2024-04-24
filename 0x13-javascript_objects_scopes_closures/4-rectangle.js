#!/usr/bin/node

class Rectangle {
  width;
  height;
  symbol;
  constructor (w, h) {
    if ((!isNaN(w) && w > 0) && (!isNaN(h) && h > 0)) {
      this.width = w;
      this.height = h;
      this.symbol = 'X';
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let line = '';
      for (let y = 0; y < this.width; y++) {
        line += this.symbol;
      }
      console.log(line);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
