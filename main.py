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

# conveyor.run_conveyor()

# ur_arm.home_pos()

ur_arm.standby_pos()
gripper.open()
time.sleep(1)
print()

dx,dy,dradian = vision.get_obj_pos()
# once item is detected by the camera, there is ~2 seconds window for the arm to move before item passes gripper
ur_arm.movej(x=dx+.18, y=dy, z=-0.1 , rz=dradian, task_time=1, relative=True)
ur_arm.movej(y=0,z=-0.22, task_time=1, relative=True)
time.sleep(1)
gripper.close()
time.sleep(3)
gripper.open()
ur_arm.standby_pos()

# # conveyor.stop_conveyor()