var bugCollection = [];  // Declare object
var numBugs = 25;

function setup() {
  createCanvas(200, 200);
  
  
  for (var x = 0; x < numBugs; x++) {
  	bugCollection[x] = new Jitter();
  }

}



function draw() {
  background(50, 89, 100);
 
  for (var x = 0; x < numBugs; x++) {
  	bugCollection[x].move();
    bugCollection[x].display();
    
    var distance = dist(mouseX, mouseY, bugCollection[x].x, bugCollection[x].y);
  	
    if (distance <= bugCollection[x].diameter / 2) {
    	bugCollection[x].r  = 255;
          	bugCollection[x].g  = 0;
          	bugCollection[x].b  = 0;
    }
  }
 

}

// Jitter class
function Jitter() {
  this.x = random(width);
  this.y = random(height);
  this.diameter = random(10, 20);
  
  this.r = random(255);
  this.g = random(255);
  this.b = random(255);
  
  this.speed = 1;

  this.move = function() {
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  };

  this.display = function() {
    fill(this.r, this.g, this.b);
    ellipse(this.x, this.y, this.diameter, this.diameter);
  }
};