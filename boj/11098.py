# 첼시를 도와줘!
import sys
input = sys.stdin.readline

for t in range(int(input())):
    l = []
    for p in range(int(input())):
        c, name = input().split()
        l.append((int(c), name))
    print(sorted(l, reverse=True)[0][1])
