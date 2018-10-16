import socket
from threading import Thread
from random import randrange
import json
import time
import sys

from noise import pnoise1


class Client():
    def __init__(self):
        self.sock = self.start_client()
        self.frame = 0



        t2 = Thread(target=self.client_listen, daemon=True)
        t2.start()

        while True:
            temp = self.read_sensors()
            j = json.dumps(temp)
            try:
                self.client_send(j)
                time.sleep(3)
            except Exception as e:
                pass

    @staticmethod
    def start_client():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('localhost', 50000))
                return s
            except Exception as e:
                pass

    def client_send(self, message):
        t1 = Thread(target=self.sock.sendall, args=(message,))
        t1.start()

    def client_listen(self):
        while True:
            data = self.sock.recv(1024)
            print(data)

    def read_sensors(self):
        self.frame += 1
        return {'data': {'depth': pnoise1(self.frame * .0013), 'IMUx': pnoise1(self.frame * -.0023),
                         'IMUy': pnoise1(self.frame * .0073),
                         'IMUz': pnoise1(self.frame * -.0003)}}


if __name__ == '__main__':
    Client()
