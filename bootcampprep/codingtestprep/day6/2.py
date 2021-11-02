# 오르막길
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
road = []
h = 0

for i in range(n-1):
    if p[i] < p[i+1]:
        road.append(p[i])
        road.append(p[i+1])
    else:
        if road:
            h = max(road[-1] - road[0], h)
        road = []

if road:
    h = max(road[-1] - road[0], h)

print(h)
