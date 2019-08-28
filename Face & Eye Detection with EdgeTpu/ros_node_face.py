#!/usr/bin/env python

from face_detection_1.py import message
import rospy
from geometry_msgs.msg import Vector3

def publ():
	vec3 = Vector3()
	vec3.x = message[0][0]
	vec3.y = message[1][0]
	vec3.z = message[2][0]
	pub = rospy.Publisher('Topic1', Vector3, queue_size=10) # Topic?
	rospy.init_node('ros_node_face', anonymous=True)	# Replace node name
	rate = rospy.Rate(10) # What is the rate
	while not rospy.is_shutdown():
		rospy.loginfo(vec3)
		pub.publish(vec3)
		rate.sleep()



if __name__ == '__main__':
	try:
		publ()
	except rospy.ROSInterruptException:
		pass