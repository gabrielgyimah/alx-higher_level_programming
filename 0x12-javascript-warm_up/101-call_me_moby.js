#!/usr/bin/node

exports.callMeMoby = function (x, printXTime) {
    let counter = 0;
  
    while (counter < x) {
        printXTime();
        counter++;
    }
};