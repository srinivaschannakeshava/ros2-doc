#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPublisherNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("num_pub")  # MODIFY NAME
        self.publisher_=self.create_publisher(Int64,"number",10)
        self.timer_=self.create_timer(2, self.publish_num)
        self.get_logger().info("Number Publisher started..")

    def publish_num(self):
        num=Int64()
        num.data=2
        self.publisher_.publish(num)
        self.get_logger().info("Number Published : "+str(num))




def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
