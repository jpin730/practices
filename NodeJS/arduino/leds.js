var jf = require("johnny-five")
var board = new jf.Board()
var ledPort = 13
var blinkPeriod = 500

board.on("ready", start)

function start() {
  var led = new jf.Led(ledPort)
  led.blink(blinkPeriod)
}