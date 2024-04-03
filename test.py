import socket,time
from socket import *


host    = '10.10.0.98'
port_conv = 2002

c = socket(AF_INET, SOCK_STREAM)
#c.bind(('10.10.0.98', 2002))



#c = socket.socket()

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
c.bind((host , port_conv))
print ("socket binded to %s" %(port_conv)) 

c.listen(1)
print ("socket is listening") 
conv, addr = c.accept()
with conv:
    print(f"Connected by {addr}")
    conv.sendall(b'activate,tcp,0.0\n')
    time.sleep(1)

    conv.sendall(b'pwr_on,conv,0\n')
    time.sleep(1)

    conv.sendall(b'set_vel,conv,20\n')
    time.sleep(1)

    conv.sendall(b'jog_stop,conv,0\n')
    time.sleep(1)

    conv_recv = conv.recv(100)
    print(conv_recv)