#! /usr/bin/env python

import rospy                               
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

ctrl_c = False
rospy.init_node('drone_forward')
rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
empty = Empty()
pub = rospy.Publisher('drone/takeoff',Empty,queue_size=1)
forward = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
land = rospy.Publisher('drone/land',Empty,queue_size=1)
move_front = Twist()
move_front.linear.x = 1
stop = Twist()

while not ctrl_c:
    connections = pub.get_num_connections()
    if connections > 0:
        pub.publish(empty)
        rospy.loginfo("takeoff Published")
        break
    else:
        rate.sleep()

rospy.sleep(1)
forward.publish(move_front)
rospy.sleep(5)
forward.publish(stop)
rospy.sleep(2)
land.publish(empty)
rospy.sleep(0.1)
rospy.loginfo("land Published")



print("yo")
