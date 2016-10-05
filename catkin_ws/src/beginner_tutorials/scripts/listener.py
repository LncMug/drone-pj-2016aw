#!/usr/bin/env python
# 2016.10.05 ros subcribe msg LncMug

import rospy
from std_msgs.msg import String


# callback for subcriber
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


# subcribe msgs from ros master
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
