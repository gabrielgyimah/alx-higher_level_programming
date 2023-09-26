#!/usr/bin/node
// Writes a string to a file.

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];


try {
    fs.writeFileSync(file, content, 'utf-8')
} catch (error) {
    console.log(error);
}