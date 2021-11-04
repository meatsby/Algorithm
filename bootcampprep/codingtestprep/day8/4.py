# 소가 길을 건너간 이유 1
import sys
input = sys.stdin.readline

cow = [[-1]*10, [0]*10]

for _ in range(int(input())):
    n, d = map(int, input().split())
    if cow[0][n-1] == -1:
        cow[0][n-1] = d
        continue
    if cow[0][n-1] != d:
        cow[0][n-1] = d
        cow[1][n-1] += 1
        continue

print(sum(cow[1]))
