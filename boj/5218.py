# 알파벳 거리
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = input().rstrip().split()
    ans = []
    for i in range(len(x)):
        a = ord(y[i]) - ord(x[i]) + 26 if ord(y[i]) - ord(x[i]) < 0 else ord(y[i]) - ord(x[i])
        ans.append(a)
    print("Distances: ", end="")
    print(*ans)
