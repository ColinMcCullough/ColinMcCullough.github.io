
// save this file as sketch.js
// Sketch One
var s = function( p ) { // p could be any variable name
  p.setup = function() {
    p.createCanvas(250, 250);
  };

  p.draw = function() {
    p.background(204);
    p.ellipse(50, 50, 80, 80);
  };
};
var myp5 = new p5(s, 'sketch-holder-left');

// Sketch Two
var t = function( p ) { // p could be any variable name
  p.setup = function() {
    p.createCanvas(400, 250);
    p.background(204);
  };

  p.draw = function() {
    if (p.mouseIsPressed) {
    p.fill(0);
    } else {
    p.fill(255);
    }
    p.ellipse(p.mouseX, p.mouseY, 80, 80);
    }
  }
var myp5 = new p5(t, 'sketch-holder-right');


// Sketch Three
var z = function( p ) { // p could be any variable name
    p.setup = function() {
      p.createCanvas(400, 250);
      p.background(204);
    };
  
    p.draw = function() {
      p.background(204);
      p.quad(158, 55, 199, 14, 392, 66, 351, 107);
      p.triangle(347, 54, 392, 9, 392, 66);
      p.triangle(158, 55, 290, 91, 290, 112);
      }
    }
  var myp5 = new p5(z, 'sketch-holder-leftone');

  // Sketch Four
var z = function( p ) { // p could be any variable name
  p.setup = function() {
    p.createCanvas(480, 250);
    p.background(204);
  };

  p.draw = function() {
    p.background(204);
    p.fill(255, 0, 0);
    p.ellipse(278, -100, 400, 400);
    p.fill(0, 0, 255); 
    p.ellipse(150, 100, 110, 110);
    p.fill(0, 255, 0); 
    p.ellipse(412, 60, 18, 18);
    }
  }
var myp5 = new p5(z, 'sketch-holder-rightone');

// Sketch Five
var z = function( p ) { // p could be any variable name
  p.setup = function() {
    p.createCanvas(1100, 350);
    p.background(204);
  };

  p.draw = function() {
    p.background('white');
    p.stroke(135,206,250);
    p.fill(135,206,250);
    p.rect(0,0,1100,150);
    p.stroke(139,69,19);
    p.fill(139,69,19);
    p.rect(0,150,1100,200);
    p.stroke('black');
    p.fill('black');
    p.quad(540,150,560,150,590,350,510,350);
    p.stroke('yellow');
    p.line(550,350,550,340);
    p.line(550,330,550,320);
    p.line(550,310,550,300);
    p.line(550,290,550,280);
    p.line(550,270,550,260);
    p.line(550,250,550,240);
    p.line(550,230,550,220);
    p.line(550,210,550,200);
    p.line(550,190,550,180);
    p.line(550,170,550,160);


    }
  }
var myp5 = new p5(z, 'sketch-holder-third-row');