//Team Calculator - Andrew Jiang, William Li
//SoftDev -- K27: Guarding Against Burnout - DVD animation
//2021-05-10


//access canvas and buttons via DOM
var c = document.getElementById("playground")
var dotButton = document.getElementById("buttonCircle")// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop")// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d")// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "blue"// YOUR CODE HERE

var requestID;  //init global var for use with animation frames


var logo = new Image();
logo.src = "logo_dvd.jpeg"

//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;


var dvdSetUp = document.getElementById("DVDbutton")

xCoor = c.width/2
yCoor = c.height/2
xDirection = 9
yDirection = 6

var drawLogo = () => {
  clear();
  if(xCoor >= c.width-50 || xCoor < 0){
    xDirection*= -1
  }
  if(yCoor >= c.height-50 || yCoor < 0){
    yDirection*= -1
  }
  xCoor = xCoor + xDirection
  yCoor = yCoor + yDirection

  ctx.drawImage(logo, xCoor, yCoor, 50, 50);
  requestID = window.requestAnimationFrame(drawLogo)

}

//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...");
  clear();

  if (growing){
      radius += 1;
      if (radius == c.width/2){
          growing = false;
      }
  }else{
      radius -= 1;
      if (radius == 0){
          growing = true;
      }
  }

  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0 , 2 * Math.PI);
  ctx.stroke()
  console.log( requestID + "request ID");
  requestID = window.requestAnimationFrame(drawDot) //sets requestID as a unique number that represents the next frame. 
  //The window.requestAnimationFrame will recursively call the drawDot function. 
  //Unlike setTimeout or setInterval where you specify the time inbetween when the functions are called, requestAnimationFrame will run it the next time that the function can be called.
  
  
  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,

    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()

   */
};



//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);   //stops the animation at the next frame represented by the requestID variable

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation

    You will need
    window.cancelAnimationFrame()
  */
};

dvdSetUp.addEventListener("click", drawLogo)
dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );