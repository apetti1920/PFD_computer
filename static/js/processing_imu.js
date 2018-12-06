// Attaching js code to the canvas by using a sketch object

var sketch = new Processing.Sketch();
var globaldata = {'data': {'depth': 0, 'IMUx': 0, 'IMUy': 0, 'IMUz': 0}};
// define 3D context
sketch.use3DContext = true;
// preload the image
// attach function (also, can be specified as the single parameter
// in the Processing.Sketch object constructor)
sketch.attachFunction = function(processing) {

    socket.on('my event', function(data) {
        globaldata = data;
        processing.redraw();
    });

    processing.setup = function() {
      processing.size(300, 300, processing.P3D);

      processing.background(255);
      processing.lights();
      processing.translate(processing.width / 2, processing.height / 2, -100);

      rotatePyrimid();

      processing.noLoop();
    };

    processing.draw = function() {

        processing.background(255);
        processing.lights();
        processing.translate(processing.width / 2, processing.height / 2, -100);

        rotatePyrimid();
    };

    function drawPyrimid() {
      processing.beginShape();
      processing.vertex(-100, -100, -100);
      processing.vertex( 100, -100, -100);
      processing.vertex(   0,    0,  100);
      processing.fill(0, 0, 0);
      processing.endShape();

      processing.beginShape();
      processing.vertex( 100, -100, -100);
      processing.vertex( 100,  100, -100);
      processing.vertex(   0,    0,  100);
      processing.fill(0, 255, 0);
      processing.endShape();

      processing.beginShape();
      processing.vertex( 100, 100, -100);
      processing.vertex(-100, 100, -100);
      processing.vertex(   0,   0,  100);
      processing.fill(0, 0, 255);
      processing.endShape();

      processing.beginShape();
      processing.vertex(-100,  100, -100);
      processing.vertex(-100, -100, -100);
      processing.vertex(   0,    0,  100);
      processing.fill(255, 0, 0);
      processing.endShape();

      processing.beginShape();
      processing.vertex(-100,  100, -100);
      processing.vertex(-100, -100, -100);
      processing.vertex( 100,  100, -100);
      processing.vertex( 100, -100, -100);
      processing.fill(255, 255, 102);
      processing.endShape();

    }

    function rotatePyrimid() {

            console.log(globaldata['data']);
            processing.rotateX(globaldata['data']['IMUx']);
            processing.rotateY(globaldata['data']['IMUy']);
            processing.rotateZ(globaldata['data']['IMUz']);
            processing.stroke(255);


            drawPyrimid();
    }
};

var canvas = document.getElementById("imu_canvas");
// attaching the sketch to the canvas
var p = new Processing(canvas, sketch);