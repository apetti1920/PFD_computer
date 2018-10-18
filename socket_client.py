import socket
from threading import Thread
import json
import time

from noise import pnoise1


class Client():
    def __init__(self):
        self.sock = self.start_client()
        self.frame = 0

        t2 = Thread(target=self.client_listen)
        t2.start()

        while True:
            temp = self.read_sensors()
            j = json.dumps(temp)
            j = j.encode('utf8')
            try:
                print(j)
                self.client_send(j)
                time.sleep(.05)
            except Exception as e:
                pass

    @staticmethod
    def start_client():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 50000))
        print('connected')
        return s

    def client_send(self, message):
        t1 = Thread(target=self.sock.sendall, args=(message,))
        t1.start()

    def client_listen(self):
        while True:
            data = self.sock.recv(1024)
            print(data)

    def read_sensors(self):
        data = {'data': {'depth': pnoise1(self.frame*.0023)*150, 'IMUx': pnoise1(self.frame*-.0013),
                         'IMUy': pnoise1(self.frame*-.0073),
                         'IMUz': pnoise1(self.frame*-.0003)}}


        self.frame += 1
        return data


if __name__ == '__main__':
    Client()