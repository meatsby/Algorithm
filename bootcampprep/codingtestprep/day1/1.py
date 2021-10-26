# 대회 or 인턴
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
team = min(n//2, m)
f = n - team * 2
m = m - team
left = f + m
need = k - left

if need > 0:
    print((team*3 - need)//3)
else:
    print(team)