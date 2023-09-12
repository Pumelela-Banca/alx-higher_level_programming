#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if (typeof w !== 'number' || typeof w !== 'number' ||
        w < 1 || h < 1) {
        // do nothing
      } else if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }

    print () {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
};
