from umqtt.simple import MQTTClient
import sys
import time
import mcu


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
# wi.scan()
if wi.connect():
    print(f"IP={wi.ip}")


MQTT = mcu.MQTT("Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")

MQTT.connect()

MQTT.subscribe("nobody", on_message)

while True:
    MQTT.check_msg()
    time.sleep(1)
