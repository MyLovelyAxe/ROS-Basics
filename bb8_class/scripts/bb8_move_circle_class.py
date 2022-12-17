#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


class MoveBB8():

    def __init__(self, duration):
        self.bb8_vel_publisher = rospy.Publisher(
            '/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)  # 10hz
        self.duration = duration
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True

    def move_bb8(self, linear_speed=0.2, angular_speed=0.2):

        i = 0
        while i < self.duration:

            self.cmd.linear.x = linear_speed
            self.cmd.angular.z = angular_speed

            rospy.loginfo("Moving BB8 in %dth second!", i+1)
            print("try %d", i+1)
            self.bb8_vel_publisher.publish(self.cmd)
            self.rate.sleep()

            i += 1

        self.cmd.linear.x = 0
        self.cmd.angular.z = 0
        self.bb8_vel_publisher.publish(self.cmd)


if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.move_bb8()
    except rospy.ROSInterruptException:
        pass
