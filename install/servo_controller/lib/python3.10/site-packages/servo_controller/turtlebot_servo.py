import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ServoController(Node):
  def __init__(self):
      super().__init__('servo_controller')
      self.servo_pub = self.create_publisher(Float64, '/servo_command', 10)
      self.timer = self.create_timer(2.0, self.move_servo)
      self.servo_angle = 0.0

  def move_servo(self):
    msg = Float64()
    # Alternar entre 0 (bajar) y 1.0 (levantar)
    if self.servo_angle == 0.0:
        self.servo_angle = 1.0
    else:
        self.servo_angle = 0.0

    msg.data = self.servo_angle
    self.servo_pub.publish(msg)
    self.get_logger().info(f'Servo moved to {self.servo_angle}')


def main(args=None):
    rclpy.init(args=args)
    servo_controller = ServoController()
    rclpy.spin(servo_controller)
    servo_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()