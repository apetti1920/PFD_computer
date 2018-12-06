import socket
from threading import Thread
import json
import time

from noise import pnoise1


class Client:
    def __init__(self):
        self.sock = socket.socket()
        self.frame = 0
        self.collect_data = False
        self.connected = False
        self.start_client()

    def start_client(self):
        while not self.connected:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('', 50000))
                self.sock = s
                self.connected = True
                break
            except socket.error:
                self.connected = False
                print('No Connection')
                time.sleep(2)

        listen_thread = Thread(target=self.client_listen, name="Listen Thread")
        listen_thread.start()

        data_thread = Thread(target=self.handle_data, name='Data Thread')
        data_thread.start()

    def handle_data(self):
        while True:
            if self.collect_data:
                j = self.read_sensors()
                self.client_send(j)
                time.sleep(.05)

    def client_send(self, message):
        try:
            self.sock.sendall(message, )
        except socket.error:
            self.connected = False

    def client_listen(self):
        while True:
            data = self.sock.recv(1024)
            if data.decode("utf-8") == 'Arm':
                print('Armmed')
                self.collect_data = True
            elif data.decode("utf-8") == 'Disarm':
                print('Disarmed')
                self.collect_data = False
            elif not data:
                print('not data')
                self.sock.close()
                self.connected = False
                break

    def read_sensors(self):
        data = {'data': {'depth': pnoise1(self.frame * .0023) * 150, 'IMUx': pnoise1(self.frame * -.0013),
                         'IMUy': pnoise1(self.frame * -.0073),
                         'IMUz': pnoise1(self.frame * -.0003)}}

        self.frame += 1

        j = json.dumps(data)
        j = j.encode('utf8')
        return j


if __name__ == '__main__':
    Client()
