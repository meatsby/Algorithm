# 요세푸스 문제 0

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
circle = [i for i in range(1, n+1)]
order = 0
ans = []

for i in range(n, 0, -1):
    order = (order+k-1) % i
    temp = circle.pop(order)
    ans.append(temp)

print("<" + str(ans)[1:-1] + ">")
