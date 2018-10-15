import socket
from threading import Thread


class Client():
    def __init__(self):
        self.start_client()

    def start_client(self):
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server

        print('Connected to', client_socket.getsockname())

        message = input(" -> ")  # take input

        while message.lower().strip() != 'bye':
            client_socket.send(str(message))  # send message
            data = client_socket.recv(1024)  # receive response

            print('Received from server: ' + data)  # show in terminal

            message = input(" -> ")  # again take input

        client_socket.close()  # close the connection


if __name__ == '__main__':
    Client()
