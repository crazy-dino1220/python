import getpass
import os
import paho.mqtt.client as mqtt
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.2)

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()

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
    result = client.publish("nobody", ans + ":" + msg.content)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成
    print(msg.content)
    # while True:
    # msg = input("請輸入想上傳MQTT的訊息:")

    # # 檢查發布是否成功
    # if result.rc == mqtt.MQTT_ERR_SUCCESS:
    #     print("Message published successfully")
    # else:
    #     print("Failed to publish message")
    # time.sleep(0.1)
