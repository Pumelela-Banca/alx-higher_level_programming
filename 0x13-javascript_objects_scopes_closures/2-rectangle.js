#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w !== "number" || typeof w !== "number" ||
      w < 1 || h < 1) {
      return;   
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
