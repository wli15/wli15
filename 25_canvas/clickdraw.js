//Team Calculator - Andrew Jiang, William Li
//SoftDev -- K25: I See a Red Door - javascript canvas work
//2021-05-04
var x = 0;
var y = 0;
var canvas = document.getElementById('slate');
    if (canvas.getContext) {
      var ctx = canvas.getContext('2d');
    }

function clear(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

var clearall = document.getElementById('clearall');
clearall.addEventListener('click', clear);


function toggleMode(){
    if (toggle.innerHTML == "dot"){
        toggle.innerHTML = "rect";
    } else{
        toggle.innerHTML = "dot";
    }
}

var toggle = document.getElementById("toggle")
toggle.addEventListener('click', toggleMode);


function recordCoor(event){
    x = event.offsetX; //get the x coor of where the mouse is relative to the canvas, not the page
    y = event.offsetY; //gets y coor
    console.log(x,y);

    if(toggle.innerHTML == "dot"){
        ctx.fillRect(x, y, 14,14);
        console.log("rectangle");
    }
    else{
        ctx.beginPath();        //establishes that drawing is about to begin mapping out a path
        ctx.arc(x,y,7,0, 2*Math.PI);    //outlines the circle path
        ctx.fill();
        ctx.stroke(); //actually draws based on previously established paths

        console.log("circ");
    }
}


//}


//canvas.addEventListener('onclick', draw());