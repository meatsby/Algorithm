# 생일
import sys
input = sys.stdin.readline

p = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    p.append([int(y), int(m), int(d), name])

print(sorted(p)[-1][3])
print(sorted(p)[0][3])
