
from launch import LaunchDescription
fromlaunch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    ])

