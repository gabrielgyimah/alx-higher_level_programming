#!/usr/bin/node
// Prints the content of a file to the console

const fs = require('fs');
const file = process.argv[2];

try {
    const fileContent = fs.readFileSync(file, 'utf-8');
    console.log(fileContent);
} catch (error) {
    console.log(error)
}
