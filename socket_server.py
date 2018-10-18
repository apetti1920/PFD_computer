import socket
from threading import Thread
import json


class Server():
    def __init__(self, sockio):
        self.sockio=sockio
        self.conn: socket = socket.socket()
        self.addr: (str, int) = ('', 50000)
        self.start_server()


    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 50000))
        s.listen(1)
        self.conn, self.addr = s.accept()
        t1 = Thread(target=self.server_listen)
        t1.start()

    def server_listen(self):
        while 1:
            data = self.conn.recv(1024)
            if not data:
                self.conn.close()
                #send disconnected signal to webpage
                break

            self.sockio.emit('my event', json.loads(data.decode('utf8')))
            print(data)

        self.start_server()

    def server_send(self, message):
        t1 = Thread(target=self.conn.sendall, args=(message,))
        t1.start()