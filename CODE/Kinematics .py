import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray
import math
import numpy as np

class OreoKinematics:
    """3-DOF Inverse Kinematics for OREO Leg"""
    def __init__(self, L_coxa=40, L_femur=100, L_tibia=100):
        self.L1 = L_coxa
        self.L2 = L_femur
        self.L3 = L_tibia

    def solve_ik(self, x, y, z):
        # Angle 1: Coxa (Hip Yaw)
        theta1 = math.atan2(y, x)
        
        # Distance in XY plane from coxa joint to foot
        r = math.sqrt(x**2 + y**2) - self.L1
        
        # Distance from shoulder (femur joint) to foot in the R-Z plane
        s = math.sqrt(r**2 + z**2)
        
        # Cosine rule for Theta3 (Tibia)
        cos_theta3 = (self.L2**2 + self.L3**2 - s**2) / (2 * self.L2 * self.L3)
        cos_theta3 = max(-1, min(1, cos_theta3)) # Clamp
        theta3 = math.acos(cos_theta3)
        
        # Theta2 (Femur)
        phi1 = math.atan2(z, r)
        phi2 = math.acos((self.L2**2 + s**2 - self.L3**2) / (2 * self.L2 * s))
        theta2 = phi1 + phi2

        # Convert to degrees and shift to 0-180 range (approx)
        return [
            math.degrees(theta1) + 90,
            math.degrees(theta2) + 90,
            math.degrees(theta3)
        ]

class GaitManagerNode(Node):
    def __init__(self):
        super().__init__('gait_manager_node')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/joint_angles', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        
        self.ik = OreoKinematics()
        self.timer = self.create_timer(0.02, self.update_gait) # 50Hz
        
        self.velocity = 0.0
        self.step_height = 30.0
        self.t = 0.0 # Time phase

    def cmd_vel_callback(self, msg):
        self.velocity = msg.linear.x

    def update_gait(self):
        # Very simplified Trot Gait Logic
        # Each leg moves in a sine wave trajectory
        # Leg 0 & 3 (Group A), Leg 1 & 2 (Group B)
        
        angles = []
        # Normal standing height Z = -120
        base_z = -120 
        
        # Calculate X/Z offsets based on time t and velocity
        phase_a = math.sin(self.t)
        phase_b = math.sin(self.t + math.pi)
        
        for i in range(4):
            # Alternate legs
            p = phase_a if i in [0, 3] else phase_b
            
            x = self.velocity * p * 50  # Stride length
            z = base_z + (abs(p) * self.step_height if p > 0 else 0)
            y = 0 # Assume straight line
            
            angles.extend(self.ik.solve_ik(x + 50, y, z)) # Offset x by 50 for neutral pos

        msg = Int32MultiArray()
        msg.data = [int(a) for a in angles]
        self.publisher_.publish(msg)
        self.t += 0.2 # Speed of gait cycle

def main(args=None):
    rclpy.init(args=args)
    node = GaitManagerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()