from arm import Arm
from gripper import Gripper
from vision import Vision
import time

ur_arm = Arm()
gripper = Gripper()
vision = Vision()

ur_arm.home_pos()
time.sleep(2)

ur_arm.standby_pos()
gripper.open()

print()
while 1:
    dx,dy,dradian = vision.get_obj_pos()
    # once item is detected by the camera, there is ~2 seconds window for the arm to move before item passes gripper
    ur_arm.movej(x=dx+0.07, y=dy, z=-0.1 , rz=dradian, task_time=1, relative=True)
    ur_arm.movej(x=0,z=-0.22, task_time=1, relative=True)
    # time.sleep(1)
    gripper.close()
    time.sleep(.25)
    ur_arm.movel(z = .32, relative=True)
    time.sleep(2)
    gripper.open()
    ur_arm.standby_pos()
