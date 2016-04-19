void setup() {
  size(200, 200);
  background(100);
  stroke(255);
  ellipse(50, 50, 25, 25);
  println("hello web!");
  draw();
}

// <Description> Move Sprite forward based on rotational values using Sin and Cos </Description>

var TURTLE_SPEED = 2.0;
var TURTLE_ROTATION_SPEED = 2.4;
var turtle_Rotation = 0;

// Actual Cartesian X, Y Coordinates
var turtle_Position_X = 200;
var turtle_Position_Y = 200;

// Scaled Coordinates based on rotation
var turtle_X_Scale;
var turtle_Y_Scale;

// Amount to move each tick
var turtle_Velocity_X;
var turtle_Velocity_Y;

var updateTurtle = function(){
// Not really necessary. Rotation = 10,000 will work
// could maybe wig out if you drove in circles for hours
    if (turtle_Rotation > 360){ turtle_Rotation -= 360; }
    if (turtle_Rotation < 0){ turtle_Rotation += 360; }

// Amount to move in X and Y to correct Radial Coordinates
    turtle_Y_Scale = cos(turtle_Rotation);
    turtle_X_Scale = sin(turtle_Rotation);

// Now that weve Scaled X and Y, calculate distance per frame
    turtle_Velocity_X = (TURTLE_SPEED * turtle_X_Scale);
    turtle_Velocity_Y = (TURTLE_SPEED * turtle_Y_Scale);

// Move the turtle the correct distance in Cartesian Coordinates
    turtle_Position_X += turtle_Velocity_X;
    turtle_Position_Y -= turtle_Velocity_Y;

    // Optional - Keep Sprite onscreen
    if(turtle_Position_X > 410){ turtle_Position_X = -10; }
    if(turtle_Position_X < -10){ turtle_Position_X = 410; }
    if(turtle_Position_Y > 410){ turtle_Position_Y = -10; }
    if(turtle_Position_Y < -10){ turtle_Position_Y = 410; }
};

var drawTurtle = function(){
// Move Matrix 0,0 to Sprite Center
translate(turtle_Position_X, turtle_Position_Y); 
rotate(turtle_Rotation); // Rotate Matrix
scale(0.5, 0.5); // Resize Sprite to taste

// Draw Sprite centered at 0,0 instead of the middle of the screen
// set the color for the head, legs, and tail
stroke(102, 81, 67);
fill(0, 166, 0);

// head
// Note the X and Y coordinates are -200 from our original turtle
ellipse(0, -124, 83, 78);
// left feet
triangle(-88, -102, -117, -62, -62, -50);
triangle(-88, 94, -117, 56, -62, 38);
// right feet
triangle(88, -102, 117, -62, 62, -50);
triangle(88, 94, 117, 56, 62, 38);
// tail
triangle(-20, 100, 20, 100, 0, 172);
// eyes
fill(17, 34, 219);
ellipse(-27, -139, 10, 10);
ellipse(27, -139, 10, 10);
// shell
fill(13, 161, 0);
ellipse(0, 0, 200, 226);

// turn off outlines for the smaller shell ellipses
noStroke();
fill(167, 207, 20);
ellipse(0, 0, 169, 194);
fill(198, 250, 10);
ellipse(0, 0, 129, 149);
fill(231, 255, 46);
ellipse(0, 0, 82, 96);

resetMatrix();
};

// Use Arrow keys to control rotation
var keyPressed = function(){
   if(keyCode === LEFT) {
      turtle_Rotation -= TURTLE_ROTATION_SPEED;}
    if (keyCode === RIGHT) {
      turtle_Rotation += TURTLE_ROTATION_SPEED;} 
};

// Begin Game Loop
var draw = function () {
background(0, 0, 0);
fill(255, 0, 234);

text("Click inside Game window to activate Keyboard control", 40, 24); 
text("Use Right and Left Arrow keys to steer Turtle", 70, 43); 

updateTurtle();
drawTurtle();

}; // End Game Loop
// Tutorials in Plain English by Dillinger 2012
