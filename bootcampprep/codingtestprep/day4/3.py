# 슈퍼 마리오
import sys
input = sys.stdin.readline

score = 0
mushs = [int(input()) for _ in range(10)]

for mush in mushs:
    after = score + mush
    if after >= 100:
        if after - 100 > 100 - score:
            break
    score = after

print(score)
