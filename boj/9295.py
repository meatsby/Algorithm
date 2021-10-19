# 주사워
import sys
input = sys.stdin.readline

for t in range(1, int(input())+1):
    c, v = map(int, input().split())
    print(f"Case {t}: {c+v}")
