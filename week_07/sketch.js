var capture1;
var capture2;
var w = 640,
    h = 480;
var img;
var tracker;

function setup() {

  createCanvas(w*2, h);

  capture1 = createCapture(VIDEO);  // capture video
  capture2 = capture1;

  capture1.hide();
  capture1.size(w, h);

  colorMode(HSB);

  tracker = new clm.tracker();
  tracker.init(pModel);
  tracker.start(capture1.elt);
}

function draw() {
  image(capture1, 0, 0, 640, 480);
  filter('GRAY');
  image(capture2, 640, 0, 640, 480);

  var positions = tracker.getCurrentPosition();

  noFill();
  stroke(255);
  beginShape();
  for (var i = 0; i < positions.length; i++) {
      vertex(positions[i][0], positions[i][1]);
  }
  endShape();

  noStroke();
  for (var i = 0; i < positions.length; i++) {
      fill(map(i, 0, positions.length, 0, 360), 50, 100);
      ellipse(positions[i][0], positions[i][1], 4, 4);
      text(i, positions[i][0], positions[i][1]);
  }
  fill(0);
  textSize(25);
  text('NOW SMILE', 50, 50);

  if (positions.length > 0) {
      var mouthLeft = createVector(positions[44][0], positions[44][1]);
      var mouthRight = createVector(positions[50][0], positions[50][1]);
      var smile = mouthLeft.dist(mouthRight);

      if (smile > 90) {
        capture1 = takePhoto();
      }
  }
}

function takePhoto() {
    capture1.loadPixels();
}
