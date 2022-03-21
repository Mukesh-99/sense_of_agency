import socket
import time
import numpy as np

from socket import (
    socket,
    timeout as sockettimeoutexception,
    AF_INET,
    SOCK_DGRAM,
    SOL_SOCKET,
    SO_RCVBUF,
    SO_REUSEADDR,
)

host = "127.0.0.1"
udpPort = 8667
"""
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind((host, udpPort))
s.listen(1)
conn, addr = s.accept()
success = 0
"""

with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind((host, udpPort))
    while True:
        data = list(s.recv(1024))#.decode()
        print(data)




"""
for i in range(1000):
    packet = [0, 0, 0.01, 0, 0]
    bytes = np.bytes(packet)
    s.connect((host,udpPort))
    s.sendto(bytes, (host,udpPort))
    time.sleep(0.02)

    success += 1

print("success", success)
"""