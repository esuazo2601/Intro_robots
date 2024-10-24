from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([FindPackageShare('gazebo_ros'), '/launch/gazebo.launch.py'])
    )

    servo_controller_node = Node(
        package='servo_controller',
        executable='servo_controller',
        name='servo_controller',
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        servo_controller_node
    ])