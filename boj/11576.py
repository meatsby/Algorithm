# Base Conversion

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
num = list(reversed(list(map(int, input().split()))))

temp = 0

for i in range(m):
    temp += num[i] * (a**i)

ans = []

while True:
    ans.append(temp%b)
    temp = temp//b
    if temp < b:
        ans.append(temp)
        break

print(*ans[::-1])
