# 더하기
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(sum(l))
