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

def gripper_open(s):
    s.send(b'SET SPE 173\n')
    s.send(b'SET FOR 214\n')
    s.send(b'SET POS 0\n')
    time.sleep(2)


def gripper_close(s):
    s.send(b'SET SPE 173\n')
    s.send(b'SET FOR 214\n')
    s.send(b'SET POS 255\n')
    time.sleep(2)


HOST = '10.10.0.14'
PORT = 30003
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))

GRIPPER_PORT = 63352
s_g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_g.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_g.connect((HOST, GRIPPER_PORT))
s_g.send(b'SET ACT 1\n')
s_g.send(b'SET GTO 1\n')

VISION_HOST = '10.10.1.10'
PORT = 2024

s_v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_v.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_v.connect((VISION_HOST, PORT))


time.sleep(3)
default_pos(s)
time.sleep(2)
operation_pos(s)

time.sleep(2)
obj_pos = s_v.recv(255)
# turn MSG into list
dx,dy,dradian = 0,0,0
while dx and dy and dradian:
    obj_pos = s_v.recv(255).decode('utf-8')
    poslist = [x for x in obj_pos.strip()[1:-1].split(',')]
    # turn MSG into list
    if poslist[0] == 'TRUE':
        dx,dy,dtheta = [float(x) for x in poslist[1:]] # mm
        # convert to meters
        dx = dx/1000
        dy = dy/1000
        # convert to radian
        dradian = dtheta%180*math.pi/180
        print(dx,dy,dradian)

gripper_open(s_g)
s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0.18,0,-0.1,0,0,0]),1,0.25,2,0)\n')
time.sleep(2)
command = f'movel(pose_add(get_actual_tcp_pose(),p[{dx},{dy},0,0,0,{dradian}]),1,0.25,2,0)\n'
s.send(command.encode('utf-8'))
time.sleep(2)
s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0,0,-.2,0,0,0]),1,0.25,2,0)\n')
time.sleep(2)
gripper_close(s_g)
s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0,0,.2,0,0,0]),1,0.25,2,0)\n')
time.sleep(2)
s.send(b'movel(pose_add(get_actual_tcp_pose(),p[-0.18,0,0.1,0,0,0]),1,0.25,2,0)\n')
time.sleep(2)
s.send(b'movel(p[.046,-.32,-.1,2.2,2.239,0],0.1,0.1,2,0)\n')
time.sleep(2)
gripper_open(s_g)
time.sleep(.5)
operation_pos(s)
time.sleep(2)
default_pos(s)
# # move 10 cm to the left
# s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0,0,.1,0,0,0]),1,0.25,0,0)\n')
# time.sleep(2)
# s.send(b'movel(pose_add(get_actual_tcp_pose(),p[-.05,0,0,0,0,0]),1,0.25,0,0)\n')
# time.sleep(2)
# s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0,0,-.1,0,0,0]),1,0.25,0,0)\n')
# time.sleep(2)
# gripper_open(s_g)
# default_pos(s)


# s.send(b'movel(pose_add(get_actual_tcp_pose(),p[0,0,-.3,0,0,0]),1,0.25,0,0)\n')