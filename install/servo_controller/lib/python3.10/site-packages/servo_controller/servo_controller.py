import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import sys
import termios
import tty

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.servo1_pub = self.create_publisher(Float64, '/servo1_command', 10)
        self.servo2_pub = self.create_publisher(Float64, '/servo2_command', 10)
        self.servo1_angle = 0.0
        self.servo2_angle = 0.0
    
    def move_servo1(self, angle):
        msg = Float64()
        self.servo1_angle = angle
        msg.data = self.servo1_angle
        self.servo1_pub.publish(msg)
        self.get_logger().info(f'Servo 1 moved to {self.servo1_angle}')

    def move_servo2(self, angle):
        msg = Float64()
        self.servo2_angle = angle
        msg.data = self.servo2_angle
        self.servo2_pub.publish(msg)
        self.get_logger().info(f'Servo 2 moved to {self.servo2_angle}')

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

def main(args=None):
    rclpy.init(args=args)
    servo_controller = ServoController()

    try:
        while rclpy.ok():
            key = servo_controller.get_key()
            if key == 'w':
                servo_controller.move_servo1(1.0)
                servo_controller.move_servo2(1.0)
            elif key == 's':
                servo_controller.move_servo1(0.0)
                servo_controller.move_servo2(0.0)
            elif key == '\x03':  # Ctrl+C
                break
    except Exception as e:
        servo_controller.get_logger().error(f'Exception: {e}')
    finally:
        servo_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()