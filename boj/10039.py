# 평균 점수
import sys
input = sys.stdin.readline

ans = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    ans += score

print(ans//5)
