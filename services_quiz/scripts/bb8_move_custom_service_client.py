#! /usr/bin/env python
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node("services_quiz_custom_client_node")
rospy.wait_for_service("/move_bb8_in_square_custom")
bb8_square_client = rospy.ServiceProxy(
    "/move_bb8_in_square_custom", BB8CustomServiceMessage)

# twice for smaller square
my_request_small = BB8CustomServiceMessageRequest()
my_request_small.side = 2
my_request_small.repetitions = 2
# once for bigger square
my_request_big = BB8CustomServiceMessageRequest()
my_request_big.side = 4
my_request_big.repetitions = 1

result_small = bb8_square_client(my_request_small)
print(result_small)

my_request_big = bb8_square_client(my_request_big)
print(my_request_big)
