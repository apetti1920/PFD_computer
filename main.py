from flask import Flask, render_template
from flask_socketio import SocketIO
from PFDSocket import PFDSocket
from threading import Thread, Event, Timer
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

def on_data(data):
    socketio.emit(data)


if __name__ == '__main__':
    arm = Event()
    disarm = Event()

    # noinspection PyTypeChecker
    sock = PFDSocket()
    sock.on('data', on_data)
    Thread(target=sock.server(), name="Server Thread").start()
    Thread(target=socketio.run, args=(app,), name="SocketIO Thread").start()
    Thread(target=webbrowser.open, args=('http://127.0.0.1:5000/',), name="Browser Thread").start()
