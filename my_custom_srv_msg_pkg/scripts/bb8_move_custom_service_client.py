#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest
import sys

# Initialise a ROS node with the name bb8_move_custom_client_node
rospy.init_node('bb8_move_custom_client_node')
# Wait for the service client /move_bb8_in_circle_custom to be running
rospy.wait_for_service('/move_bb8_in_circle_custom')
# Create the connection to the service
bb8_service_custom_client = rospy.ServiceProxy(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage)
# Create an object of type MyCustomServiceMessageRequest
bb8_object_client = MyCustomServiceMessageRequest()
# set value of "duration": let bb8 move 5 seconds
bb8_object_client.duration = 15

result = bb8_service_custom_client(bb8_object_client)
# Print the result given by the service called
print(result)
