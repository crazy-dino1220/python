import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
from langchain_core.messages import HumanMessage


while True:
    ans = input("請輸入想跟AI說的話:")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個控制室內燈光開關的人
                你可以根據使用者說的話來判斷是否要開燈
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
    print(msg.content)
