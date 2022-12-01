#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntClientNode(Node):
    def __init__(self):
        super().__init__("add_two_int_client")
        self.client_ = self.create_client(
            AddTwoInts, "add_two_ints")
        self.get_logger().info("Add Two Ints client started..")
        self.call_add_two_ints_serv(10,12)
        self.call_add_two_ints_serv(3,6)
        self.call_add_two_ints_serv(15,1)

    def call_add_two_ints_serv(self, a, b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server !!")
        req= AddTwoInts.Request()
        req.a=a
        req.b=b
        future = self.client_.call_async(req)
        future.add_done_callback(partial(self.cb_call_add_to_int,a=a,b=b))

    def cb_call_add_to_int(self,future,a,b):
      try:
        resp = future.result()
        self.get_logger().info(str(a)+"+"+str(b)+"="+str(resp.sum))
      except Exception as e:
        self.get_logger().error("Service call failed %r" %(e,))  

def main(args=None):
    rclpy.init(args=args)
    node= AddTwoIntClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()