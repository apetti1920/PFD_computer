// Attaching js code to the canvas by using a sketch object

var sketch2 = new Processing.Sketch();
sketch2.use3DContext = false;
// attach function (also, can be specified as the single parameter
// in the Processing.Sketch object constructor)
sketch2.attachFunction = function(processing) {

    socket.on('my event', function(data) {
        processing.redraw()
    });

    processing.setup = function() {
      processing.size(150, 300, processing.P3D);

      processing.background(255);
      processing.noLoop();
    };

    processing.draw = function() {
        processing.background(255);
        var depth = globaldata['data']['depth'];
        processing.rect(processing.width/2-50, processing.height-depth, 100, depth);
        var x = processing.map(globaldata['data']['depth'], 0, processing.height, 0, 255);
        processing.fill(x, 255-x, 0);
    };
};

var canvas = document.getElementById("depth_canvas");
// attaching the sketch to the canvas
var p = new Processing(canvas, sketch2);