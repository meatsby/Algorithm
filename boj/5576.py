# 콘테스트
import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(20)]
w = sorted(scores[:10], reverse=True)
k = sorted(scores[10:], reverse=True)

print(sum(w[:3]), sum(k[:3]))
