#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry
from exer43.msg import Age

rospy.init_node('how_old_are_you')
pub = rospy.Publisher('/robot_age', Age, queue_size=1)
rate = rospy.Rate(1)
age = Age()
age.years = 24
age.months = 7
age.days = 24

while not rospy.is_shutdown():
    pub.publish(age)
    age.days += 1
    rate.sleep()
