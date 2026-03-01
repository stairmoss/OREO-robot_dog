import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import serial
import time

class SerialBridgeNode(Node):
    def __init__(self):
        super().__init__('serial_bridge_node')
        self.declare_parameter('port', '/dev/ttyACM0')
        self.declare_parameter('baud', 115200)
        
        port = self.get_parameter('port').value
        baud = self.get_parameter('baud').value

        try:
            self.ser = serial.Serial(port, baud, timeout=0.1)
            self.get_logger().info(f"Connected to Teensy on {port}")
        except Exception as e:
            self.get_logger().error(f"Failed to connect: {e}")

        self.subscription = self.create_subscription(
            Int32MultiArray,
            '/joint_angles',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        if len(msg.data) == 12:
            # Format: S,a1,a2,...,a12\n
            angle_str = ",".join(map(str, msg.data))
            packet = f"S,{angle_str}\n"
            self.ser.write(packet.encode())

def main(args=None):
    rclpy.init(args=args)
    node = SerialBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()