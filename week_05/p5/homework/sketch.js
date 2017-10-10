var serial; // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbmodem1431';  // fill in your serial port name here
var redValue;
var greenValue;
var blueValue;
var myDotColor = ["0", "0", "0", "1.0"];
var ledColor = myDotColor;

function setup() {
  createCanvas(1200,800);
  background(0);

  serial = new p5.SerialPort();     // make a new instance of the serialport library
  serial.on('data', serialEvent);    // callback for when new data arrives
}

function draw() {
  fill(myDotColor);
  ellipse(600, 400, 80, 80);

  myDotColor = [redValue, greenValue, blueValue, "1.0"];
}

function serialEvent() {
  // read a string from the serial port
  // until you get carriage return and newline:
  var inString = serial.readStringUntil('\r\n');
  //check to see that there's actually a string there:
  if (inString.length > 0) {
    if (inString !== 'hello') {           // if you get hello, ignore it
      var colors = split(inString, ','); // split the string on the commas
      if (colors.length > 2) { // if there are three elements
        redValue = colors[0]; // element 0 is the red value
        greenValue = colors[1]; // element 1 is the green value
        blueValue = colors[2];      // element 2 is the blue value
      }
    }
    serial.write('x'); // send a byte requesting more serial data 
  }
}
