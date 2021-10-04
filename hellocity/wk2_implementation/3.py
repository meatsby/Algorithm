# 백준 10250번: ACM 호텔

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = ((n-1)%h + 1) * 100
    room = (n-1)//h + 1
    print(floor + room)
