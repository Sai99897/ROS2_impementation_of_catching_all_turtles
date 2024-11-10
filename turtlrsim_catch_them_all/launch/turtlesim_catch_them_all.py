from os import access
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package="turtlesim",
            executable="turtlesim_node",
            output='screen',
        ),

        Node(
            package="turtlrsim_catch_them_all",
            executable="turtlesim_controller",
            output='screen',
            parameters=[
                {"catch_closest_turtle_fisrt": True}
                
            ],

        ),


        Node(
            package="turtlrsim_catch_them_all",
            executable="turtle_spawner",
            output='screen',
            parameters=[
                {"spawn_frequency":2.0},
                {"turtle_name_prefix":"my_turtle"}
                
            ],
        ),

    ])


   

    


    


    