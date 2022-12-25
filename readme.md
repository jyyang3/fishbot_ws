Following a Chinese ROS2 tutorial.(https://blog.csdn.net/qq_27865227/article/details/125069257)

Works as a test project for the ongoing drone SLAM project.

description:

1.node-fishbot_description:model of a differential drive robot and storage of a test environment.
2.node-fishbot_cartographer:SLAM node for the differential drive robot.
3.node-fishbot_navigation2:navigation configuration for the differential drive robot.

run 1 and 2 for mapping
run 1 and 3 for navigation

rosbag recording: ros2 bag record -o SLAMDATA /tf /odom /scan /tf_static
