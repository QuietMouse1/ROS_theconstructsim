#! /usr/bin/env python

import rospy
from path_exam.srv import Motion_Service, Motion_ServiceResponse, Motion_ServiceRequest # you import the service message python classes generated from Empty.srv.
from path_exam.msg import RecordOdomFeedback, RecordOdomAction, RecordOdomResult, RecordOdomGoal
from nav_msgs.msg import Odometry
import actionlib
from geometry_msgs.msg import Twist
import sys


# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/my_service')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/my_service', Motion_Service)
# Create an object of type TrajByNameRequest
print("sending")
traj_by_name_object = Motion_ServiceRequest()
print ("sent?")
# Send through the connection the name of the trajectory to be executed by the robot
result = traj_by_name_service(traj_by_name_object)
# Print the result given by the service called
print result