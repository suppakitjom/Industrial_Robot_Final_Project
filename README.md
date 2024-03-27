# Catch-A-Box: UR3 Robot Control System

## Project Overview
The Catch-A-Box project involves the development of an automated control system for a UR3 robotic arm to identify, track, and grasp moving boxes on a conveyor belt. The system utilizes real-time visual processing and dynamic motion planning to achieve precise, timely, and efficient object manipulation.

### System Architecture
- **Vision System:** Utilizes a camera mounted to the end-effector of the UR3 robot to continuously monitor the conveyor belt, identify boxes, and calculate their relative positions and orientations in real-time using NI Vision Builder.
- **Control Algorithm:** Employs a program that integrates vision system data to dynamically control the robot's arm and gripper.
