const socket = io.connect('http://' + "127.0.0.1" + ':' + 5000);
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});
socket.on('message', function(data) {
    console.log(data)
});


function buttonclick() {
    const elem = document.getElementById("arm_button");
    if (elem.innerHTML == 'Arm Device'){
        socket.emit('button click', {data: 'Arm'});
        elem.innerHTML = 'Disarm Device'
    }
    else if (elem.innerHTML == 'Disarm Device'){
        socket.emit('button click', {data: 'Disarm'});
        elem.innerHTML = 'Arm Device'
    }
}