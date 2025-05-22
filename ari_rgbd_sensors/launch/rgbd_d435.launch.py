# Copyright (c) 2025 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node as RclpyNode
from launch import LaunchDescription
from launch_ros.actions import LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode
from launch_pal import get_pal_configuration


def generate_launch_description():

    ld = LaunchDescription()

    torso_front_camera_node = 'torso_front_rgbd_camera'
    torso_back_camera_node = 'torso_back_stereo_camera'
    torso_front_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=torso_front_camera_node,
        ld=ld,
        cmdline_args=False,
    )
    torso_back_camera_config = get_pal_configuration(
        pkg='realsense_deprecated_camera_cfg',
        node=torso_back_camera_node,
        ld=ld,
        cmdline_args=False,
    )

    # If the container node already exists, just load the component
    rclpy.init()
    node = RclpyNode('node_checker')
    rclpy.spin_once(node, timeout_sec=1.0)
    if 'rgbd_container' not in node.get_node_names():
        rgbd_container = Node(
            name='rgbd_container',
            package='rclcpp_components',
            executable='component_container',
            emulate_tty=True,
            output='screen',
        )
        ld.add_action(rgbd_container)
    rclpy.shutdown()

    camera_components = LoadComposableNodes(
        target_container='rgbd_container',
        composable_node_descriptions=[
            # Torso Front Camera Driver
            ComposableNode(
                package='realsense2_camera',
                plugin='realsense2_camera::RealSenseNodeFactory',
                name=torso_front_camera_node,
                namespace='torso_front_rgbd_camera',
                parameters=torso_front_camera_config["parameters"],
                remappings=torso_front_camera_config["remappings"],
            ),
            # Torso Back Camera Driver
            ComposableNode(
                package='realsense2_camera',
                plugin='realsense2_camera::RealSenseNodeFactory',
                name=torso_back_camera_node,
                namespace='torso_back_stereo_camera',
                parameters=torso_back_camera_config["parameters"],
                remappings=torso_back_camera_config["remappings"],
            ),
        ],
    )

    ld.add_action(camera_components)
    return ld
