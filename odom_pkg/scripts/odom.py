#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry


def callback(msg):
    print(msg.header)


rospy.init_node('odom_sub')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
