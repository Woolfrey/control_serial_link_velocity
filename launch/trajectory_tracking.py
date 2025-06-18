import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import OpaqueFunction

def launch_setup(context, *args, **kwargs):

    model = LaunchConfiguration('model').perform(context)                                           # Launch argument

    endpoint_map = {
        'iiwa14' : 'link7',
        'panda'  : 'link72attachment_fixed_jointbody',                                              # This is what it's called in the converted .xml file
        'sawyer' : 'right_l6',
        'ur10e'  : 'wrist_3_link'
    }

    if model not in endpoint_map:
        raise RuntimeError(f"Unknown model '{model}'")

    endpoint_name = endpoint_map[model]                                                             # Get the name of the endpoint from the map

    package_dir = get_package_share_directory('serial_link_velocity_control')
    
    this_directory = os.path.dirname(__file__)
    
    urdf_path = os.path.join(package_dir, 'urdf', f'{model}', f'{model}.urdf')

    # Nodes
    server = Node(
        package    = 'serial_link_action_server',
        executable = 'trajectory_tracking_server',
        name       = 'trajectory_tracking_server',
        output     = 'screen',
        parameters = [os.path.join(package_dir, 'config/control_parameters.yaml')],
        arguments  = [urdf_path, 
                      endpoint_name, 
                      'joint_command_relay', 
                      'joint_states',                                                                # Joint state topic to subscribe to
                      'VELOCITY']
    )

    relay = Node(
        package    = 'serial_link_velocity_control',
        executable = 'joint_command_relay',
        name       = 'joint_command_relay',
        output     = 'screen',
        arguments = ['joint_command_relay', 
                     'joint_command_relay', 
                     'joint_commands']
    )

    robot_state = Node(
        package    = 'robot_state_publisher',
        executable = 'robot_state_publisher',
        name       = 'robot_state_publisher',
        output     = 'screen',
        parameters = [{'robot_description': open(urdf_path).read()}]
    )

    rviz = Node(
        package    = 'rviz2',
        executable = 'rviz2',
        name       = 'rviz2',
        output     = 'screen',
        arguments  = ['-d', os.path.join(this_directory, '../rviz/trajectory_tracking.rviz')]
    )

    return [server, relay, robot_state, rviz]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('robot_model', default_value='iiwa14', description='Name of robot model'),
        OpaqueFunction(function=launch_setup)
    ])

