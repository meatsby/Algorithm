# 이분 그래프
from collections import deque
import sys
input = sys.stdin.readline

def bfs(k):
    group[k] = 1  # 시작점을 그룹1로 선언
    q = deque()
    q.append(k)
    while q:
        x = q.popleft()
        for i in l[x]:  # x와 인접한 정점들 중
            if group[i] == 0:  # 그룹핑이 안되어있을 경우
                group[i] = -group[x]  # 그룹-1로 선언
                q.append(i)
            elif group[i] == group[x]:  # 인접한 정점인데 같은 그룹일 경우 이분그래프가 아님
                return False
    return True

for t in range(int(input())):
    v, e = map(int, input().split())
    l = [[] for _ in range(v+1)]  # 인접리스트 선언
    group = [0] * (v+1)  # 두개의 그룹으로 나누기
    isBin = True

    for _ in range(e):
        a, b = map(int, input().split())  # 인접리스트로 저장
        l[a].append(b)
        l[b].append(a)

    for k in range(1, v+1):
        if group[k] == 0:  # 아직 그룹핑이 안된 정점들일 경우
            if not bfs(k):
                isBin = False
                break

    print("YES" if isBin else "NO")
