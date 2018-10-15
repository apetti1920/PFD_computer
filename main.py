from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def ack():
    print('message was received!')

@app.route('/')
def index():
    return render_template('client.html')


@socketio.on('message')
def handle_message(message):
    print(message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, json=True, callback=ack)

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     send(json, json=True, callback=ack)

@socketio.on('connect')
def test_connect():
    send({'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)
