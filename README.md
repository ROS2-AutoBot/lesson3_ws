Folders and files explanation
.vscode, build, install, log:  autocreated, do nothing
src:      contains pkg
- rmit_description:     See lesson2. Otherwise, the added information are:
    - urdf/rmitbot_ros2_control.xacro:  define control parameters of the wheel
    - pacakge.xml:      add the depedency ros2_control
- rmit_controller: 
    - config/rmitbot_controller.yaml: configuration of the ros2_controller pkg
    - include: no node, so useless
    - launch:
        - controller:       
            - use_sim_time_arg,
            - use_python_arg,
            - wheel_radius_arg,
            - wheel_separation_arg,
            - wheel_controller_spawner,
            - joint_state_broadcaster_spawner,
        - teleopkeyboard: 
            - use_sim_time_arg, 
            - teleop_keyboard, 
    - src: no node, so useless
    - CMakeLists.txt: folders added: launch config
    - package.xml: depedency: 
        - ros2launch
        - robot_state_publisher
        - xacro
        - controller_manager
 
  