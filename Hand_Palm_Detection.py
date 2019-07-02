# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:53:19 2019

@author: jinda
"""

import cv2
import numpy as np
import os
import imutils

os.chdir("D:\Sign Language\Opencv-master\haarcascade")
cap = cv2.VideoCapture(0)

hand_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
count = 0

while(True):
    (ret, frame) = cap.read()
    #frame = imutils.resize(frame, width=700)
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    faces= face_cascade.detectMultiScale(gray,1.3,6)
    contour = hands
    contour = np.array(contour)
    
    if len(faces)>0:
        for (a,b,c,d) in faces:
            cv2.rectangle(frame, (a,b), (a+c, b+d), (255,0,0), 2)

    if count==0:

        if len(contour)==2:
            cv2.putText(img=frame, text='Two Palms', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if count>0:

        if len(contour)>=2:
            cv2.putText(img=frame, text='More than 2 palms', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(255, 0, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==1:
            cv2.putText(img=frame, text='Palm detected', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==0:
            cv2.putText(img=frame, text='No Palm detected', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))


    count+=1

    cv2.imshow('Main frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()