# 주사위 세개
import sys
input = sys.stdin.readline

eyes = [0, 0, 0, 0, 0, 0, 0]
for dice in list(map(int, input().split())):
    eyes[dice] += 1

if 3 in eyes:
    prize = 10000 + eyes.index(3)*1000
elif 2 in eyes:
    prize = 1000 + eyes.index(2)*100
else:
    for i in range(6, 0, -1):
        if eyes[i] == 1:
            prize = i*100
            break

print(prize)
