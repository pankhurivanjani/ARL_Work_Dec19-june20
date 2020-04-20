############################dual_ekf_navsat_example.launch###############################
#<!--
#     This launch file provides an example of how to work with GPS data using robot_localization. It runs three nodes:
#       (1) An EKF instance that fuses odometry and IMU data and outputs an odom-frame state estimate
#       (2) A second EKF instance that fuses the same data, but also fuses the transformed GPS data from (3)
#      (3) An instance of navsat_transform_node, which takes in GPS data and produces pose data that has been
#           transformed into your robot's world frame (here, map). The node produces a map-frame state estimate.
#       The first EKF instance produces the odom->base_link transform. The second EKF produces the map->odom transform,
#       but requires the odom->base_link transform from the first instance in order to do so. See the
#       params/dual_ekf_navsat_example.yaml file for parameter specification.
#-->

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='robot_localization',
            node_executable='ekf_node',
            node_name='ekf_filter_node_odom',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("robot_localization"), 'params', 'dual_ekf_navsat_example.yaml')],
           ),

        launch_ros.actions.Node(
            package='robot_localization',
            node_executable='ekf_node',
            node_name='ekf_filter_node_map',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("robot_localization"), 'params', 'dual_ekf_navsat_example.yaml')],
           ),

        launch_ros.actions.Node(
            package='robot_localization',
            node_executable='navsat_transform_node',
            node_name='navsat_transform_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("robot_localization"), 'params', 'dual_ekf_navsat_example.yaml')],
           ),   
 
])
#remappings=[('__params', get_package_share_directory('test')+"/cfg/demo.yaml")])

####################################

#        launch_ros.actions.Node(
#            package='robot_localization',
#            node_executable='ekf_node',
#            node_name='ekf_filter_node_odom',
#            output='screen',
#            parameters=[os.path.join(get_package_share_directory("robot_localization"), 'params', 'dual_ekf_navsat_example.yaml')],
#           ),

#        launch_ros.actions.Node(
#            package='robot_localization',
#            node_executable='ekf_node',
#            node_name='ekf_filter_node_map',
#            output='screen',
#            parameters=[os.path.join(get_package_share_directory("robot_localization"), 'params', 'dual_ekf_navsat_example.yaml')],
#           ),
