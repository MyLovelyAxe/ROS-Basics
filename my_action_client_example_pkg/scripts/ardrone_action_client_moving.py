#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received


def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received' % nImage)
    nImage += 1


# initializes the action client node
rospy.init_node('drone_action_client_moving')

# create the connection to the action server
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction)
# waits until the action server is up and running
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name)

# publisher of movement, taking off and landing
movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
takeoff = Empty()
land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)
land = Empty()
rate = rospy.Rate(1)

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10  # indicates, take pictures along 10 seconds
# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time
state_result = client.get_state()

# take off in 3 seconds
for i in range(3):

    rospy.loginfo('taking off...')
    takeoff_pub.publish(takeoff)
    rate.sleep()

while state_result < DONE:

    vel.linear.x = 0.5
    vel.angular.z = 0.5
    movement_pub.publish(vel)
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo('current state is: ' + str(state_result))

vel.linear.x = 0
vel.angular.z = 0
movement_pub.publish(vel)


for i in range(3):

    rospy.loginfo('landing...')
    land_pub.publish(land)
    rate.sleep()


print('[Result] State: %d' % (client.get_state()))
