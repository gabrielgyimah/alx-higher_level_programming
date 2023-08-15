#!usr/bin/node

class Rectangle {
  w;
  h;

  constructor (w, h) {
    if (w < 1 || w === undefined || h < 1 || h === undefined) {
      const emptyRect = class Rectangle {};
      return new emptyRect();
    }

    this.width = w;
    this.height = h;
  }

  print () {
    let counter = 0;

    while (counter < this.height) {
      console.log('X'.repeat(this.width));
      counter++;
    }
  }
}

module.exports = Rectangle;
