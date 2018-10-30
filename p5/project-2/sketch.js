
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

// My Sketch
var z = function( p ) { // p could be any variable name
  p.setup = function() {
    p.createCanvas(1100, 350);
    p.background(204);
  };

    p.draw = function() {
    //background
    p.background('white');
    //sky
    p.stroke(135,206,250);
    p.fill(135,206,250);
    p.rect(0,0,1100,150);
    //land
    p.stroke(139,69,19);
    p.fill(139,69,19);
    p.rect(0,150,1100,200);
    //road
    p.stroke('black');
    p.fill('black');
    p.quad(540,150,560,150,590,350,510,350);
    
    //road dash
    for (var i = 170; i <= 350; i += 20) {
      p.stroke('yellow');
      p.line(550,i,550,i - 10); 
    }

    var d = 20
    var z = 15
    var y = 25
    //Top Cloud Loop
    for (var i = 25; i <= 1025; i += 500) {
      p.stroke('white');
      p.fill('white');
      p.ellipse(i, y, d, d);
      p.ellipse(i+z, y-5, d, d);
      p.ellipse(i+z, y+5, d, d);
      p.ellipse(i+(z*2), y-5, d, d);
      p.ellipse(i+(z*2), y+5, d, d);
      p.ellipse(i+45,y,d,d);
  }    
   //Bottom Cloud Loop
    var y = 45
    for (var i = 275; i <= 775; i += 500) {
      p.stroke('white');
      p.fill('white');
      p.ellipse(i, y, d, d);
      p.ellipse(i+z, y-5, d, d);
      p.ellipse(i+z, y+5, d, d);
      p.ellipse(i+(z*2), y-5, d, d);
      p.ellipse(i+(z*2), y+5, d, d);
      p.ellipse(i+45,y,d,d);
  } 

    //Mountain 1
    
    for (var i = 75; i < 1000; i += 75) {
      p.stroke(139,69,19);
      p.fill('tan');
      p.triangle(i,75,i+75,150,i-75,150);
      p.fill('white');
      p.triangle(i,75,i+15,90,i-15,90);
   }
    }
  }
var myp5 = new p5(z, 'sketch-holder-third-row');