# Yangjojang of The Year
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = []
    for i in range(int(input())):
        uni, lit = input().rstrip().split()
        lit = int(lit)
        l.append((uni, lit))
    l = sorted(l, key = lambda x : x[1], reverse=True)
    print(l[0][0])
