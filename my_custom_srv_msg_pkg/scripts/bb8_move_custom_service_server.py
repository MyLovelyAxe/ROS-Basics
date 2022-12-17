#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse


def my_callback(request):

    my_response = MyCustomServiceMessageResponse()
    t = 0
    rospy.loginfo('bb8 is going to move for %d seconds!!!', request.duration)
    vel.linear.x = 0.5
    vel.angular.z = 0.5

    while t < request.duration:

        pub.publish(vel)
        rate.sleep()
        my_response.success = False
        t += 1
        rospy.loginfo('bb8 has already moved for %d seconds!!!', t)

    vel.linear.x = 0
    vel.angular.z = 0
    pub.publish(vel)
    my_response.success = True
    rospy.loginfo('bb8 stops!!!')

    # the service Response class, in this case EmptyResponse
    return my_response
    # return MyServiceResponse(len(request.words.split()))


rospy.init_node('bb8_move_custom_server_node')
# create the Service called my_service with the defined callback
my_service = rospy.Service(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rate = rospy.Rate(1)
rospy.loginfo('Service /move_bb8_in_circle_custom is ready')
rospy.spin()  # maintain the service open.
