const socket = io.connect('http://' + "127.0.0.1" + ':' + 5000);
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});
socket.on('message', function(data) {
    console.log(data)
});


function buttonclick() {
    const elem = document.getElementById("arm_button");
    if (elem.innerHTML === 'Arm Device'){
        b1 = document.getElementById("bladder1").value;
        b2 = document.getElementById("bladder2").value;
        b3 = document.getElementById("bladder3").value;
        b4 = document.getElementById("bladder4").value;

        data = {data: 'Arm', times: {B1: b1, B2: b2, B3: b3, B4: b4}};
        socket.emit('button click', data);
        elem.innerHTML = 'Disarm Device';
    }
    else if (elem.innerHTML === 'Disarm Device'){
        socket.emit('button click', {data: 'Disarm'});
        elem.innerHTML = 'Arm Device';
    }
}