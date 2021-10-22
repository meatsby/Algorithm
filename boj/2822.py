# 점수 계산
import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(8)]
final = sorted(scores, reverse=True)[:5]
ans = []

for score in final:
    ans.append(scores.index(score) + 1)

print(sum(final))
print(*sorted(ans))
