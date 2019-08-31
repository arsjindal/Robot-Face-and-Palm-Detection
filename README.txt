Human Face Detection:
Navigate to folder- “Face _ Eye Detection with EdgeTpu”
Run python script- "face_detection_1.py" in your python environment via following commands:
* python3 face_detection_1.py
This code will use your webcam or camera connected to your linux operating system and start detecting Faces and Eyes of users in front of Quori.
Currently this code is using webcam of computer, to change the input of camera. Change value of VideoCapture() function. 
The code is designed to detect three triggers:
* Sleep: In this code we are recognizing faces of person with the help of pre-Trained Mobilenet network suitable for facial recognition with help of Google CORAL. We track time intervals for which faces are recognized in code. If faces are not recognized for a long time, that implies that no one is near Quori to interact with. If the time for object not recognized is greater than 20 seconds, this code sends message to ROS node to go to sleep. Currently this time is set as 20 seconds in the code. This can be varied by modifying “time_2_sleep” function.
* Face Tilt:- It recognizes the face tilt and direction of tilt for the person standing nearest to Robot. Eyes of nearest person is detected in the algorithm using Human Eye detection Haar Cascade- “haarcascade_eye.xml” from OpenCV. We are tracking the horizontal alignment of a person. If both eyes are in same level, the face is not tilted and in other case scenarios, we can also find the direction of tilt. As, face tilt is detected, this code sends message to Ros node for communication b/w robots.
* Surprise: This is made to detect if a person is approaching Quori really fast. This will send trigger to quori for acting surprised. We are tracking the y pixel value of nearest person standing and processing it for every 4 frames. If person approaches near quori, his y value would reduce. So, by processing it every 4 second we are able to determine its speed in pixels/second. If speed of person reaches more that 20 pixels per second in y direction upwards, it will send trigger to Quori. We can change the speed value by modifying variable “max_speed”.

