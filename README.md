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
            - wheel_controller_spawner,         spawn the controller for the wheel
            - joint_state_broadcaster_spawner,  spawn the encoder reading
        - teleopkeyboard: 
            - use_sim_time_arg,                 use simulation time
            - teleop_keyboard,                  use keyboard to give twist command
    - src: no node, so useless
    - CMakeLists.txt: folders added: launch config
    - package.xml: depedency: 
        - ros2launch
        - robot_state_publisher
        - xacro
        - controller_manager
  