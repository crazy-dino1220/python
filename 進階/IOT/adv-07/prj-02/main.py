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

mq_sever = "mqtt.singularinnovation-ai.com"
MQTTClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    MQTTClientId, mq_sever, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT sever")

mqClient0.set_callback(on_message)
mqClient0.subscribe("nobody")

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)
