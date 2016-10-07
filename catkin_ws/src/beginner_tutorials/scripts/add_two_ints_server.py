#!/usr/bin/env python
""" Service node
2016.10.05 LncMug
"""

from beginner_tutorials.srv import *
import rospy


def handle_add_two_ints(req):
    """ Add two ints
    return that's result
    """

    print "Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)


def add_two_ints_server():
    """ Server for add two ints
    recieve two ints from client and throw thats sum
    """
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add ints."
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()
