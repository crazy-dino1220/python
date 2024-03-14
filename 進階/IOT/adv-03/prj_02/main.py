from machine import Pin, PWM
from time import sleep
import mcu


frequency = 1000
duty_cycle = 0
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5), frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), frequency, duty=duty_cycle)
delay = 0.002
while True:
    for duty_cycle in range(1023, -1, -1):
        RED.duty(duty_cycle)
        GREEN.duty(1023 - duty_cycle)
        sleep(delay)
    for duty_cycle in range(1023, -1, -1):
        GREEN.duty(duty_cycle)
        BLUE.duty(1023 - duty_cycle)
        sleep(delay)
    for duty_cycle in range(1023, -1, -1):
        BLUE.duty(duty_cycle)
        RED.duty(1023 - duty_cycle)
        sleep(delay)
