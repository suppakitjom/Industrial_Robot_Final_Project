from arm import Arm
from conveyor import Conveyor
from gripper import Gripper
from vision import Vision
import time
import math

ur_arm = Arm()
conveyor = Conveyor() # not needed in the real demo
gripper = Gripper()
vision = Vision()

ur_arm.home_pos()
ur_arm.standby_pos()
gripper.open()

dx,dy,dradian = vision.get_obj_pos()
# once item is detected by the camera, there is ~2 seconds window for the arm to move before item passes gripper
if dx and dy and dradian:
    ur_arm.movej(x=dx, y=dy, rz=dradian, task_time=1, relative=True)
    ur_arm.movel(z=-0.32, task_time=1, relative=True)
    gripper.close()