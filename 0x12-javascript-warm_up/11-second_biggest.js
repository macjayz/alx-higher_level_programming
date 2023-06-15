#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv
    .slice(2, process.argv.length)
    .map(Number)
    .filter(num => !isNaN(num))
    .sort((a, b) => a - b);

  if (args.length < 2) {
    console.log('Insufficient numeric inputs. Please provide at least two valid numbers.');
  } else {
    console.log(args[args.length - 2]);
  }
}
