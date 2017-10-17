function setup() {
  createCanvas(400, 200);
  background(0);
  noStroke();
  fill(0, 255, 0);  
}

var ballX = 200;
var ballY = 100;

var ballXV = -4;
var ballYV = 1;

var rect1X = 10;
var rect1Y = 10;

var rect2X = 370;
var rect2Y = 10;

var p1 = 5;
var p2 = 5;

function draw() {
  fill(0, 255, 0); 
  rect(300,30,50,50);
  background(0);  
  setText();
  setShapes();
  keyboardMoved();    
  bounceCheck();
  increment();
  scoreCheck();  
}

function increment() {  
  ballX += ballXV;  
  ballY += ballYV;
  
  if(millis() % 1000 == 0) {
    ballXV = ballXV * 2;
  }
}

function keyboardMoved() {
  if (keyIsDown(16))
    rect1Y -= 5;
  if (keyIsDown(17))
    rect1Y += 5;
  if (keyIsDown(UP_ARROW))
    rect2Y -= 5;
  if (keyIsDown(DOWN_ARROW))
    rect2Y += 5;
}

function ball(x, y) {
  ellipse(x - 2, y, 30, 30);
  ellipse(x, y, 15, 15);
}

function setShapes() {
  fill(255);
  rect(rect1X, rect1Y, 20, 75);
  rect(rect2X, rect2Y, 20, 75);
  ball(ballX, ballY);
}

function sliderBounce() {
  // if(rect1Y < ballY && rect1Y + 100 > ballY) {
  //   ballXV = ballXV * -1;
  // }
  // if(rect2Y < ballY && rect2Y + 100 > ballY) {
  //   ballXV = ballXV * -1;
  // }
  if(rect1Y < ballY && rect1Y + 75 > ballY) {
    ballXV = ballXV * -1;
  }
  if(rect2Y < ballY && rect2Y + 75 > ballY) {
    ballXV = ballXV * -1;
  }
  // sets limit for bar distance

  if(rect1Y < -200) {
    rect1Y = -200;
  }
  if(rect1Y > 200) {
    rect1Y = 200;
  }
  if(rect2Y < -200) {
    rect2Y = -200;
  }
  if(rect2Y > 200) {
    rect2Y = 200;
  }
}

function bounceCheck() {
  if(ballY < 0 || ballY > 200) {
    ballYV = ballYV * -1;
  }
  
  if(ballX < 40 && ballXV < 0) {
    sliderBounce();
  }
  
  if(ballX > 360 && ballXV > 0) {
    sliderBounce();
  }
  
  if(ballX < 0) {
    ballX = 200;
    p1 -= 1;
  }

  if(ballX > 400) {
    ballX = 200;
    p2 -= 1;
  }
}

function scoreCheck() {
  if(p1 == 0) {
    //stop the ball
    ballXV = 0;
    ballYV = 0;
    result = "P2 WINS";
    setWinner();
  }
  if(p2 == 0) {
    //stop the ball
    ballXV = 0;
    ballYV = 0;
    result = "P1 WINS";
    setWinner();
  }
}

function setText() {
  textAlign(CENTER);
  textSize(22);
  text(p1, 180, 25);
  text(" - ", 200, 25);
  text(p2, 220, 25);
}

function setWinner() {
  fill(0, 255, 0);
  textAlign(CENTER);
  textSize(22);
  text(result, 200, 50);
}