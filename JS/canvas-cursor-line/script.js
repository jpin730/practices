// TRICK: console shortcut
const c = console.log;

// get canvas from html
var canvasArea = document.getElementById("drawingArea");
var canvas = canvasArea.getContext("2d"); // 2d canvas
var width = canvasArea.width; // canvas width

// key event for submit button
document.addEventListener("keyup",drawWithKey);

// fn to plot line
function drawLine(color, xInitial, yInitial, xFinal, yFinal, canvasObject) {
  canvasObject.beginPath();
  canvasObject.strokeStyle = color;
  canvasObject.lineWidth = 3;
  canvasObject.moveTo(xInitial, yInitial);
  canvasObject.lineTo(xFinal, yFinal);
  canvasObject.stroke();
  canvasObject.closePath();
}

// initial point
var x = 150; y = 150;
drawLine(canvasColor, x-1, y-1, x+1, y+1, canvas)

// fn to plot lines pattern when click submit button
function drawWithKey(keyEvent) {
  var increment = 10; // increment to plot
  var canvasColor = "red";
  const key = { // comparison object
    LEFT: 37,
    UP: 38,
    RIGHT: 39,
    DOWN: 40
  };
  // 
  switch (keyEvent.keyCode) {
    case key.LEFT:
      drawLine(canvasColor, x, y, x-increment, y, canvas);
      x -= increment;
      break;
    
    case key.UP:
      drawLine(canvasColor, x, y, x, y-increment, canvas);
      y -= increment;
      break;

    case key.RIGHT:
      drawLine(canvasColor, x, y, x+increment, y, canvas);
      x += increment;
      break;

    case key.DOWN:
      drawLine(canvasColor, x, y, x, y+increment, canvas);
      y += increment;
      break;

    default:
      break;
  }
  // plot borders
  // drawLine(borderColor,   1,   1, 299,   1) // up
  // drawLine(borderColor, 299, 299, 299,   1) // right
  // drawLine(borderColor, 299, 299,   1, 299) // down
  // drawLine(borderColor,   1,   1,   1, 299) // left
 }