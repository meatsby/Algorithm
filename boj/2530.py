# 인공지능 시계
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())
h = (a + (b + (c+d)//60)//60)%24
m = (b + (c+d)//60)%60
s = (c+d)%60

print(h, m, s)
