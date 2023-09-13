#!/usr/bin/node

exports.logMe = function (item) {
  if (this.c === undefined) {
    this.c = 0;
  }
  console.log(this.c + ': ' + item);
  this.c++;
};
