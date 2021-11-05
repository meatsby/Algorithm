# ABC
import sys
input = sys.stdin.readline

abc = sorted(map(int, input().split()))
s = input().rstrip()
ans = []

for i in s:
    if i == "A":
        ans.append(abc[0])
    if i == "B":
        ans.append(abc[1])
    if i == "C":
        ans.append(abc[2])

print(*ans)
