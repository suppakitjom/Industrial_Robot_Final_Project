import socket
import time
import numpy as np
from colored_printed import print_colored

class Arm:
    _ip: str = '10.10.0.14'
    _port: int = 30003
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print_colored(f'Connecting to arm at {self._ip}:{self._port}...','cyan')
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print_colored('Connected to arm.','cyan')

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
            move_cmd = f'movej(pose_add(get_actual_tcp_pose(),p[{x},{y},{z},{rx},{ry},{rz}]),{acceleration},{velocity},{task_time},{blend_radius})'
        else:
            move_cmd = f'movej(p[{x},{y},{z},{rx},{ry},{rz}],{acceleration},{velocity},{task_time},{blend_radius})'
        print_colored(f'Sending move command: {move_cmd}','cyan')
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
            move_cmd = f'movel(pose_add(get_actual_tcp_pose(),p[{x},{y},{z},{rx},{ry},{rz}]),{acceleration},{velocity},{task_time},{blend_radius})'
        else:
            move_cmd = f'movel(p[{x},{y},{z},{rx},{ry},{rz}],{acceleration},{velocity},{task_time},{blend_radius})'
        print_colored(f'Sending move command: {move_cmd}','cyan')
        self.__send(move_cmd)
        time.sleep(task_time or 1)

    def standby_pos(self):
        self.movej(x=.046, y=-.32, z=.065, rx=2.2, ry=2.24, rz=0, task_time=2, relative=False)
        print_colored('Arm moving to standby position...','cyan')

    def home_pos(self):
        # self._client.send(b'movel(p[.116,-.3,.2,0,-3.143,0],0.2,0.2,2,0)\n')
        # self.movej(x=.116, y=-.3, z=.2, rx=0, ry=-3.143, rz=0, task_time=1, relative=False)
        angles = (np.array([-48.48, -101.48, -40.23, -128.24, 90.05, 41.52])*np.pi/180).astype(str)
        move_cmd = f'movej([{",".join(angles)}],1,1,2,0)'
        self.__send(move_cmd)
        print_colored('Arm moving to home position...','cyan')



if __name__ == '__main__':
    arm = Arm()
    # arm.home_pos()
    arm.standby_pos()