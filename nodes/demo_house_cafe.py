#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point 
from std_msgs.msg import Byte
#from sound_play.libsoundplay import SoundClient
global Value

class map_navigation():
	def choose(self):

		choice='q'

		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|Loading Food >>>>>>>>>>>>>>>>>>")
		rospy.loginfo("|PRESSE A KEY:")
		rospy.loginfo("|'0': Go to Point Start >>>>>>>>>> ")
		rospy.loginfo("|'1': Go to Table 1 >>>>>>>>>> ")
		rospy.loginfo("|'2': Go to Table 2 >>>>>>>>>> ")
		rospy.loginfo("|'3': Go to Table 3 >>>>>>>>>> ")
		rospy.loginfo("|'4': Go to Table 4 >>>>>>>>>> ")
		rospy.loginfo("|'q': Quit ")
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|WHERE TO GO?")
		choice = input()
		return choice
			
	def __init__(self): 
		self.button_sub = rospy.Subscriber('button', Byte, self.get_button, queue_size = 1)
		#sc = SoundClient()
		#path_to_sounds = "/home/ros/catkin_ws/src/gaitech_edu/src/sounds/"

		# declare the coordinates of interest 
		self.xStart_Point =  0.04
		self.yStart_Point = 0.27
		self.xCounter = 0.04
		self.yCounter = 0.27
		self.xTable1 = 1.18
		self.yTable1 = 2.23
		self.xTable2 = 0.08
		self.yTable2 = 1.01
		self.xTable3 = 1.87
		self.yTable3 = -0.05
		self.xTable4 = 0.01
		self.yTable4 = 1.56
		self.goalReached = False
		# initiliaze
        rospy.init_node('demo_house_cafe', anonymous=False)
		choice = self.choose()
		
		if (choice == 0 ):

			self.goalReached = self.moveToGoal(self.xStart_Point, self.yStart_Point)
		
		elif (choice == 1):

			self.goalReached = self.moveToGoal(self.xTable1, self.yTable1)

		elif (choice == 2):
			
			self.goalReached = self.moveToGoal(self.xTable2, self.yTable2)
		
		elif (choice == 3):

			self.goalReached = self.moveToGoal(self.xTable3, self.yTable3)

		elif (choice == 4):

			self.goalReached = self.moveToGoal(self.xTable4, self.yTable4)

		if (choice!='q'):

			if (self.goalReached):
				rospy.loginfo("Congratulations!")
				#rospy.spin()

				#sc.playWave(path_to_sounds+"ship_bell.wav")
				
				#rospy.spin()

			else:
				rospy.loginfo("Hard Luck!")
				#sc.playWave(path_to_sounds+"short_buzzer.wav")
		
		while choice != 'q':
			choice = self.choose()
			if (choice == 0):

				self.goalReached = self.moveToGoal(self.xStart_Point, self.yStart_Point)
		
			elif (choice == 1):

				self.goalReached = self.moveToGoal(self.xTable1, self.yTable1)

			elif (choice == 2):
		
				self.goalReached = self.moveToGoal(self.xTable2, self.yTable2)
		
			elif (choice == 3):

				self.goalReached = self.moveToGoal(self.xTable3, self.yTable3)

			elif (choice == 4):

				self.goalReached = self.moveToGoal(self.xTable4, self.yTable4)

			if (choice!='q'):

				if (self.goalReached):
					rospy.loginfo("Congratulations!")
					#rospy.spin()

					#sc.playWave(path_to_sounds+"ship_bell.wav")

				else:
					rospy.loginfo("Hard Luck!")
					#sc.playWave(path_to_sounds+"short_buzzer.wav")

	def get_button(self, button):
		if button.data == 0 :
			self.goalReached = self.moveToGoal(self.xStart_Point, self.yStart_Point)
			rospy.loginfo("End Calling >>>>>>>>")
			rospy.loginfo("Go To Point Start >>>>>>>>")
		
		elif button.data == 1:
			self.goalReached = self.moveToGoal(self.xTable1, self.yTable1)
			rospy.loginfo("Table 1 Calling >>>>>>>>")
			rospy.loginfo("Presse a key '1' to go Table1 >>>>>>>>")

		elif button.data == 2:
			self.goalReached = self.moveToGoal(self.xTable2, self.yTable2)
			rospy.loginfo("Table 2 Calling >>>>>>>>")
			rospy.loginfo("Presse a key '2' to go Table2 >>>>>>>>")
		
		elif button.data == 3:
			self.goalReached = self.moveToGoal(self.xTable3, self.yTable3)
			rospy.loginfo("Table 3 Calling >>>>>>>>")
			rospy.loginfo("Presse a key '3' to go Table3 >>>>>>>>")

		elif button.data == 4:
			self.goalReached = self.moveToGoal(self.xTable4, self.yTable4)
			rospy.loginfo("Table 4 Calling >>>>>>>>")
			rospy.loginfo("Presse a key '4' to go Table4 >>>>>>>>")


	def shutdown(self):
        # stop turtlebot
        	rospy.loginfo("Quit program")
        	rospy.sleep()

	def moveToGoal(self,xGoal,yGoal):

		#define a client for to send goal requests to the move_base server through a SimpleActionClient
		ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

		#wait for the action server to come up
		while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
			rospy.loginfo("Waiting for the move_base action server to come up")
		

		goal = MoveBaseGoal()

		#set up the frame parameters
		goal.target_pose.header.frame_id = "map"
		goal.target_pose.header.stamp = rospy.Time.now()

		# moving towards the goal*/

		goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
		goal.target_pose.pose.orientation.x = 0.0
		goal.target_pose.pose.orientation.y = 0.0
		goal.target_pose.pose.orientation.z = 0.0
		goal.target_pose.pose.orientation.w = 1.0

		rospy.loginfo("Sending goal location ...")
		ac.send_goal(goal)

		ac.wait_for_result(rospy.Duration(60))

		if(ac.get_state() ==  GoalStatus.SUCCEEDED):
			rospy.loginfo("You have reached the destination")	
			return True
	
		else:
			rospy.loginfo("The robot failed to reach the destination")
			return False

if __name__ == '__main__':
    try:
	
	rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
