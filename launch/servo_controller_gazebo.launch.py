from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Ruta relativa al archivo URDF
    urdf_file = os.path.join(
        get_package_share_directory('servo_controller'),
        'urdf',
        'my_turtlebot3_burger.urdf'
    )

    return LaunchDescription([
        # Lanzar Gazebo y spawnear la entidad TurtleBot con el URDF personalizado
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'my_turtlebot3', '-file', urdf_file],
            output='screen'
        ),
        # Publicar el estado del robot
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_file],
            output='screen'
        ),
    ])
