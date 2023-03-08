import os

# file_path = "C:\\Users\\user\\Documents\\TRPG.docx"
# if os.path.isfile(file_path):
#     print("檔案存在")
# else:
#     print("檔案不存在")

#1. 要開啟的檔名
fileName = "good.txt"
#2. 指定w/ r /a mode
Mode = "r"
#3. 開啟檔案
myFile = open(fileName, Mode)
#4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("How old are you?")

total = myFile.read()
print(total)
#5. 關閉檔案
myFile.close()