# 등수 구하기
import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
score = list(map(int, input().split()))
board = [-1] * p
ans = 0

for i in range(n):
    board[i] = score[i]

if new <= board[-1]:
    ans = -1
else:
    for i in range(p):
        if new >= board[i]:
            ans = i + 1
            break

print(ans)
