#! /usr/bin/env python

import rospy
from path_exam.srv import Motion_Service, Motion_ServiceResponse 
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from std_msgs.msg import Empty as Empty_msg
from geometry_msgs.msg import Twist

rospy.init_node("motion_service")
rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
empty = Empty()
empty_msg = Empty_msg()
emptyResponse = EmptyResponse()
ctrl_c = False

pub = rospy.Publisher('drone/takeoff',Empty_msg,queue_size=1)
forward = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
land = rospy.Publisher('drone/land',Empty_msg,queue_size=1)
move_front = Twist()
move_front.linear.x = 1
stop = Twist()

def move_forward():
    while not ctrl_c:
        connections = pub.get_num_connections()
        if connections > 0:
            pub.publish(empty_msg)
            rospy.loginfo("takeoff Published")
        break
    else:
        rate.sleep()
    
    rospy.sleep(1)
    forward.publish(move_front)
    rospy.sleep(5)
    forward.publish(stop)
    rospy.sleep(2)
    land.publish(empty_msg)
    rospy.sleep(0.1)
    rospy.loginfo("land Published")

def my_callback(request):
    response = Motion_ServiceResponse
    move_forward()
    return emptyResponse

my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.