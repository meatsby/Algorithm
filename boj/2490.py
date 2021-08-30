# 윷놀이

import sys
input = sys.stdin.readline
yut = ["E", "A", "B", "C", "D"]

for _ in range(3):
    n = list(map(int, input().split()))
    print(yut[n.count(0)])
