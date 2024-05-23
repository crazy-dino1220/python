import time
import mcu
from machine import Pin
import dht


gpio = mcu.gpio()
d=dht.DHT11(Pin(gpio.D0,Pin.IN))

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"Humidity:{hum:02d}, temperarute:{temp:02d}{'\u00b0'}C")
    time.sleep(1)