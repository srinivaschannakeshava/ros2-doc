#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("num_pub")  # MODIFY NAME
        self.counter_=0
        self.publisher_=self.create_publisher(Int64,"number_count",10)
        self.subscriber_=self.create_subscription(Int64,"number",self.num_cb, 10)
        self.get_logger().info("Number Counter started..")

    def publish_num(self,num):
        msg=Int64()
        msg.data=num
        self.publisher_.publish(msg)
        self.get_logger().info("Number count Published : "+str(num))

    def num_cb(self,msg):
        self.get_logger().info("receife mesage: "+str(msg.data))
        self.counter_=self.counter_+msg.data
        self.publish_num(self.counter_)



def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
