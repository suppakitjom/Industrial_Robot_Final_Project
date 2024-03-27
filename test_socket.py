import socket
import sys
import time
import math

def default_pos(s):
    s.send(b'movel(p[.116,-.3,.2,0,-3.143,0],0.2,0.2,2,0)\n')
    time.sleep(1)

def operation_pos(s):
    # s.send(b'movel(p[.116,-.32,.2,2.2,2.239,0],0.2,0.2,2,0)\n')
    s.send(b'movel(p[.046,-.32,.2,2.2,2.239,0],0.2,0.2,2,0)\n')
    time.sleep(1)


HOST = '10.10.0.14'
PORT = 30003
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))

# default_pos(s)
operation_pos(s)
# s.send(b'movel(p[.046,-.32,-.1,2.2,2.239,0],0.1,0.1,2,0)\n')