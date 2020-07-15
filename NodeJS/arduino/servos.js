var jf = require("johnny-five")
var board = new jf.Board()

var led, servo, analogInput
var ledPort = 13
var ledPort = 9
var servoPosition = 180

board.on("ready", start)

function start() {
  var analogInputSetup = {pin: "A0", freq: 50}
  analogInput = new jf.Sensor(analogInputSetup)

  led = new jf.Led(ledPort)
  led.on()

  servo = new jf.Servo(servoPort)
  servo.to(servoPosition)

  move()
}

function move() {
  console.log("Analog input value: " + analogInput.value)
  setTimeout(move, 1000)
}