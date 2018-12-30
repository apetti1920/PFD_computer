from noise import pnoise1

from PFDSocket import PFDSocket

sock = PFDSocket()

def on_data(data):
    print(data)

sock.on('data', on_data)
sock.server()
