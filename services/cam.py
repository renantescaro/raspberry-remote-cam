from services.servo_motor import ServoMotor
from services.setting import Setting

class Camera:
    def __init__(self):
        self.porta_servo_vertical = int(Setting.get('PORT_SERVO_VERTICAL'))
        self.porta_servo_horizontal = int(Setting.get('PORT_SERVO_HORIZONTAL'))

    def mover_vertical(self, angulo):
        servo_motor = ServoMotor(port=self.porta_servo_vertical)
        servo_motor.set_angle(angulo)

    def mover_horizontal(self, angulo):
        servo_motor = ServoMotor(port=self.porta_servo_horizontal)
        servo_motor.set_angle(angulo)
