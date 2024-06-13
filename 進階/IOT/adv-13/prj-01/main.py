import whisper

model = whisper.load_model("base")
result = model.transcribe("adv-13/prj-01/錄製.m4a")
print(result["text"])
