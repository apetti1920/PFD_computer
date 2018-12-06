import socket
from threading import Thread, Event
import json


class Server():
    def __init__(self, sockio, eventlist):
        self.sockio=sockio
        self.arm = eventlist[0]
        self.disarm = eventlist[1]
        self.conn: socket = socket.socket()
        self.addr: (str, int) = ('', 50000)
        self.start_server()


    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 50000))
        s.listen(1)
        print('server lsitening')
        self.conn, self.addr = s.accept()
        print('Server got Connection')
        t1 = Thread(target=self.server_listen)
        t1.start()
        t2 = Thread(target=self.wait_for_flag)
        t2.start()

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

    def wait_for_flag(self):
        while True:
            if self.arm.isSet():
                self.server_send('Arm'.encode('utf8'))
                self.arm.clear()
            elif self.disarm.isSet():
                self.server_send('Disarm'.encode('utf8'))
                self.disarm.clear()