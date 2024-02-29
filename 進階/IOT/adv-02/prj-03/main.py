from machine import Pin
from time import sleep
import mcu

gpio = mcu.gpio()
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

while True:
    RED.value(1)
    GREEN.value(0)
    BLUE.value(0)
    sleep(1)
    RED.value(0)
    GREEN.value(1)
    BLUE.value(0)
    sleep(1)
    RED.value(0)
    GREEN.value(0)
    BLUE.value(1)
    sleep(1)
