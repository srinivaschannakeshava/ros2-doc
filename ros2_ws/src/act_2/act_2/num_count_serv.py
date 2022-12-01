#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("num_pub_serv")  # MODIFY NAME
        self.counter_=0
        self.publisher_=self.create_publisher(Int64,"number_count",10)
        self.subscriber_=self.create_subscription(Int64,"number",self.num_cb, 10)
        self.get_logger().info("Number Counter started..")
        self.server_=self.create_service(
            SetBool, "reset_counter", self.cb_reset_counter)

    def cb_reset_counter(self,req,resp):
        reset:bool=req.data
        if(reset):
          self.counter_=0
        self.get_logger().info("Reset : "+str(reset))
        resp.success=True
        return resp

    def publish_num(self,num):
        msg=Int64()
        msg.data=num
        self.publisher_.publish(msg)
        self.get_logger().info("Number Count Sum Published : "+str(num))

    def num_cb(self,msg):
        self.get_logger().info("received mesage: "+str(msg.data))
        self.counter_=self.counter_+msg.data
        self.publish_num(self.counter_)



def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
