import socket
from threading import Thread
import json


class Server():
    def __init__(self, sockio):
        self.sockio=sockio
        self.conn, self.addr = self.start_server()
        self.t1 = Thread(target=self.server_listen)
        self.t1.start()

    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 50000))
        s.listen(1)
        conn, addr = s.accept()
        return conn, addr

    def server_listen(self):
        while 1:
            data = self.conn.recv(1024)
            if not data:
                print('not data')
                break

            self.sockio.emit('my event', json.loads(data.decode('utf8')))
            print(data)

        self.conn.close()

    def server_send(self, message):
        t1 = Thread(target=self.conn.sendall, args=(message,))
        t1.start()