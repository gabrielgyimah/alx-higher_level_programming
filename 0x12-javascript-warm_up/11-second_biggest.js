#!/usr/bin/node

let firstBiggest = 0;
let secondBiggest = 0;
let counter = 2;

if ((process.argv.length - 2) < 2) {
    console.log(0);
}
else {
    while(counter < process.argv.length) {
        let num = parseInt(process.argv[counter]);

        if (num > firstBiggest) {
            secondBiggest = firstBiggest;
            firstBiggest = num;
        }
        else if (num > secondBiggest && num < firstBiggest) {
            secondBiggest = num;
        }
        
        counter++;
    }
    console.log(secondBiggest);
}