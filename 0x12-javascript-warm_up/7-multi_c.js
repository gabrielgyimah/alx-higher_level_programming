#!/usr/bin/node

const numberOfOccurences = parseInt(process.argv[2]);

if (!numberOfOccurences) {
    console.log('Missing number of occurrences');
}
else {
    let counter = 0;

    while (counter < numberOfOccurences) {
        console.log('C is fun');
        counter++;
    }
}