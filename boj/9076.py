# 점수 집계
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    scores = sorted(map(int, input().split()))
    if scores[3] - scores[1] >= 4:
        print("KIN")
    else:
        print(sum(scores[1:4]))
