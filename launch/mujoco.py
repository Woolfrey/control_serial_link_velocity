#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def launch_setup(context, *args, **kwargs):

    model = LaunchConfiguration('model').perform(context)
    
    mujoco_menagerie_directory = "/home/woolfrey/workspace/mujoco_menagerie"
    
    if not os.path.exists(mujoco_menagerie_directory):
        raise FileNotFoundError(f"Directory does not exist: {mujoco_menagerie_directory}")

    scene_map = {
        'iiwa14' : os.path.join(mujoco_menagerie_directory, 'kuka_iiwa_14/scene.xml'),
        'panda'  : os.path.join(mujoco_menagerie_directory, 'franka_emika_panda/scene.xml'),
        'sawyer' : os.path.join(mujoco_menagerie_directory, 'rethink_robotics_sawyer/scene.xml'),
        'ur10e'  : os.path.join(mujoco_menagerie_directory, 'universal_robots_ur10e/scene.xml')
    }
    
    scene = scene_map[model]
    
    mujoco = Node(
        package    = "mujoco_ros2",
        executable = "mujoco_node",
        output     = "screen",
        arguments  = [scene],
        parameters = [{"joint_state_topic_name"   : "joint_states"},
                      {"joint_command_topic_name" : "joint_commands"},
                      {"control_mode"             : "VELOCITY"},
                      {"simulation_frequency"     : 1000},
                      {"visualisation_frequency"  : 20},
                      {"camera_focal_point"       : [0.0, 0.0, 0.5]},
                      {"camera_distance"          : 2.5},
                      {"camera_azimuth"           : 135.0},
                      {"camera_elevation"         : -35.0},
                      {"camera_orthographic"      : True}
        ]
    )

    return [mujoco]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'model',
            default_value = 'iiwa14',
            description = 'Subfolder name in mujoco_menagerie containing scene.xml'
        ),
        OpaqueFunction(function=launch_setup)
    ])

