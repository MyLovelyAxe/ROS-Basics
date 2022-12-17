#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist


def my_callback(request):
    rospy.loginfo("bb8 is moving!!!")
    vel.linear.x = 0.5
    vel.angular.z = 0.5
    pub.publish(vel)
    rospy.loginfo("bb8 is done moving!!!")
    return EmptyResponse()  # the service Response class, in this case EmptyResponse
    # return MyServiceResponse(len(request.words.split()))


rospy.init_node('bb8_move_server_node')
# create the Service called my_service with the defined callback
my_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rospy.loginfo('Service /move_bb8_in_circle is ready')
rospy.spin()  # maintain the service open.
