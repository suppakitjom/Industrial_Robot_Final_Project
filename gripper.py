import socket
import time
from colored_printed import print_colored

class Gripper:
    _ip: str = '10.10.0.14'
    _port: int = 63352
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print_colored(f'Connecting to gripper at {self._ip}:{self._port}...','yellow')
        self.__connect()

    def __connect(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print_colored('Connected to gripper. Getting ACT','yellow')
        self._client.send(b'SET ACT 1\n')
        self._client.send(b'GET ACT\n')
        if '1' in str(self._client.recv(10), 'UTF-8'):
            print_colored('ACT Received. Activating gripper','yellow')
        # self._client.send(b'SET GTO 1\n')

    def open(self):
        self._client.send(b'SET FOR 214\n')
        self._client.send(b'SET SPE 255\n')
        self._client.send(b'SET POS 0\n')
        print_colored(str(self._client.recv(255), 'UTF-8'),'yellow')

    def close(self):
        self._client.send(b'SET FOR 214\n')
        self._client.send(b'SET SPE 255\n')
        self._client.send(b'SET POS 255\n')
        print_colored(str(self._client.recv(255), 'UTF-8'),'yellow')

if __name__ == '__main__':
    gripper = Gripper()
    gripper.open()