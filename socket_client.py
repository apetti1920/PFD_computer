import socket
from threading import Thread


class Client():
    def __init__(self):
        self.start_client()


    def start_client(self):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 50000))
        t1 = Thread(target=self.client_listen, args=(s,))
        t1.start()

        while True:
            s.sendall('hi')

    def client_listen(self, sock):
        while True:
            data = sock.recv(1024)
            print(data)


if __name__ == '__main__':
    Client()
