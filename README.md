Folders and files explanation
.vscode, build, install, log:  autocreated, do nothing
src:      contains pkg
- rmit_description:     See lesson2. Otherwise, the added information are:
    - rmitbot_ros2_control.xacro:   File added to describe the control of the robot
    - rmitbot.urdf.xacro:           File updated to include rmitbot_ros2_control.xacro
    - pacakge.xml:                  add the depedency for ros2_control
- rmit_controller: 
    - config/rmitbot_controller.yaml: configuration of the ros2_controller pkg
    - include: no node, so empty
    - launch:
        - controller:       
            - wheel_controller_spawner,         spawn the controller for the wheel
            - joint_state_broadcaster_spawner,  spawn the encoder reading
        - teleopkeyboard: 
            - use_sim_time_arg,                 use simulation time
            - teleop_keyboard,                  use keyboard to give twist command
    - src: no node, so empty
    - CMakeLists.txt: folders added: launch config
    - package.xml: depedency: 
        - ros2launch
        - robot_state_publisher
        - xacro
        - controller_manager
  