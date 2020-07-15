// TRICK: console shortcut
const c = console.log;

// get canvas from html
var d = document.getElementById("drawing");
var canvas = d.getContext("2d"); // 2d canvas
var width = d.width; // canvas width

// get inputs from html: LINES NUMBER and SUBMIT BUTTON
var linesNumber = document.getElementById("number");
var button = document.getElementById("submit");
// click event for submit button
button.addEventListener("click",strokeOnClick);

// fn to plot line
function strokeLine(color, xInitial, yInitial, xFinal, yFinal) {
  canvas.beginPath();
  canvas.strokeStyle = color;
  canvas.moveTo(xInitial, yInitial);
  canvas.lineTo(xFinal, yFinal);
  canvas.stroke();
  canvas.closePath();
}

// fn to plot lines pattern when click submit button
function strokeOnClick() {
  d.width = d.width; // TRICK: to clean canvas
  var canvasColor = "red";
  var borderColor = canvasColor;
  var lines = parseInt(linesNumber.value);
  for(let i = 0; i < 300; i+=width/lines) {
     strokeLine(canvasColor, i, 0, 300, i+width/lines);
  }
  // plot borders
  strokeLine(borderColor,   1,   1, 299,   1) // up
  strokeLine(borderColor, 299, 299, 299,   1) // right
  // strokeLine(borderColor, 299, 299,   1, 299) // down
  // strokeLine(borderColor,   1,   1,   1, 299) // left
 }