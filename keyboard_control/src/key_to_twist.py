#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
key_mapping = { 'w': [ 0, 1], 's': [0, -1],
				'a': [-1, 0], 'd': [1, 0] }
def keys_cb(msg, twist_pub):
	t = Twist()
	if msg.data == '0':
		t.angular.z = 0
		t.linear.x = 0
		twist_pub.publish(t)
	elif len(msg.data) == 0 or msg.data not in ['w','s','a','d']:
		pass
	else:
		vels = key_mapping[msg.data[0]]
		t.angular.z = vels[0]
		t.linear.x = vels[1]
		twist_pub.publish(t)
if __name__ == '__main__':
	rospy.init_node('keys_to_twist')
	twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.Subscriber('keys', String, keys_cb, twist_pub)
	rospy.spin()
