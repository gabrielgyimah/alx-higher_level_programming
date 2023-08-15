#!/usr/bin/node

exports.esrever = function (list) {
  const tempArr = [];

  const reversetempArr = () => {
    let len = list.length - 1;

    while (len >= 0) {
      tempArr.push(list[len]);
      len--;
    }
  };

  reversetempArr();

  return tempArr;
};
