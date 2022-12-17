#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse


def my_callback(request):

    side_len = request.side
    circle_num = request.repetitions
    # the default speed of BB8 is 0.5 (m/s)
    speed = 0.5
    # we get requested distance from "request.side", a.k.a side_len
    # so BB8 should only go time_limit (s) as below
    time_limit = int(side_len / speed)

    # BB8 should repeate circle_num rounds
    for i in range(circle_num):
        # each round for a square has 4 side
        for j in range(4):

            time = 0
            rospy.loginfo('BB8 begins %dth round %dth side', i+1, j+1)
            while time <= time_limit:
                vel.linear.x = speed
                pub.publish(vel)
                time += 1
                rate.sleep()
            vel.linear.x = 0

            # when one side of a square is finished
            # rotate anticlockwisely about 90 degree
            # in rotating speed of 0.1 (m/s), rotate 3 (s)
            vel.angular.z = 0.6
            rotate_time = 0
            while rotate_time <= 2:
                pub.publish(vel)
                rotate_time += 1
                rate.sleep()
            vel.angular.z = 0

    my_response = BB8CustomServiceMessageResponse()
    my_response.success = True
    rospy.loginfo('BB8 finish all rounds')

    return my_response


rospy.init_node("services_quiz_custom_server_node")
my_service = rospy.Service(
    "/move_bb8_in_square_custom", BB8CustomServiceMessage, my_callback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
vel = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_square_custom is ready")
rospy.spin()
