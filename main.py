from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from socket_server import Server
from threading import Thread, Event
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

arm = Event()
disarm = Event()

# noinspection PyTypeChecker
Thread(target=Server, args=(socketio, [arm, disarm])).start()
print('Thread Connection')


@app.route("/")
def index():
    return render_template("dashboard.html")


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('button click')
def handle_my_custom_event(json2):
    print(json2)
    if json2['data'] == 'Arm':
        arm.set()
    elif json2['data'] == 'Disarm':
        disarm.set()


if __name__ == '__main__':
    socketio.run(app)
