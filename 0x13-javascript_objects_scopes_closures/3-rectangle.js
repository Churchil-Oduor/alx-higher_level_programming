#!/usr/bin/node

class Rectangle {
  width;
  height;
  constructor (w, h) {
    if ((!isNaN(w) && w > 0) && (!isNaN(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let line = '';
      for (let y = 0; y < this.width; y++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Rectangle;
