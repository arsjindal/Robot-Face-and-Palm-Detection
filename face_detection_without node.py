'''Written by: Aayush Jindal'''
import argparse
import platform
import subprocess
from edgetpu.detection.engine import DetectionEngine
from PIL import Image
from PIL import ImageDraw
import cv2
import numpy as np
import sys
import time



# Function to read labels from text files.
def ReadLabelFile(file_path):
  with open(file_path, 'r', encoding="utf-8") as f:
    lines = f.readlines()
  ret = {}
  for line in lines:
    pair = line.strip().split(maxsplit=1)
    ret[int(pair[0])] = pair[1].strip()
  return ret


if __name__ == '__main__':
	# Selecting model
	engine = DetectionEngine('mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite')
	labels = None
	eye_cascade= cv2.CascadeClassifier('/home/aayushj/Downloads/Eye_cascade/haarcascade_eye.xml')
	# Blob Detector
	detector_params= cv2.SimpleBlobDetector_Params()
	detector_params.filterByArea= True
	detector_params.maxArea = 1500
	detector= cv2.SimpleBlobDetector_create(detector_params)

	# Starting Video Capture
	video_capture= cv2.VideoCapture(0)
	Y=[]
	while True:
		# cap frame by frame
		ret, frame = video_capture.read()
		img = frame
		#to convert it again into image like jpg
		img2= Image.fromarray(img)
		# This calculates the bounding boxes
		ans = engine.DetectWithImage(img2, threshold=0.05, keep_aspect_ratio= True, relative_coord= False, top_k=10)
		current_time= time.time()
		if ans:
			boxes_detected=[]
			areas=[]
			for obj in ans:
				print ('------------------------')
				if labels:
					print(labels[obj.label_id])
				print('score=', obj.score)
				box = obj.bounding_box.flatten().tolist()
				print('box= ', box)
				# boundaries of rectangle
				x= int(box[0])
				y= int(box[1])
				w= int(box[2])
				h= int(box[3])
				area= (w-x)*(h-y)
				#print()
				# Drawing rectangle around faces
				cv2.rectangle(frame, (x,y),(w, h), (0,255,0),2)
				boxes_detected.append(box)
				areas.append(area)
			# helps in detecting time at which code ran
			detection_time= time.time()
			#determining boxes with largest area
			pos= areas.index(max(areas))
			box= boxes_detected[pos]
			x1= int(box[0])
			y1= int(box[1])
			w1= int(box[2])
			h1= int(box[3])
			face= frame[y1:h1, x1:w1]
			Y.append(y1)
			gray_face= cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
			eyes= eye_cascade.detectMultiScale(gray_face, 1.3, 5)
			face_height= np.size(face, 0)
			face_width= np.size(face,1)
			left_eye= None
			right_eye= None
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(face,(ex,ey),(ex+ew, ey+eh), (0,255,255), 2)
				if ey> face_height/2:
					pass
				eye_center= ex+ ew/2
				if eye_center < face_width*0.5:
					left_eye_position= ey + eh/2
				else:
					right_eye_position= ey + eh/2 
				#position.append(int(ey))
			if len(eyes)==2:
				a= left_eye_position
				b= right_eye_position
				if (abs(a-b)<10):
					print("Face is straight")
				elif ((a-b)<-10):
					print("Face is tilted towards left")
				else:
					print("face is tilted towards right")
				
		else:
			print('No object detected')
		# condition for quori to go to sleep
		if ((current_time- detection_time)> 20):
			print('Going to Sleep')
		else:
			print('I am active')
		# condition for finding if somebody is approaching fast enough
		if (len(Y)==4):
			speed= (Y[3]-Y[0])
			print(speed)
			print()
			if (abs(speed)>20):
				print("Object is approaching fast")
			else:
				print("object is slow")
		elif (len(Y)>4):
			Y= []
			Time=[]

		cv2.imshow('Video',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	video_capture.release()
	cv2.destroyAllWindows()
