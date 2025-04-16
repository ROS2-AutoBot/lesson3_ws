import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, GroupAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    # Some parameters
    # use_sim_time_arg = DeclareLaunchArgument(
    #     "use_sim_time",
    #     default_value="True",
    # )
    # use_python_arg = DeclareLaunchArgument(
    #     "use_python",
    #     default_value="False",
    # )
    # wheel_radius_arg = DeclareLaunchArgument(
    #     "wheel_radius",
    #     default_value="0.033",
    # )
    # wheel_separation_arg = DeclareLaunchArgument(
    #     "wheel_separation",
    #     default_value="0.17",
    # )
    
    # use_sim_time = LaunchConfiguration("use_sim_time")
    # use_simple_controller = LaunchConfiguration("use_simple_controller")
    # use_python = LaunchConfiguration("use_python")
    # wheel_radius = LaunchConfiguration("wheel_radius")
    # wheel_separation = LaunchConfiguration("wheel_separation")


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
            # use_sim_time_arg,
            # use_python_arg,
            # wheel_radius_arg,
            # wheel_separation_arg,
            wheel_controller_spawner,
            joint_state_broadcaster_spawner,
        ]
    )