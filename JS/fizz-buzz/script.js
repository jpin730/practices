var c = console.log;
var numbers = 100;

for (let i = 1; i <= numbers; i++) {
  if (i % 3 === 0 || i % 5 === 0) {
    if (i % 3 === 0) {
      document.write("Fizz ");
    }
    if (i % 5 === 0) {
      document.write("Buzz");
    }
    document.write("<br>");
  }
  else {
    document.write(i + "<br>");
  }
}
