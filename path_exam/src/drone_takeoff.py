#! /usr/bin/env python

import rospy                               
from std_msgs.msg import Empty

ctrl_c = False
rospy.init_node('drone_takeoff')
rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
empty = Empty()
pub = rospy.Publisher('drone/takeoff',Empty,queue_size=1)

while not ctrl_c:
    connections = pub.get_num_connections()
    if connections > 0:
        pub.publish(empty)
        rospy.loginfo("Cmd Published")
        break
    else:
        rate.sleep()
 
pub.publish(empty)
print("yo")
