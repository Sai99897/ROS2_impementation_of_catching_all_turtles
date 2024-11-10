from os import access
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld=LaunchDescription()

    turtlesim_node=Node(
        package="turtlesim",
        executable="turtlesim_node",
    )

    turtlesim_controller_node=Node(
        package="turtlrsim_catch_them_all",
        executable="turtlesim_controller",
        parameters=[
            {"catch_closest_turtle_fisrt": True}
            
        ]

    )


    turtlesim_spawner_node=Node(
        package="turtlrsim_catch_them_all",
        executable="turtle_spawner",
        parameters=[
            {"spawn_frequency":2.0},
            {"turtle_name_prefix":"my_turtle"}
            
        ]

    )


    ld.add_action(turtlesim_node)
    ld.add_action(turtlesim_controller_node)
    ld.add_action(turtlesim_spawner_node)
    return ld