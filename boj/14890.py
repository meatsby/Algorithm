# 경사로
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.extend(list(zip(*graph)))
ans = 0

for line in graph:
    isTrue = True
    canImp = [True for _ in range(n)]  # 경사로 배치 가능?
    i = 0
    while True:
        # print(i, end="")
        if i >= n-1:  # 범위내에서
            break
        elif canImp[i] and i < n-l and len(set(line[i:i+l])) == 1 and line[i]+1 == line[i+l]:  # 경사로를 통해 올라갈 경우
            for k in range(i, i+l):
                canImp[k] = False
            i += l
        elif canImp[i+1] and i < n-l and len(set(line[i+1:i+l+1])) == 1 and line[i]-1 == line[i+l]:  # 경사로를 통해 내려갈 경우
            for k in range(i+1, i+l+1):
                canImp[k] = False
            i += l
        elif i < n-1 and line[i] == line[i+1]:  # 같은 높이일 경우
            i += 1
        else:
            isTrue = False
            break
    if isTrue:
        ans += 1
    # print(isTrue)

print(ans)
