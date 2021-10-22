# 나는 요리사다
import sys
input = sys.stdin.readline

num, score = 0, 0

for i in range(1, 6):
    scores = sum(list(map(int, input().split())))
    if scores > score:
        num, score = i, scores

print(num, score)
