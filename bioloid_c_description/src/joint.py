#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    servo_states = JointState()
    servo_states.header = Header()
    servo_states.header.stamp = rospy.Time.now()
    servo_states.name = [
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
    servo_states.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    servo_states.velocity = []
    servo_states.effort = []
    rate.sleep()

    while not rospy.is_shutdown():
      for i in range(len(servo_states.name)):
        #   print(i)
          servo_states.position[i] = 0.0
      servo_states.header.stamp = rospy.Time.now() #always set the header stamp before updating the joints
      pub.publish(servo_states)
      rate.sleep()

      #test move   
      for i in range(len(servo_states.name)):
        #   print(i)
          servo_states.position[i] = 0.628
      servo_states.header.stamp = rospy.Time.now() #always set the header stamp before updating the joints

      pub.publish(servo_states)
      rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass