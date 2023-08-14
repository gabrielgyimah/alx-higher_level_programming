#!/usr/bin/node

const sizeOfSquare = parseInt(process.argv[2]);

if (!sizeOfSquare) {
    console.log('Missing size');
}
else {
    let counter = 0;

    while (counter < sizeOfSquare) {
        console.log('x'.repeat(sizeOfSquare));
        counter++;
    }
}