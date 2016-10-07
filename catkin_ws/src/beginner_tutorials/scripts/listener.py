#!/usr/bin/env python
""" ros subcribe msg
2016.10.05 LncMug
"""

import rospy
from std_msgs.msg import String


def callback(data):
    """ Callback function
    print msg recieve from talker
    """
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


# subcribe msgs from ros master
def listener():
    """ Subscriber
    Subscribe msgs from master that published by talker
    """

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
