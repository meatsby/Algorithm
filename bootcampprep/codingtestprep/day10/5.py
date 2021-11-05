# 개미
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]
    mx, mn = 0, 0

    for ant in ants:
        if ant > l-ant:
            mx = max(mx, ant)
            mn = max(mn, l-ant)
        else:
            mx = max(mx, l-ant)
            mn = max(mn, ant)
    
    print(mn, mx)
