import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    package_name = 'servo_controller'
    urdf_file_name = 'my_turtlebot3_burger.urdf'
    urdf = os.path.join(get_package_share_directory(package_name), 'urdf', urdf_file_name)

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', urdf],
            output='screen'
        )
    ])