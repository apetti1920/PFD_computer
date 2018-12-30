import json
import time
from noise import pnoise1
from PFDSocket import PFDSocket

frame = 0
sock = PFDSocket()
sock.client()
while True:
    data = {'data': {'depth': pnoise1(frame * .0023) * 150,
                     'IMUx': pnoise1(frame * -.0013),
                     'IMUy': pnoise1(frame * -.0073),
                     'IMUz': pnoise1(frame * -.0003)}}

    frame += 1
    j = json.dumps(data)
    sock.sendmsg(j)
    time.sleep(.5)
