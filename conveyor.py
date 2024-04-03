import socket
import time
from colored_printed import print_colored

class Conveyor:
    _ip: str = "10.10.0.98"
    _port: int = 2002
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print_colored(f"Connecting to conveyor at {self._ip}:{self._port}...",'green')
        self.__connect()

    def __connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self._ip, self._port))
        s.listen()
        print_colored(f"Server listening at {self._ip}:{self._port}",'green')
        c, addr = s.accept()
        print_colored(f"Connected by {addr}",'green')
        c.sendall(b"activate,tcp,0.0\n")
        c.sendall(b"pwr_on,conv,0\n")
        self._client = c

    def run_conveyor(self):
        time.sleep(1)
        self._client.sendall(b"set_vel,conv,10\n")
        self._client.sendall(b"jog_fwd,conv,0\n")
        print_colored(self._client.recv(20),'green')

    def stop_conveyor(self):
        print_colored("Stopping conveyor",'green')
        time.sleep(1)
        self._client.sendall(b"jog_stop,conv,0\n")
        print_colored(self._client.recv(20),'green')

    def set_speed(self, speed: float):
        time.sleep(1)
        command = f"set_vel,conv,{speed}\n".encode()
        self._client.sendall(command)
        print(command)
        print_colored(self._client.recv(20),'green')
        

if __name__ == "__main__":
    conveyor = Conveyor()
    # conveyor.set_speed(200)
    conveyor.run_conveyor()
    input()
    conveyor.stop_conveyor()