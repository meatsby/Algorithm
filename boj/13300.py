# 방 배정
import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
male = [0]*7
female = [0]*7
ans = 0

for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        male[y] += 1
    else:
        female[y] += 1

for i in range(1, 6):
    male[i] = math.ceil(male[i]/k)
    female[i] = math.ceil(female[i]/k)

print(sum(male) + sum(female))
