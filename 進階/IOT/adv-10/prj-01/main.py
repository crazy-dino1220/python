from machine import Pin, I2C
import mcu
import ssd1306
from umqtt.simple import MQTTClient
import sys
import time
import mcu


def on_message(topic, msg):
    global mesg
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")
    mesg = msg


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
# wi.scan()
if wi.connect():
    print(f"IP={wi.ip}")
mesg = ""

MQTT = mcu.MQTT("Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")

MQTT.connect()

MQTT.subscribe("nobody", on_message)

gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    MQTT.check_msg()
    oled.fill(0)
    oled.text(f"IP={wi.ip}", 0, 0)
    oled.text(mesg, 0, 20)
    oled.text("Topic=nobody", 0, 10)
    oled.show()
    time.sleep(0.1)
