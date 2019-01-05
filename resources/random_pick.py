import random
from time import sleep

students = ["김민주", "최익창", "조대영", "권오동", "김지한", "김영훈"]

random.shuffle(students)


print("발표 순서 추첨을 시작합니다")
for i in range(1,10+1):
    print(i)
    sleep(1)

print("결과는")
print(students)
