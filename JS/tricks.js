// console print abbr
const c = console.log;

// invert string
const invertString = string => string.split('').reverse().join('');

// sort array by numeric value
const sortNumbers = array => array.sort((a,b) => a - b);

// remove duplicates
const removeDuplicates = array => [...new Set(array)];

// random number between two numbers regardless max or min order
function randomBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}