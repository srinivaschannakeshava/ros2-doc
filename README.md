# ROS-2

## Why ROS-2?

- ROS- Robot Operating System
- Provide a standard for robotic applications
- Use on any robot
- What is ROS-2?
  - Provides Code separation and communication tools
  - Provide Tools and Plug&Play Library
  - Language Agnostic

## Installing ROS-2

- https://docs.ros.org/en/rolling/Releases.html - choose the Distro with LTS support
- https://docs.ros.org/en/humble/Installation.html - Bumble Hawksbill distro
- add ros2 to bash 
  - ` nano ~/.bashrc `
  - add the line in end of file ` source /opt/ros/humble/setup.bash `
- build tool for ros2 apps
  - `sudo apt install python3-colcon-common-extensions`
  - add this to source for autocomplete of build of ros2 package in bashrc- `source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash`

## Creating a simple project

- create a workspace folder - ex - `mkdir ros2-ws` and create a src folder inside
- run `colcon build` inside the ros2-ws folder - this generates the folder and files - build, install,logs 
- `source local_setup.sh` which is inside install folder to have app on the terminal - `source setup.bash` to have on global
- inside src folder run the following cmd to create a python package 
  - `ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy`  - here ament_python is the python builder engine for ros , rclpy is a ros python library

- build the project from ros2_ws using the cmd - `colcon build` - if error on build - try downgrading the `pip3 install setuptool==58.2.0`

### ROS Node

- Node -Subprogram in your application , responsible for only one thing
- Combined into a graph
- Communicate with each other through topics,services and parameters

- Package is independent unit inside your application
- Nodes inside package
- Nodes communicate using RoS communication topics

- Why Nodes
  - reduce code complexity
  - Fault Tolerance
  - Can be written in Python,C++ ...
- Nodes name should be unique

### Running app from ROS cmd

> edit `setup.py` - add entrypoint in consolescript as in ex app. `"py_node = my_py_pkg.first_node:main"`
> `colcon build --packages-select my_py_pkg`
> inside install folder `source setup.bash` - run app by `ros2 run my_py_pkg py_node`

### Debugging and monitoring Nodes in ROS2

- `ros2 node list` - lists nodes
- `ros2 node info /firstNode` - give info about node named firstNode
- running node with diff name during runtime
  - `ros2 run my_py_pkg first_node --ros-arg --remap __node:=abc`

- you can use `colcon build --packages-select my_py_pkg --symlink-install` - this will create a symlink with python source file so that you need not compile evertim eyou make changes during dev - for this to work you need to make your python scripts executable i.e chmod +x ..
- rqt - graph tool for visualizing nodes/data //... etc
- turtlesim -

### ROS Topics

- A topic is a named bus over which nodes exchange messages
- Data streams are Unidirectional from publisher to subscriber
- A topic has a message type

> `ros2 interface show example_interfaces/msg/String` \
> `ros2 topic list` - list the live topics \
> `ros2 topic echo /rb_news` - echos messages published on topic **/rb_news** \
> `ros2 topic info /rb_news` \
> `ros2 topic hz /rb_news` - gets frequency of publication \
> `ros2 topic pub -r 10 /rb_news example_interfaces/msg/String  "{data: 'hello from term'}"` - here r is message frequency/sec , message type , message \
> `ros2 run my_py_pkg rb_news --ros-args -r __node:=my_stat -r rb_news:=my_news` - change the default node name during runtime to my_stat and topic name to my_news from rb_news

## ROS services

- The 2 most important communication features in ROS2 are Topics and Services.
- Topics are used for data streams, and Services for a client/server interaction.
- A ROS2 service is a client/server system
  - synchronous or asynchronous
  - a service server can only exist once but can have many clients

> `ros2 service list` \
> `ros2 service call /add_two_ints example_interface/srv/AddTwoInts "{a: 1,b: 2}"` \

## ROS2 Interfaces

- 