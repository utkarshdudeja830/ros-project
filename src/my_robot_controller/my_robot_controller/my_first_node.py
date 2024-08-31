#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("my_first_node")
        #self.get_logger().info("Hello fro ROS#")
        self.create_timer(1.0, self.callback)
    def callback(self):
        self.get_logger().info("Hello fro ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)



    rclpy.shutdown

if __name__ == '__main__':
    main()