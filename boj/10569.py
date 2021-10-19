# 다면체
import sys
input = sys.stdin.readline

for t in range(int(input())):
    v, e = map(int, input().split())
    print(2+e-v)
