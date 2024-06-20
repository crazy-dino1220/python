
import getpass
import os
import paho.mqtt.client as mqtt
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")

def on_connect(client, userdata, mid, reason_code, properties):
    print(f"連線結果:{reason_code}")
    client.subscribe("home")

def on_message(client, userdata, msg):
    global home_config

    home_config=str(msg.payload.decode('utf-8'))

os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.2)
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
home_config = "None"
while True:
    ans = input("請輸入想跟AI說的話:")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個控制室內燈光開關的人
                你可以根據使用者說的話來判斷是否要開燈
                若用戶想出門，記得幫她關燈
                你只能回答'on'、'off'、'None'或'open'或'close'，可以同時回答多個
                'on'代表開燈
                'off'代表關燈
                'None'不動作
                'open'是開車庫門
                'close'是關車庫門
                不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    )
    result = client.publish("home", ans + ":" + msg.content)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成
    print(msg.content)

    if msg == "home_config":
        msg = model.invoke(
            [
                HumanMessage(
                    content="""
                你是一個負責解釋家裡狀況的小幫手，目前家裡的狀況是:
                    """
                ),content
                print(msg)
            ]
        )

## def on_message(topic, msg):
#     global mesg
#     msg = msg.decode("utf-8")
#     topic = topic.decode("utf-8")
#     print(f"my subscribe topic:{topic},msg:{msg}")
#     mesg = msg
