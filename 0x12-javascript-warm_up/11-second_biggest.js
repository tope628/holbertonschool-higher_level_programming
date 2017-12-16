#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  let argSort = args.sort();
  console.log(argSort[(args.length - 2)]);
}
