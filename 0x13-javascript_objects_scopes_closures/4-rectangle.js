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

  rotate () {
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
