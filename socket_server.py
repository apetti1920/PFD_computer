import socket
from threading import Thread
import time


class Server():
    def __init__(self):
        self.start_server()

    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 50000))
        s.listen(1)
        conn, addr = s.accept()
        t1 = Thread(target=self.server_send, args=(conn,), daemon=True)
        t1.start()

        while 1:
            data = conn.recv(1024)
            if not data:
                break

            print(data)

        conn.close()

    def server_send(self, conn):
        time.sleep(5)
        conn.sendall('stop')


if __name__ == '__main__':
    Server()
