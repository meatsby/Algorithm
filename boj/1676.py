# 팩토리얼 0의 개수
import math
import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(math.factorial(n), -1, -1):
    zeros = str(i).count("0")
    ans += zeros
    if zeros == 0:
        print(ans)
        break
