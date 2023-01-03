Following a Chinese ROS2 tutorial.(https://blog.csdn.net/qq_27865227/article/details/125069257)

Works as a test project for the ongoing drone SLAM project.

description:

1.node-fishbot_description:model of a differential drive robot and storage of a test environment.
2.node-fishbot_cartographer:SLAM node for the differential drive robot.
3.node-fishbot_navigation2:navigation configuration for the differential drive robot.



mapping:
First terminal:
1.cd fishbot_ws
2.source install/setup.bash
3.ros2 run teleop_twist_keyboard teleop_twist_keyboard

Second terminal:
1.cd fishbot_ws
2.source install/setup.bash
3.ros2 launch fishbot_description gazebo.launch.py

Third terminal:
1.cd fishbot_ws
2.source install/setup.bash
3.ros2 launch fishbot_cartographer cartographer.launch.py



navigation:
First terminal:
1.cd fishbot_ws
2.source install/setup.bash
3.ros2 launch fishbot_description gazebo.launch.py

Second terminal:
1.cd fishbot_ws
2.source install/setup.bash
3.ros2 launch fishbot_navigation2 navigation2.launch.py


rosbag recording: ros2 bag record -o SLAMDATA /tf /odom /scan /tf_static

