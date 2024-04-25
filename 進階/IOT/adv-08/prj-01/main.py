from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC
from machine import Pin, PWM
from time import sleep


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")
    m = msg


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
# wi.scan()
if wi.connect():
    print(f"IP={wi.ip}")

mq_sever = "mqtt.singularinnovation-ai.com"
MQTTClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
m = ""
mqClient0 = MQTTClient(
    MQTTClientId, mq_sever, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()  #
except:
    sys.exit()
finally:
    print("connected MQTT sever")

mqClient0.set_callback(on_message)
mqClient0.subscribe("nobody")


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
    mqClient0.check_msg()
    mqClient0.ping()
    if m == "on":
        RED.duty(1023)
        BLUE.duty(1023)
        GREEN.duty(1023)
    elif m == "off":
        RED.duty(0)
        BLUE.duty(0)
        GREEN.duty(0)
    elif m == "auto":
        if light_sensor_reading > 600:
            RED.duty(1023)
            BLUE.duty(1023)
            GREEN.duty(1023)
        else:
            RED.duty(0)
            BLUE.duty(0)
            GREEN.duty(0)
    time.sleep(1)
