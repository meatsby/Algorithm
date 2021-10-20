# 점수계산
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ans = 0
temp = 0

for i in l:
    if i == 1:
        temp += 1
    elif i == 0:
        temp = 0
    ans += temp

print(ans)
