## 1. Vision Builder for Automated Inspection

<div align="center">

![Flow of the NI Vision Builder](./imgs/flow.png)

_Flow of the inspection_

</div>

Once the video feed is acquired, each frame is then passed to the Vision Assistant for the grayscale plane to be extracted for more efficient image processing.

<div align="center">

![Grayscale plane extraction](./imgs/extract_grayscale_plane.png)

_Grayscale plane extraction_

</div>

The grayscale frame is then passed to the calibration stage where the distance measurements are calibrated and the origin of the image is set to the center of the image.

<div align="center">

![Calibration stage](./imgs/calibration.png)

_Calibration stage_

</div>

After that, the frame in then inspected to see if if finds the object of interest. Here we are using the Match Pattern function to find the object.

<div align="center">

![Match Pattern function](./imgs/match_pattern.png)

_Match Pattern function_

</div>

The function will then return the relative x-y coordinates of the images in the unit of millimeters along with the orientation of the object in the unit of degrees. The coordinates are then broadcasted through TCP/IP.

<div align="center">

![Broadcasting the coordinates](./imgs/send_to_tcp.png)

_Broadcasting the coordinates and orientation_

</div>

In addition, an overlay displaying the real time position and orientation of the object is displayed on the video feed.

<div align="center">

![Overlay](./imgs/real_time_overlay.png)

_Overlay displaying the real time position and orientation of the object_

</div>

## 2. Python Program for controlling UR3 Robot Arm

The Python program is responsible for receiving the coordinates and orientation of the object from the Vision Builder and then sending the coordinates to the UR3 robot arm to pick up the object.

Every communication in the system is done through socket programming. The Python program will establish connections with the Vision Builder Program, the UR3 robot arm and the gripper.

Here we are opting for a class-based approach programming, making the code more modular and easier to maintain.

<div align="center">

![Class-based approach](./imgs/modular_code.png)

_Class-based approach_

</div>
