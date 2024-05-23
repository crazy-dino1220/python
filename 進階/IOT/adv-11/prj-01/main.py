import time
import mcu


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)

mqtt_client.connect()

while True:
    msg = input("text:")
    topic = input("topic:")
    mqtt_client.publish(topic, msg)
    time.sleep(0.1)
