import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # locate related package
    pkg_share = FindPackageShare(package='fishbot_cartographer').find('fishbot_cartographer')
    
    #=====================configuration for nodes=======================================================================
    # use_sim_time = true for gazebo
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # resolution for map
    resolution = LaunchConfiguration('resolution', default='0.05')
    # publish_period for map
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')
    # set path for directory
    configuration_directory = LaunchConfiguration('configuration_directory',default= os.path.join(pkg_share, 'config') )
    # configuration file
    configuration_basename = LaunchConfiguration('configuration_basename', default='fishbot_2d.lua')

    
    #=====================declare 3 nodes, cartographer/occupancy_grid_node/rviz_node=================================
    cartographer_node = Node(
        package='cartographer_ros',
        executable='cartographer_node',
        name='cartographer_node',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-configuration_directory', configuration_directory,
                   '-configuration_basename', configuration_basename])

    occupancy_grid_node = Node(
        package='cartographer_ros',
        executable='occupancy_grid_node',
        name='occupancy_grid_node',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-resolution', resolution, '-publish_period_sec', publish_period_sec])

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        # arguments=['-d', rviz_config_dir],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen')

    #===============================================define launch file========================================================
    ld = LaunchDescription()
    ld.add_action(cartographer_node)
    ld.add_action(occupancy_grid_node)
    ld.add_action(rviz_node)

    return ld

