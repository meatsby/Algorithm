# 기상캐스터
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cloud = [list(input().rstrip()) for _ in range(n)]
city = [[-1]*m for _ in range(n)]
t = 0

for _ in range(m):
    for i in range(n):
        for j in range(m):
            if cloud[i][j] == "c" and city[i][j] == -1:
                city[i][j] = t
    t += 1
    for i in range(n):
        cloud[i].pop()
        cloud[i].insert(0, ".")

for ct in city:
    print(*ct)
