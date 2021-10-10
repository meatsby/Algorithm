# 오븐 시계
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
h = (a + (b+c)//60)%24
m = (b+c)%60

print(h, m)
