#!/bin/bash

# Argument (default to iiwa14)
MODEL=${1:-iiwa14}

# Get install paths using ros2 pkg prefix
PKG_PREFIX=$(ros2 pkg prefix serial_link_velocity_control)
CONFIG_DIR="${PKG_PREFIX}/share/serial_link_velocity_control/config"

# Open a new terminal and run the action server
gnome-terminal -- bash -c "ros2 launch serial_link_velocity_control follow_twist.py model:=${MODEL}; exec bash"

# Wait for the server to start
sleep 1

# Run the client with installed parameter file paths
ros2 run serial_link_action_client follow_twist_client \
  --ros-args \
  --params-file "${CONFIG_DIR}/${MODEL}/joint_configurations.yaml" \
  --params-file "${CONFIG_DIR}/tolerances.yaml"
