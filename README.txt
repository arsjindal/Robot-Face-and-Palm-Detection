#######Human Face Detection:
Navigate to folder- “Face _ Eye Detection with EdgeTpu”
Run python script- "face_detection_1.py" in your python environment via following commands:
* python3 face_detection_1.py
This code will use your webcam or camera connected to your linux operating system and start detecting Faces and Eyes of users in front of Quori.
Currently this code is using webcam of computer, to change the input of camera. Change value of VideoCapture() function. 
The code is designed to detect three triggers:
* Sleep: In this code we are recognizing faces of person with the help of pre-Trained Mobilenet network suitable for facial recognition with help of Google CORAL. We track time intervals for which faces are recognized in code. If faces are not recognized for a long time, that implies that no one is near Quori to interact with. If the time for object not recognized is greater than 20 seconds, this code sends message to ROS node to go to sleep. Currently this time is set as 20 seconds in the code. This can be varied by modifying “time_2_sleep” function.
* Face Tilt:- It recognizes the face tilt and direction of tilt for the person standing nearest to Robot. Eyes of nearest person is detected in the algorithm using Human Eye detection Haar Cascade- “haarcascade_eye.xml” from OpenCV. We are tracking the horizontal alignment of a person. If both eyes are in same level, the face is not tilted and in other case scenarios, we can also find the direction of tilt. As, face tilt is detected, this code sends message to Ros node for communication b/w robots.
* Surprise: This is made to detect if a person is approaching Quori really fast. This will send trigger to quori for acting surprised. We are tracking the y pixel value of nearest person standing and processing it for every 4 frames. If person approaches near quori, his y value would reduce. So, by processing it every 4 second we are able to determine its speed in pixels/second. If speed of person reaches more that 20 pixels per second in y direction upwards, it will send trigger to Quori. We can change the speed value by modifying variable “max_speed”.

message array: The final output file in the code is an 3X1 array with integer entries. Each element represent certain trigger.
first element: represents Sleep(0) or not (1)
second element: represent no face tilt (0) or face tilt left (1) or face tilt right (2)
third element: represents no surprise (0) or suprise(1)

Example: If the robot detects a person who advances towards the it at a rapid pace with his/her face tilted right (from quori's perspective), quori would not be in the sleep mode(1) and be surprised (1) and detect a right face tilt (2). So the final message file would be:
[1
2
1]

####### Node Info:
Node name: ros_node_face.py*
The note imports the final "message" file and publishes the array as a Vector3 msg file on the topic Topic1* with a 10Hz* rate.

Please edit names of files which are marked * to integrate into the structure.

#######################################################################################################
THIS IS A TRIAL MESSAGE TO CHECK GIT COMMIT IN NEW BRANCH
#######################################################################################################