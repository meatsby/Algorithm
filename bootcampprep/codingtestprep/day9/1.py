# 행복
import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

print(max(score) - min(score))
