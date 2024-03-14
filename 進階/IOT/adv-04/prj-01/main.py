from machine import Pin, ADC
from machine import Pin, PWM
from time import sleep
import mcu

gpio = mcu.gpio()
light_sensor = ADC(0)
frequency = 1000
duty_cycle = 0
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5), frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), frequency, duty=duty_cycle)

while True:
    light_sensor_reading = light_sensor.read()
    print(f"value={light_sensor_reading},{round(light_sensor_reading*100/1024)}%")
    if light_sensor_reading >= 600:
        RED.duty(light_sensor_reading)
    else:
        RED.duty(0)
