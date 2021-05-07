//Team Calculator - Andrew Jiang, William Li
//SoftDev -- K26: They lock us in the tower whenever we get caught - using animationframe and animationcancel
//2021-05-04


//access canvas and buttons via DOM
var c = document.getElementById("playground")
var dotButton = document.getElementById("buttonCircle")// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop")// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d")// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "blue"// YOUR CODE HERE

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;


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


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );