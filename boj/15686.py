# 치킨 배달
# 정답참고

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
town = []
house = []
chicken = []

for i in range(N):
    t = list(map(int, input().split()))
    town.append(t)
    for j in range(N):
        if t[j] == 1:
            house.append((i, j))
        elif t[j] == 2:
            chicken.append((i, j))

comb = combinations(chicken, M)
ans = float("inf")

for c in comb:  # 가능한 치킨집 경우의 수
    comb_min = 0
    for i, j in house:
        min_dis = float("inf")
        for x, y in c:
            chi_dis = abs(x-i) + abs(y-j)  # 각 치킨집과 집간의 치킨거리
            min_dis = min(chi_dis, min_dis)  # 경우의 수에서 최소 치킨거리
        comb_min += min_dis  # 경우의 수에서 모든 집간의 치킨거리
    ans = min(ans, comb_min)  # 최소 치킨거리를 갖는 조합

print(ans)
