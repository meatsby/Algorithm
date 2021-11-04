# 방 배정
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [[0]*2 for _ in range(6)]
ans = 0

for _ in range(n):
    s, y = map(int, input().split())
    students[y-1][s-1] += 1

for y in range(6):
    for s in range(2):
        if students[y][s]%k == 0:
            ans += students[y][s]//k
        else:
            ans += students[y][s]//k + 1

print(ans)
