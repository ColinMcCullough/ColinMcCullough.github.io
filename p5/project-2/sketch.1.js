var paddleX = 370; //x starting position paddle
var paddleY = 10;  // y starting position paddle
var paddleWidth = 10; //paddle width
var paddleHeight = 50; // paddle height
var rectA_color = 0;

var rad = 10; // Width of the shape ball
var xpos, ypos; // Starting position of ball

var xspeed = 3.8; // Speed of the ball
var yspeed = 3.2; // Speed of the ball

var xdirection = 1; // Left or Right(ball)
var ydirection = 1; // Top to Bottom(ball)
var bgColor = 'black'; // background color

/////////////////////////////////////////////////////////////////
 
function setup() {
  createCanvas(400, 400);
  background(bgColor);
  noStroke();
  frameRate(100);
  ellipseMode(RADIUS);
  // Set the starting position of the shape
  xpos = width / 2;
  ypos = height / 2;
}
  
/////////////////////////////////////////////////////


 
function paddle() {

  fill(bgColor);
  rect(paddleX, paddleY, paddleWidth, paddleHeight);
 
  if (keyIsDown(UP_ARROW)) {
    paddleY = constrain(paddleY, 0 , 350); //prevents paddle from going out of screen
    paddleY -= 5;  //speed of up
  } else if (keyIsDown(DOWN_ARROW)) {
    paddleY = constrain(paddleY, 0 , 350); //prevents paddle from going out of screen
    paddleY += 5;  //speed of down
  }
 
  key = '';
  fill(rectA_color);
  rect(paddleX, paddleY, paddleWidth, paddleHeight);
}
/////////////////////////////////////////
 
start = true;
 

function draw() {
  background('black');
  noStroke();
  paddle();
 
  if (start) {
    rectA_color = color('white');
    start = false;
  }

  // Update the position of the shape 
  
  xpos = xpos + xspeed * xdirection;
  ypos = ypos + yspeed * ydirection;

  // Test to see if the shape exceeds the boundaries of the screen
  // If it does, reverse its direction by multiplying by -1
	if (xpos + rad >= paddleX) {
				if (ypos >= paddleY && ypos <= paddleY + paddleHeight) {
	    		xdirection *= -1;
	    		
			}
    }
  if (xpos > width - rad || xpos < rad) {
    xdirection *= -1;
  }
  if (ypos > height - rad || ypos < rad) {
    ydirection *= -1;
  }

  // Draw the shape
  
  ellipse(xpos, ypos, rad, rad);
}





