#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subsciber_ = self.create_subscription(Pose, "/turtle1/pose",self.pose_callback,10)
        self.get_logger().info("Draw circle node has been started")
        
    def pose_callback(self,msg:Pose):
        self.get_logger().info("(" + str(msg.x)+","+ str(msg.y)+ ")")
        # msg = Pose()
        # msg.linear.x = 2.0 
        # msg.angular.z = 3.0
        # self.pose_subsciber_.subscribe(msg)

def main(args=None):

    # Intializing the node
    rclpy.init(args=args)

    # Node 
    node = PoseSubscriberNode()
    rclpy.spin(node)

    #Shutting down the node
    rclpy.shutdown

if __name__ == '__main__':
    main()