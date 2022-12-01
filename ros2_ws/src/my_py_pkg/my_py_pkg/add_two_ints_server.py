#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(
            AddTwoInts, "add_two_ints", self.cb_add_two_ints)
        self.get_logger().info("Add Two Ints server started..")

    def cb_add_two_ints(self, req, resp):
        resp.sum = req.a+req.b
        self.get_logger().info(str(req.a)+"+"+str(req.b)+"="+str(resp.sum))
        return resp


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
