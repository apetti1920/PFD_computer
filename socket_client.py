import socket
from threading import Thread
from random import randrange
import json
import time

class Client():
    def __init__(self):
        self.sock = self.start_client()

        t2 = Thread(target=self.client_listen)
        t2.start()

        while True:
            temp = self.read_sensors()
            j = json.dumps(temp)
            try:
                self.client_send(j)
                time.sleep(1)
            except Exception as e:
                print('error', e)


    def start_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 50000))

        return s

    def client_send(self, message):
        t1 = Thread(target=self.sock.sendall, args=(message,))
        t1.start()

    def client_listen(self):
        while True:
            data = self.sock.recv(1024)
            print(data)

    def read_sensors(self):
        return {'data': {'depth': randrange(0,100,2), 'IMUx': randrange(0,100,3), 'IMUy': randrange(0,100,2), 'IMUz': randrange(0,100,3)}}


if __name__ == '__main__':
    Client()
