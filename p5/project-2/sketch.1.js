var a = function( p ) { // p could be any variable name
  let leftscore = 0;
  let rightscore = 0;

  p.setup = function() {
    p.createCanvas(800, 500);
    p.background(bgColor);
    p.noStroke();
    p.frameRate(100);
    p.ellipseMode(p.RADIUS);
    // Set the starting position of the shape
    xpos = p.width / 2;
    ypos = p.height / 2;
  };

  p.start = true;

  p.draw = function() {
    p.background('black');
    for (var i = 10; i <= 500; i += 20) {
      p.strokeWeight(3);
      p.stroke('white');
      p.line(p.width/2,i,p.width/2,i - 10); 
      }
    p.noStroke();
    p.paddle();
    p.textSize(32);
    p.text(leftscore, 50, 40);
    p.text(rightscore, p.width-64, 40);
    if (p.start) {
        rectA_color = p.color('white');
        p.start = false;
      }
    if(begin == 1 && leftscore < 10 && rightscore < 10) {
      p.ball()
      }
    if (leftscore >= 10) {
      p.text('leftplayer wins', p.width/2 -100, 40);
      p.text('press "a" to play again', p.width/2 -100, 80);
      p.keyTyped()
      }
    if (rightscore >= 10) {
      p.text('rightplayer wins', p.width/2 -100, 40);
      p.text('press "a" to play again', p.width/2 -100, 80);
      }
  }
  begin = 0;
  p.keyTyped = function() {
    if (p.key === 'a') {
      begin = 1;
      p.clear()
      p.start = true;
      leftscore = 0;
      rightscore = 0;
      p.background('black');
      p.noStroke();
      p.paddle();
      p.textSize(32);
      p.text(leftscore, 50, 40);
      p.text(rightscore, p.width-64, 40);
      if (p.start) {
          rectA_color = p.color('white');
          p.start = false;
      }
    }
  } 
  // Ball Code

  var rad = 10; // Width of the shape ball
  var xpos, ypos; // Starting position of ball
  var xspeed = 3.8; // Speed of the ball
  var yspeed = 3.2; // Speed of the ball
  var xdirection = 1; // Left or Right(ball)
  var ydirection = 1; // Top to Bottom(ball)
  var bgColor = 'black'; // background color

  p.reset = function() {
    xpos = p.width / 2;
    ypos = p.height / 2;
    
    xpos = xpos + xspeed * xdirection;
    ypos = ypos + yspeed * ydirection;
    p.ellipse(xpos, ypos, rad, rad);
    
    }

    p.ball = function()  {
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
    if (xpos - rad <= paddleX1 + paddleWidth) {
          if (ypos >= paddleY1 && ypos <= paddleY1 + paddleHeight) {
            xdirection *= -1;	    		
        }
      }

    
    if (xpos > p.width - rad) {
      p.reset() //resets to center if ball goes out of screen
      leftscore++;
    }
      if (xpos < rad) {
      p.reset() //resets to center if ball goes out of screen
      rightscore++;
    }
    
    if (ypos > p.height - rad || ypos < rad) {
      ydirection *= -1;
    }
  
    p.ellipse(xpos, ypos, rad, rad); // Draw the ball
    
  }

  /// paddle functions
  var paddleX = 770; //x starting position paddle
  var paddleY = 10;  // y starting position paddle
  var paddleX1 = 20; //x starting position paddle
  var paddleY1 = 10;  // y starting position paddle
  var paddleWidth = 15; //paddle width
  var paddleHeight = 75; // paddle height
  var rectA_color = 0;

  p.paddle = function() {

    p.fill(bgColor);
    p.rect(paddleX, paddleY, paddleWidth, paddleHeight);
    p.rect(paddleX1, paddleY1, paddleWidth, paddleHeight);
  
    if (p.keyIsDown(80)) {
      paddleY = p.constrain(paddleY, 0 , p.height-paddleHeight); //prevents paddle from going out of screen
      paddleY -= 8;  //speed of up
    } else if (p.keyIsDown(76)) {
      paddleY = p.constrain(paddleY, 0 , p.height-paddleHeight); //prevents paddle from going out of screen
      paddleY += 8;  //speed of down
    }
    if (p.keyIsDown(87)) {
      paddleY1 = p.constrain(paddleY1, 0 , p.height-paddleHeight); //prevents paddle from going out of screen
      paddleY1 -= 5;  //speed of up
    } else if (p.keyIsDown(83)) {
      paddleY1 = p.constrain(paddleY1, 0 , p.height-paddleHeight); //prevents paddle from going out of screen
      paddleY1 += 5;  //speed of down
    }
  
    p.key = '';
    p.fill(rectA_color);
    p.rect(paddleX, paddleY, paddleWidth, paddleHeight);
    p.rect(paddleX1, paddleY1, paddleWidth, paddleHeight);
  }



}
var myp5 = new p5(a, 'my-sketch');