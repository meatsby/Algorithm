import time
start = time.time()  # 시작 시간 저장
 
num = int(input())
hansu = 0

if num <= 99:
    hansu = num
else:
    hansu = 99
    for n in range(100, num+1):
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1

print(hansu)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
