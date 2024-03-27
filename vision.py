import socket
import math

class Vision:
    _ip: str = '10.10.1.10'
    _port: int = 2024
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f'Connecting to vision at {self._ip}:{self._port}...')
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print('Connected to vision.')

    def get_obj_pos(self) -> list:
        dx,dy,dradian = 0,0,0
        while dx and dy and dradian:
            obj_pos = self._client.recv(255).decode('utf-8')
            poslist = [x for x in obj_pos.strip()[1:-1].split(',')]
            if poslist[0] == 'TRUE':
                dx,dy,dtheta = [float(x) for x in poslist[1:]] # mm
                # convert to meters
                dx = dx/1000
                dy = dy/1000
                # convert to radian
                dradian = dtheta%180*math.pi/180
                print(f'Object position: {dx,dy,dradian}')
        return [dx,dy,dradian]