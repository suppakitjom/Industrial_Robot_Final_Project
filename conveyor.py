import socket
import time

class Conveyor:
    _ip: str = "10.10.0.98"
    _port: int = 2002
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f"Connecting to conveyor at {self._ip}:{self._port}...")
        self.__connect()

    def __connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self._ip, self._port))
        s.listen()
        print(f"Server listening at {self._ip}:{self._port}")
        c, addr = s.accept()
        print(f"Connected by {addr}")
        c.sendall(b"activate,tcp,0.0\n")
        c.sendall(b"pwr_on,conv,0\n")
        self._client = c

    def run_conveyor(self):
        time.sleep(1)
        self._client.sendall(b"jog_fwd,conv,0\n")
        print(self._client.recv(20))

    def stop_conveyor(self):
        print("Stopping conveyor")
        time.sleep(1)
        self._client.sendall(b"jog_stop,conv,0\n")

    def set_speed(self, speed: int):
        time.sleep(1)
        self._client.sendall(f"set_vel,conv,{speed}\n".encode())

# if __name__ == "__main__":
#     conveyor = Conveyor()
#     conveyor.stop_conveyor()