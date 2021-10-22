# 이진수
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = list(reversed(format(n, "b")))
    ans = []

    for i in range(len(b)):
        if b[i] == "1":
            ans.append(i)
    
    print(*ans)
