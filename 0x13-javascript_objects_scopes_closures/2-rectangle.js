#!/usr/bin/node

class Rectangle {
    w;
    h;

    constructor(w, h) {
        if (w < 1 || w === undefined || h < 1 || h === undefined) {
            const emptyRect = class Rectangle {};
            return new emptyRect();
        }

        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;