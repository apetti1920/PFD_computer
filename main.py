from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from socket_server import Server
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def index():
    Thread(target=Server, args=(socketio,)).start()
    return render_template("client.html")


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('button click')
def handle_my_custom_event(json):
    print('received button click: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
