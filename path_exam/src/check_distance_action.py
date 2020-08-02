#! /usr/bin/env python
import rospy
import time
import actionlib
from OdomTopicSubsciber import OdomTopicReader 
from path_exam.msg import RecordOdomFeedback, RecordOdomAction, RecordOdomResult
from nav_msgs.msg import Odometry


def goal_callback(goal):
    rate = rospy.Rate(1)
    result = RecordOdomResult()
    sucess = True
    recording_time = 20 # recording time

    # record pos 20 times
    for i in range (20):
        rospy.loginfo("Recording odom index " + str(i))
        if record_odom_action_server.is_preempt_requested():
            sucess = False
            record_odom_action_server.set_preempted()
        else:
            odom_reader_object = OdomTopicReader()
            result.result_odom_array.append(odom_reader_object.get_odomdata())
            #print(odom_reader_object.get_odomdata())
        rate.sleep()
    rospy.loginfo("finished recording 20 data sets")
    if sucess:
        record_odom_action_server.set_succeeded(result)
        rospy.loginfo("result data is sent")
    
    

rospy.init_node("check_distance_node")
record_odom_action_server = actionlib.SimpleActionServer('/rec_pose_as',RecordOdomAction,goal_callback,False)
record_odom_action_server.start()
rospy.loginfo("Action server started")

