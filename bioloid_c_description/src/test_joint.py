#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = [
                    'left_shoulder_joint',
                    'right_shoulder_joint',
                    'left_hip_joint',
                    'left_thigh_joint',
                    'left_knee_joint',
                    'left_ankle_joint',
                    'left_foot_joint',
                    'right_hip_joint',
                    'right_thigh_joint',
                    'right_knee_joint',
                    'right_ankle_joint',
                    'right_foot_joint',
                    ]
    hello_str.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    hello_str.velocity = []
    hello_str.effort = []
    pub.publish(hello_str)
    rate.sleep()


    while not rospy.is_shutdown():
      hello_str.header.stamp = rospy.Time.now()
      pub.publish(hello_str)
      rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass