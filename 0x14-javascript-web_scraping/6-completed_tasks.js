#!/usr/bin/node

require('request')(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const done = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.completed[task.userID] === undefined) {
          done[task.userID] = 0;
        }
        done[task.userID] += 1;
      }
    }
    console.log(done);
  }
});
