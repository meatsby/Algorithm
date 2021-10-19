# 약수 구하기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

y = []
for i in range(1, n+1):
    if n%i == 0:
        y.append(i)

if len(y) < k:
    print(0)
else:
    print(y[k-1])
