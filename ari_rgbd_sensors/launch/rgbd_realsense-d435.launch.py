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

import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_pal import get_pal_configuration


def generate_launch_description():

    ld = LaunchDescription()

    torso_front_camera_node = 'torso_front_rgbd_camera'
    torso_front_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=torso_front_camera_node,
        ld=ld,
        cmdline_args=False,
    )

    # Torso Front Camera Driver
    camera_node = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node',
        name=torso_front_camera_node,
        output='screen',
        emulate_tty=True,
        namespace='torso_front_rgbd_camera',
        parameters=torso_front_camera_config["parameters"],
        remappings=torso_front_camera_config["remappings"],
    )

    ld.add_action(camera_node)
    rgbd_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='ari_rgbd_sensors',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(
                get_package_share_directory('ari_rgbd_sensors'),
                'config', 'rgbd_analyzers.yaml')],
    )
    ld.add_action(rgbd_analyzer)
    return ld
