#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_move_client_node')
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
bb8_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
# Create an object of type EmptyResponse
bb8_object = EmptyRequest()

result = bb8_service(bb8_object)
# Print the result given by the service called
print(result)
