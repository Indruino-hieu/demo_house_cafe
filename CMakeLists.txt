cmake_minimum_required(VERSION 3.0.2)
project(demo_house_cafe)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib
  roscpp
  rospy
  std_msgs
)

################################################################################
# Setup for python modules and scripts
################################################################################
catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS 
  actionlib 
  roscpp 
  rospy 
  std_msgs
)

###########
## Build ##
###########
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

# Install
################################################################################
catkin_install_python(PROGRAMS
  nodes/demo_house_cafe
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

################################################################################
# Test
################################################################################
