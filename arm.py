import socket
import time

class Arm:
    _ip: str = '10.10.0.14'
    _port: int = 30003
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f'Connecting to arm at {self._ip}:{self._port}...')
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print('Connected to arm.')

    def __send(self, cmd: str):
        self._client.send(f'{cmd}\n'.encode(encoding='utf-8', errors='ignore'))

    def movej(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        rx: float = 0,
        ry: float = 0,
        rz: float = 0,
        acceleration: float = 1,
        velocity: float = 0.75,
        task_time: float = 0,
        blend_radius: float = 0,
        relative = True,
    ):
        if relative:
            move_cmd = f'movej(pose_add(get_actual_tcp_pose(),p[{x},{y},{z},{rx},{ry},{rz}]),{acceleration},{velocity},{time},{blend_radius})'
        else:
            move_cmd = f'movej(p[{x},{y},{z},{rx},{ry},{rz}],{acceleration},{velocity},{time},{blend_radius})'
        print(f'Sending move command: {move_cmd}')
        self.__send(move_cmd)
        time.sleep(task_time or 1)

    def movel(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        rx: float = 0,
        ry: float = 0,
        rz: float = 0,
        acceleration: float = 1,
        velocity: float = 0.75,
        task_time: float = 0,
        blend_radius: float = 0,
        relative = True,
    ):
        if relative:
            move_cmd = f'movel(pose_add(get_actual_tcp_pose(),p[{x},{y},{z},{rx},{ry},{rz}]),{acceleration},{velocity},{time},{blend_radius})\n'
        else:
            move_cmd = f'movel(p[{x},{y},{z},{rx},{ry},{rz}],{acceleration},{velocity},{time},{blend_radius})'
        print(f'Sending move command: {move_cmd}')
        self.__send(move_cmd)
        time.sleep(task_time or 1)

    def standby_pos(self):
        self.__send('movej(p[.046,-.32,-.1,2.2,2.239,0],0.2,0.2,2,0)')
        time.sleep(2)

    def home_pos(self):
        self.__send('movej(p[.116,-.3,.2,0,-3.143,0],0.2,0.2,2,0)')
        time.sleep(2)

if __name__ == '__main__':
    arm = Arm()
    arm.home_pos()
    arm.standby_pos()
