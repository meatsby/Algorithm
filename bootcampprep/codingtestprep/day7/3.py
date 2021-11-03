# 줄 세우기
import sys
input = sys.stdin.readline

n, l = map(int,input().split())
num = 1
ans = []

while len(ans) < n:
    if str(l) not in str(num):
        ans.append(num)
    num += 1

print(ans[-1])
