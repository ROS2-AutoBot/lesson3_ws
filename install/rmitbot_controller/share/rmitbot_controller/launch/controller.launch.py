import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )
    
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["rmitbot_controller", 
                   "--controller-manager", 
                   "/controller_manager"
        ]
    )

    return LaunchDescription(
        [
            wheel_controller_spawner,
            joint_state_broadcaster_spawner,
        ]
    )