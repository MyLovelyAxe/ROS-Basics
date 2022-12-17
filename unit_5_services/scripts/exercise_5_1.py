#! /usr/bin/env python

import rospkg
import rospy
# Import the service message used by the service /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_E51_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
ExecTraj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type ExecTrajRequest
ExecTraj_object = ExecTrajRequest()
# Create an instance of type RosPack
rospack = rospkg.RosPack()
# Find a file path for trajectory
ExecTraj_file_path = rospack.get_path(
    'iri_wam_reproduce_trajectory') + "/config/get_food.txt"
# Fill the variable file of this object with the desired value
ExecTraj_object.file = ExecTraj_file_path
# Send through the connection the name of the trajectory to be executed by the robot
result = ExecTraj_service(ExecTraj_object)
# Print the result given by the service called
print(result)
