#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

import numpy as np

"""

                    'left_shoulder_joint',
                    'right_shoulder_joint',

                  6  'left_hip_joint',
                  7  'left_thigh_joint',
                  8  'left_knee_joint',
                  9  'left_ankle_joint',
                  10  'left_foot_joint',

                  1  'right_hip_joint',
                  2  'right_thigh_joint',
                  3  'right_knee_joint',
                  4  'right_ankle_joint',
                  5  'right_foot_joint',

"""
# WITHOUT ARM
TOTAL_JOINTS = 12
robot_joints = np.zeros(TOTAL_JOINTS)

rospy.init_node('joint_state_publisher')
rate = rospy.Rate(10) # 10hz

pub = rospy.Publisher('joint_states', JointState, queue_size=10)

def publishJoints(target_joints):
  print("standup")
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
  servo_states.position = [robot_joints[10], robot_joints[11], robot_joints[5], robot_joints[6], robot_joints[7], robot_joints[8], robot_joints[9], robot_joints[0], robot_joints[1], robot_joints[2], robot_joints[3], robot_joints[4]]
  servo_states.velocity = []
  servo_states.effort = []

  servo_states.header.stamp = rospy.Time.now() #always set the header stamp before updating the joints
  pub.publish(servo_states)
  rate.sleep()

def standup():
  for joints in range(TOTAL_JOINTS):
    robot_joints[joints] = 0.0
  publishJoints(robot_joints)

def inverseKinematics():
  print("Inverse Kinematics")

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
        while not rospy.is_shutdown():
          standup()
    except rospy.ROSInterruptException:
        pass