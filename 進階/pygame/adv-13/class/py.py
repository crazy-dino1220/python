from collections import deque

snack_queue = deque()

snack_queue.append("1")
snack_queue.append("2")
snack_queue.append("3")

print(f"初始列隊:{snack_queue}")

firth_student = snack_queue.popleft()
print(f"{firth_student}已經買完點心並離開列隊")
print(f"現在的列隊:{snack_queue}")
snack_queue.append("4")
print(f"4家加入列隊")

(f"最終列隊:{snack_queue}")
