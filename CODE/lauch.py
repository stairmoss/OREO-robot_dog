import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Path to the parameters file
    config = os.path.join(
        get_package_share_directory('oreo_robot'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        # 1. Serial Bridge Node (Teensy Communication)
        Node(
            package='oreo_robot',
            executable='serial_bridge',
            name='serial_bridge',
            parameters=[config],
            output='screen'
        ),
        
        # 2. Control & Gait Node (Kinematics)
        Node(
            package='oreo_robot',
            executable='kinematics',
            name='gait_manager',
            parameters=[config],
            output='screen'
        ),
        
        # 3. Vision Node (Ball Following)
        Node(
            package='oreo_robot',
            executable='vision',
            name='vision_node',
            output='screen'
        )
    ])