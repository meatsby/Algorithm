# 한 줄로 서기

import sys
input = sys.stdin.readline

n = int(input())
inf = list(map(int, input().split()))
ppl = [n] * n

for i in range(n):
    temp = 0
    for j in range(n):
        if temp == inf[i] and ppl[j] == n:
            ppl[j] = i+1
            break
        elif ppl[j] > i+1:
            temp += 1

print(*ppl)
