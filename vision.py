import socket
import math
from colored_printed import print_colored
import time

class Vision:
    _ip: str = '10.10.1.10'
    _port: int = 2024
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print_colored(f'Connecting to vision at {self._ip}:{self._port}...','magenta')
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print_colored('Connected to vision.','magenta')

    def get_obj_pos(self) -> list:
        dx,dy,dradian = 0,0,0
        while True:
            obj_pos = self._client.recv(255).decode('utf-8').split()[0]
            print(obj_pos)
            poslist = [x for x in obj_pos.strip()[1:-1].split(',')]
            if poslist[0] == 'TRUE':
                dx,dy,dtheta = [float(x) for x in poslist[1:]] # mm
                # convert to meters
                dx = dx/1000
                dy = dy/1000
                # convert to radian
                dradian = dtheta%180*math.pi/180
                print_colored(f'Object position: {dx,dy,dradian}','magenta')
                break
            time.sleep(1)
        return [dx,dy,dradian]
    
# if __name__ == '__main__':
#     v = Vision()
#     print(v.get_obj_pos())