#! /usr/bin/env python

import rospy
from bb8_move_circle_class import MoveBB8
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse


def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    time = request.duration
    rospy.loginfo("bb8 needs to move for %d seconds", time)
    movebb8_object = MoveBB8(time)
    movebb8_object.move_bb8()
    my_response = MyCustomServiceMessageResponse()
    my_response.success = True
    rospy.loginfo("Finished service move_bb8_in_circle")
    return my_response


rospy.init_node('service_move_bb8_in_circle_server')
my_service = rospy.Service('/move_bb8_in_circle',
                           MyCustomServiceMessage, my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()  # keep the service open.
