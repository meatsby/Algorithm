# 화성 수학
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mars = list(input().rstrip().split())
    n = float(mars[0])
    for i in range(1, len(mars)):
        if mars[i] == "@":
            n *= 3
        elif mars[i] == "%":
            n += 5
        else:
            n -= 7
    print('%.2f' % n)
